#script which create a view called socrata_data_city_usalooks for data.json at socrata portals and store the info of every dataset in socrata_data table
import bdUtils
import jsonUtils
import sqlite3
import re

#open db
conn=bdUtils.openDB()
conn.row_factory = sqlite3.Row

                          
try:
    socrata_data_createview_cursor=conn.cursor()
    socrata_data_createview_cursor.execute('CREATE VIEW "Socrata_DCAT_CITY_USA" AS select distinct identifier, keyword, theme, title,description from socrata_data where id_customer in (select id_customer from socrata_customers where type="City" and country="USA")')
except:
    print 'Create failed'
conn.commit()
  
print '--BD  updated!'
conn.close()
print '--BD  closed!'

