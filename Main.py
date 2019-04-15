import Handler as AppHandler
import os
import pyodbc

class Main:
    def __init__(self):
        try:
            AppHandler.Handler()
        except(Exception, pyodbc.DatabaseError) as error:
            print(error)
            os._exit


if __name__ == '__main__':
    def runTheApp():
        try:
            Main()
        except Exception as error:
            print("[!]ERROR[!] Please check: {}".format(error))
    runTheApp()