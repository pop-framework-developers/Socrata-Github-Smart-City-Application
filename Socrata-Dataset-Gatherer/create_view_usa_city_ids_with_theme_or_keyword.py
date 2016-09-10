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
    socrata_data_createview_cursor.execute(
        'CREATE VIEW "USA_CITY_IDS_WITH_THEME_OR_KEYWORD" AS select distinct identifier,theme,keyword from (select identifier,theme,keyword from socrata_data_city_usa union select identifier,theme,keyword from socrata_dcat_city_usa) where theme!="" or keyword !="" order by theme,keyword')
except:
    print 'Create failed'
conn.commit()
  
print '--BD  updated!'
conn.close()
print '--BD  closed!'

