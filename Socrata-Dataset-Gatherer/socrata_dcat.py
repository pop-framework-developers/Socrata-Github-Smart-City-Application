#script which looks for dcat.json at socrata portals and store the info of every dataset in socrata_dcat table
import bdUtils
import jsonUtils
import sqlite3
import re

#open db
conn=bdUtils.openDB()
conn.row_factory = sqlite3.Row

try:
    socrata_data_createtable_cursor=conn.cursor()
    socrata_data_createtable_cursor.execute('CREATE TABLE if not exists "socrata_dcat" ("identifier" TEXT NOT NULL ,"webService" TEXT,"accessURL" TEXT,"feed" TEXT,"keyword" TEXT,"theme" TEXT,"title" TEXT,"created" TEXT,"releaseDate" TEXT,"modified" TEXT,"description" TEXT,"id_customer" INTEGER,PRIMARY KEY (identifier,id_customer),FOREIGN KEY(id_customer) REFERENCES "socrata_customers"(id_customer))')
        
except:
    print 'Create failed'
    conn.close()
    exit()

#query dcat.json URLs
socrata_customers_cursor = conn.cursor()
socrata_customers_cursor.execute('SELECT id_customer,customer_name,open_data_site_url,api_dcat_url FROM socrata_customers')

rows = socrata_customers_cursor.fetchall()

portals_without_extract=list()
print 'socrata_customers'
#extract data
for row in rows :
    print row['id_customer'],row['customer_name'],row['open_data_site_url'],row['api_dcat_url']
    if row['api_dcat_url']=='not_available':
        portals_without_extract.append(('api_dcat_url_not_available',row['id_customer'],row['customer_name'],row['open_data_site_url'],row['api_dcat_url'])) 
    else:    
        datos= jsonUtils.openJSON(row['api_dcat_url'])
        if datos=='noJSON': 
            portals_without_extract.append(('noJSON',row['id_customer'],row['customer_name'],row['open_data_site_url'],row['api_dcat_url'])) 
        else:
            js = jsonUtils.loadJSON(datos)
            if js=='noparsedJSON': 
                portals_without_extract.append(('noparsedJSON',row['id_customer'],row['customer_name'],row['open_data_site_url'],row['api_dcat_url'])) 
            else:
                #for every json element
                for elemento in js:
                    try: 
                        #obtain identifier
                        identifier=elemento.get('identifier','not_available')
                        #check right socrata id and store it
                        if re.search('[a-z0-9]{4}-[a-z0-9]{4}',identifier) is None:continue
                        #obtain webService
                        webService=elemento.get('webService','not_available')
                        #obtain accessURL
                        accessURL=elemento.get('accessURL','not_available')
                        #obtain feed
                        feed=elemento.get('feed','not_available')
                        #obtain keyword
                        keyword=elemento.get('keyword','not_available')
                        #obtain theme
                        theme=elemento.get('theme','not_available')
                        #obtain title
                        title=elemento.get('title','not_available')
                        #obtain created
                        created=elemento.get('created','not_available')
                        #obtain releaseDate
                        releaseDate=elemento.get('releaseDate','not_available')
                        #obtain modified
                        modified=elemento.get('modified','not_available')
                        #obtain description
                        description=elemento.get('description','not_available')
                    except: 
                        print 'extraccion de elemento de json incorrecta con elemento', elemento, 'fila de la db', row['id_customer'],row['customer_name'],row['open_data_site_url'],row['api_dcat_url']
                        portals_without_extract.append(('json extracted wrong '+str(elemento),row['id_customer'],row['customer_name'],row['open_data_site_url'],row['api_dcat_url'])) 
                        continue
                    #insert row
                    failed_insertions=list()
                    try:
                        socrata_dcat_insert_cursor=conn.cursor()
                        socrata_dcat_insert_cursor.execute('INSERT OR IGNORE INTO socrata_dcat(identifier,webService,accessURL,feed,keyword,theme,title,created,releaseDate,modified,description,id_customer) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',(identifier,webService,accessURL,feed,keyword,theme,title,created,releaseDate,modified,description,row['id_customer']))
                    except:
                        failed_insertions.append((row['id_customer'],row['customer_name'],row['open_data_site_url'],row['api_dcat_url'], identifier)) 
                        print 'insercion fallida con la tupla de: ', row['id_customer'],row['customer_name'],row['open_data_site_url'],row['api_dcat_url'],identifier
    conn.commit()
    print '--Finished BD update with data of:', row['id_customer'],row['customer_name'],row['open_data_site_url'],row['api_dcat_url']
           
conn.commit()
print '--BD  updated!'
conn.close()
print '--BD  closed!'
print 'portals failed:'
with open('portals_failed_dcat.txt', 'w') as fportals:
    for portal in portals_without_extract:
        fportals.write("{}\n".format(portal))
        print portal
print 'insertions failed:'
with open('insertions_failed_dcat.txt', 'w') as finsertions:
    for insertion in failed_insertions:
        finsertions.write("{}\n".format(insertion))
        print insertion
print 'dcat load finished'
    
    
    
    


