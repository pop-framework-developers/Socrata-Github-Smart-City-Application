'''
Created on 4/10/2015

@author: aeprieto
'''
import requests
import re



def checkingURL(url):
    lastURL=url
    try:
        r = requests.get(url)
        if r.url!=url:
            lastURL=r.url
            print 'redirect',r.url
            checkingURL(lastURL)
    except requests.exceptions.SSLError:
        if re.search('^https',url): 
            urlsinhttps=url[0:4]+url[5:]
            print 'rechecking', urlsinhttps
            lastURL=checkingURL(urlsinhttps)
        elif re.search('^http:',url):
            print 'dejamos url como estaba',url 
            lastURL=url      
        else:
            print '--Error checking URL', url
            lastURL='not_available'
    except:
        print '--Error main checking url', url
        lastURL='not_available'
    if re.search('(.*)login$',lastURL):
        lastURL=lastURL[:len(lastURL)-5]
    if re.search('.*://www.socrata.com.*',lastURL):
        lastURL='not_available'
    print 'l', lastURL
    return lastURL

checkingURL('http://www.metrochicagodata.com')

