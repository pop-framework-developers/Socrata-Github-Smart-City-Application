
import re
import bdUtils
import jsonUtils
import urlUtils

#probamos a abrir base de datos, si toda va bien continuamos
conn=bdUtils.openDB()

jsonsocrata = jsonUtils.askSocrataCustomersJSONURL()

datos= jsonUtils.openJSON(jsonsocrata)

if datos=='noJSON':
    conn.close()
    exit()
    
js = jsonUtils.loadJSON(datos)
  
if js=='noparsedJSON':
    conn.close()
    exit()

    
    #creamos la tabla socrata_customers si no existe
try:
    socrata_data_createtable_cursor=conn.cursor()
    socrata_data_createtable_cursor.execute(
        'CREATE TABLE if not exists "socrata_customers" ("id_customer" INTEGER PRIMARY KEY NOT NULL,"customer_name" TEXT,"type" TEXT,"location_name" TEXT DEFAULT (null),"country" TEXT, "open_data_site_url" TEXT, "api_dcat_url" TEXT, "api_data_url" TEXT, "longitude" TEXT,"latitude" TEXT)')
except:
    print 'Create failed'
    conn.close()
    exit()
    
    #para cada elemento del json
for elemento in js: 
    #obtenemos el customer_name
    customer_name=elemento.get('customer_name','not_available')
    #obtenemos el portal_type
    portal_type=elemento.get('type','not_available')
    #obtenemos el country
    country=elemento.get('country','not_available')
    #obtenemos location_city
    location_1=elemento.get('location_1','not_available')
    if location_1=='not_available':
        location_name='not_available'
        longitude='not_available'
        latitude='not_available'
    else:
        longitude=location_1.get('longitude','not_available')
        latitude=location_1.get('longitude','not_available')
        human_address=location_1.get('human_address','not_available')
        if human_address=='not_available':location_name='not_available'
        else: 
            city=re.findall('.+city":"(.+?)"',human_address)
            location_name=city[0]
    #obtenemos urls
    url=elemento.get('open_data_site_url','not_available')
    if url=='not_available':
        open_data_site_url=url
        api_dcat_url=url
        api_data_url=url
        #print 'open_data_site_url', open_data_site_url 
    else:
        open_data_site_url=url.get('url','not_available')
        if open_data_site_url!='not_available':
            open_data_site_url=urlUtils.checkingURL(open_data_site_url)
            if open_data_site_url!='not_available':
                if open_data_site_url[len(open_data_site_url)-1]=='/':
                    api_dcat_url=open_data_site_url+'api/dcat.json'
                    api_data_url=open_data_site_url+'api/data.json'
                else:
                    open_data_site_url=open_data_site_url+'/'
                    api_dcat_url=open_data_site_url+'api/dcat.json'
                    api_data_url=open_data_site_url+'api/data.json'
    cur = conn.cursor()
#insercion de la tupla solo si tiene una url en open_data_site_url
    if open_data_site_url!='not_available':
    #comprobamos si ya existe una tupla con ese open_data_site_url
        cur.execute('SELECT id_customer FROM socrata_customers WHERE open_data_site_url = ?',(open_data_site_url,))
        id_customer = cur.fetchone()
        #si existe actualizamos la tupla sin modificar el id_customer
        if id_customer is not None:
            try:
                cur.execute('UPDATE  socrata_customers SET type=?,location_name=?,country=?,customer_name=?,api_dcat_url=?,api_data_url=?,longitude=?,latitude=? WHERE id_customer=?',(portal_type,location_name,country,customer_name,api_dcat_url,api_data_url,longitude,latitude,id_customer[0]))
            except: 
                print 'actualizacion fallida con la tupla con open_data_site_url: ',open_data_site_url
        #si no existe insertamos los datos de esa nueva tupla 
        else:
            try:
                cur.execute('INSERT INTO socrata_customers(customer_name,type,location_name,country,open_data_site_url,api_dcat_url,api_data_url,longitude,latitude) VALUES (?,?,?,?,?,?,?,?,?)',(customer_name,portal_type,location_name,country,open_data_site_url,api_dcat_url,api_data_url,longitude,latitude))
            except: 
                print 'insercion fallida con la tupla con open_data_site_url: ', open_data_site_url
            
conn.commit()
print '--BD  updated!'
conn.close()
print '--BD  closed!'
