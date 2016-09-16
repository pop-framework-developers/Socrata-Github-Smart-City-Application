import os
import sqlite3
'''
Created on 3/10/2015

@author: aeprieto

Python Utils to use with sqlite databases
Define 2 functions:
    askDBPath checks if a sqlite database exists in the specified path
        default path is: ..\db\OpenDataCatalogs.sqliteOpenDataCatalogs.sqlite

    openDB open the sqlite database specified to the function askDBPath
'''
def askDBPath():
    print('Enter the complete path of the BD')
    print(r'Default: ..\db\OpenDataCatalogs.sqlite')
    dbPath = raw_input("Enter Path:")
    if len(dbPath) < 1 : dbPath = r'..\db\OpenDataCatalogs.sqlite'
    return dbPath

def createDB():
    try:
        print 'bd to create', ruta
        conn = sqlite3.connect(ruta)
        print '==== db created OK ===='
    except:
        print '==== error creating DB: path or db name wrong===='
        conn='noDB'
        exit()
    return conn
    
def openDB():
    ruta=askDBPath()
    try:
        if os.path.exists(ruta):
            conn = sqlite3.connect(ruta)
            print '==== db opened OK ===='
        else: 
            raise()
    except:
        print '==== error opening DB: path or db name wrong===='
        conn='noDB'
        try:
            print 'bd to create', ruta
            conn = sqlite3.connect(ruta)
            print '==== db created OK ===='
        except:
            print '==== error creating DB: path or db name wrong===='
            conn='noDB'
            exit()
    return conn


