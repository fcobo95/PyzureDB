import pyodbc
from Reader import Reader
import os
import getpass

class ApplicationConnector:

    @staticmethod
    def checkForTryAgain():
        return input(">>Want to try again? [Y/N]\n")

    @staticmethod
    def checkForMoreInputs():
        return input(">>Do you want to keep using the app? [Y/N]\n")

    @staticmethod
    def checkForMoreInserts():
        return input(">>Do you want to insert more values?[Y/N]\n")

    @staticmethod
    def checkForQuit(theOption):
        theQuitOptions = ["\quit", "quit", "exit", "terminate", "end", "close"]
        if theOption in theQuitOptions:
            return theOption

    @staticmethod
    def clearScreen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def closeApp():
        os._exit

    @staticmethod
    def formatTheError(theError):
        return "Error: {}".format(theError)

    def __init__(self):
        self.theConnection = None
        self.readThe = Reader().theReader

        try:
            theUser = input(">>Enter the username:\n")
            self.clearScreen()
            thePassword = getpass.getpass(">>Password for {}: ".format(theUser))
            self.clearScreen()
            
            theServer = self.readThe['server']
            thePort = self.readThe['port']
            theDriver = self.readThe['driver']
            
            theDBName = input(">>Enter the database you want to connect to:\n")
            self.clearScreen()
            if theDBName == " " or "":
                theDBName = self.readThe['defaultDB']
            theConnectionString = "DRIVER={};SERVER={};PORT={};DATABASE={};UID={};PWD={}".format(theDriver, theServer,
                                                                                                 thePort, theDBName,
                                                                                                 theUser, thePassword)
            self.theConnection = pyodbc.connect(theConnectionString, autocommit=True)
            print(theConnectionString)
            self.theCursor = self.theConnection.cursor()
        except (Exception, pyodbc.DatabaseError) as error:
            print("Something happened")
            print(self.formatTheError(error))
            os._exit