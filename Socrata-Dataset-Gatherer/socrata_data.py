#script which looks for data.json at socrata portals and store the info of every dataset in socrata_data table
import bdUtils
import jsonUtils
import sqlite3
import re

#open db
conn=bdUtils.openDB()
conn.row_factory = sqlite3.Row

try:
    socrata_data_createtable_cursor=conn.cursor()
    socrata_data_createtable_cursor.execute('CREATE TABLE if not exists "socrata_data" ("identifier" TEXT NOT NULL ,"api_url" TEXT,"landingPage" TEXT,"publisher" TEXT,"keyword" TEXT,"theme" TEXT,"title" TEXT,"issued" TEXT,"modified" TEXT,"description" TEXT,"id_customer" INTEGER,PRIMARY KEY (identifier,id_customer),FOREIGN KEY(id_customer) REFERENCES "socrata_customers"(id_customer))')
        
except:
    print 'Create failed'
    conn.close()
    exit()


#query data.json URLs
socrata_customers_cursor = conn.cursor()
socrata_customers_cursor.execute('SELECT id_customer,customer_name,open_data_site_url,api_data_url FROM socrata_customers')

rows = socrata_customers_cursor.fetchall()


portals_without_extract=list()
print 'socrata_customers'
#extract data
for row in rows :
    print row['id_customer'],row['customer_name'],row['open_data_site_url'],row['api_data_url']
    if row['api_data_url']=='not_available':
        portals_without_extract.append(('api_data_url_not_available',row['id_customer'],row['customer_name'],row['open_data_site_url'],row['api_data_url'])) 
    else:    
        datos= jsonUtils.openJSON(row['api_data_url'])
        if datos=='noJSON': 
            portals_without_extract.append(('noJSON',row['id_customer'],row['customer_name'],row['open_data_site_url'],row['api_data_url'])) 
        else:
            js = jsonUtils.loadJSON(datos)
            if js=='noparsedJSON': 
                portals_without_extract.append(('noparsedJSON',row['id_customer'],row['customer_name'],row['open_data_site_url'],row['api_data_url'])) 
            else: 
            #for every json element
                dataset=js.get('dataset','not_available')
                if dataset=='not_available':
                    portals_without_extract.append(('nodatasetinjson',row['id_customer'],row['customer_name'],row['open_data_site_url'],row['api_data_url'])) 
                else:
                    for elemento in dataset:
                        try: 
                            #obtain identifier & api_url
                            api_url=elemento.get('identifier','not_available')
                            identifierlist=re.findall('[a-z0-9]{4}-[a-z0-9]{4}',api_url)
                            #check right socrata id and store it
                            if identifierlist is None:continue
                            identifier=identifierlist[0]
                            #obtain landingPage
                            landingPage=elemento.get('landingPage','not_available')
                            #obtain publisher
                            publisherlist=elemento.get('publisher','not_available')
                            publisher= publisherlist['name']
                            #obtain keyword
                            keywords=elemento.get('keyword','not_available')
                            if keywords!='not_available':
                                delimitador=','
                                keyword=delimitador.join(keywords)
                            else: keyword=''
                            #obtain theme
                            themes=elemento.get('theme','not_available')
                            if themes!='not_available':
                                if len(themes)>1:
                                    delimitador=','
                                    theme=delimitador.join(themes)
                                else: theme=themes[0]
                            else: theme=''
                            #obtain title
                            title=elemento.get('title','not_available')
                            #obtain issued
                            issued=elemento.get('issued','not_available')
                            #obtain modified
                            modified=elemento.get('modified','not_available')
                            #obtain description
                            description=elemento.get('description','not_available')
                        except: 
                            print 'extraccion de elemento de json incorrecta con elemento', elemento, 'fila de la db', row['id_customer'],row['customer_name'],row['open_data_site_url'],row['api_data_url']
                            portals_without_extract.append(('json extracted wrong '+str(elemento),row['id_customer'],row['customer_name'],row['open_data_site_url'],row['api_data_url'])) 
                            continue
                        #insert row
                        failed_insertions=list()                 
                        try:
                            socrata_data_insert_cursor=conn.cursor()
                            socrata_data_insert_cursor.execute('INSERT OR IGNORE INTO socrata_data(identifier,api_url,landingPage,publisher,keyword,theme,title,issued,modified,description,id_customer) VALUES (?,?,?,?,?,?,?,?,?,?,?)',(identifier,api_url,landingPage,publisher,keyword,theme,title,issued,modified,description,row['id_customer']))
                        except:
                            failed_insertions.append((row['id_customer'],row['customer_name'],row['open_data_site_url'],row['api_data_url'], identifier)) 
                            print 'insercion fallida con la tupla de: ', row['id_customer'],row['customer_name'],row['open_data_site_url'],row['api_data_url'],identifier
    conn.commit()
    print '--Finished BD  updated with data of:', row['id_customer'],row['customer_name'],row['open_data_site_url'],row['api_data_url']
conn.commit()
print '--BD  updated!'
conn.close()
print '--BD  closed!'
print 'portals failed:'
with open('portals_failed_data.txt', 'w') as fportals:
    for portal in portals_without_extract:
        fportals.write("{}\n".format(portal))
        print portal
print 'insertions failed:'
with open('insertions_failed_data.txt', 'w') as finsertions:
    for insertion in failed_insertions:
        finsertions.write("{}\n".format(insertion))
        print insertion
print 'data load finished'
    
    
    
    


