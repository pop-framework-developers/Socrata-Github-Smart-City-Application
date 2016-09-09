import json
import urllib
import re
'''
Created on 3/10/2015

@author: aeprieto
'''
from string import lower

def askSocrataCustomersJSONURL():
    print('Enter the complete URL of JSON Socrata Customers')
    print(r'Default: https://opendata.socrata.com/resource/6wk3-4ija.json')
    scJSONURL = raw_input("Enter URL:")
    if len(scJSONURL) < 1 : scJSONURL = r'https://opendata.socrata.com/resource/6wk3-4ija.json'
    return scJSONURL

def openJSON(jsonURL):
    try:
        print '--Downloading ', jsonURL
        uh = urllib.urlopen(jsonURL)
        datos = uh.read()
        print '--JSON download OK'
    except IOError:
        if re.search('^https',jsonURL): 
            jsonURLsinhttps=jsonURL[0:4]+jsonURL[5:]
            print '--trying JSON download without https'
            datos=openJSON(jsonURLsinhttps)  
        else:
            print '--Error downloading JSON', jsonURL
            datos='noJSON'
    except:
        print '--Error downloading JSON: ', jsonURL
        datos='noJSON'
    return datos

def loadJSON(jsondata):
    try: 
        print '--Parsing JSON'
        js = json.loads(jsondata)
    except: 
        print '--Error parsing JSON'
        js = 'noparsedJSON'
    return js



