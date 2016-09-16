#script which create a view called socrata_data_city_usalooks for data.json at socrata portals and store the info of every dataset in socrata_data table
import bdUtils
import jsonUtils
import sqlite3
import re

#open db
conn=bdUtils.openDB()
conn.row_factory = sqlite3.Row

                          
try:
    socrata_data_createtable_cursor=conn.cursor()
    socrata_data_createtable_cursor.execute(
        'CREATE TABLE if not exists "usa_city_datasets_categorized" ("IDENTIFIER" TEXT PRIMARY KEY  NOT NULL , "THEME" TEXT, "KEYWORD" TEXT,"TITLE" TEXT, "DESCRIPTION" TEXT,"CATEGORY" TEXT)')
except:
    print 'Create failed'
try:    
    socrata_data_insert_cursor=conn.cursor()
    socrata_data_insert_cursor.execute(
        'INSERT INTO "usa_city_datasets_categorized" (IDENTIFIER,THEME,KEYWORD,TITLE,DESCRIPTION) select distinct identifier,theme,keyword,title,description from (select identifier,theme,keyword,title,description from socrata_data_city_usa where description!="not_available" or (description="not_available" and identifier not in (select identifier from socrata_dcat_city_usa)) union select  identifier,theme,keyword,title,description from socrata_dcat_city_usa where description!="not_available" or (description="not_available" and identifier not in (select  identifier from socrata_data_city_usa) )) where theme!="" or keyword !="" order by theme,keyword')
except:
    print 'Insert failed'
try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'UPDATE "USA_CITY_DATASETS_CATEGORIZED" SET Theme = LTRIM(RTRIM(Theme))')
except:
    print 'Update Ltrim and Rtrim failed'
conn.commit()

  
print '--BD  updated!'
conn.close()
print '--BD  closed!'

