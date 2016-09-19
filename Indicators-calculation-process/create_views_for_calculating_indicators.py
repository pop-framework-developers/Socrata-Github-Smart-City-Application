#script which creates different views used to calculare indicators
import bdUtils
import jsonUtils
import sqlite3
import re

#open db
conn=bdUtils.openDB()
conn.row_factory = sqlite3.Row

                       
try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'create view repository_useful_data_for_indicators as select distinct repository_id,total_contributors,total_contributions,subscribers_count,created_at,updated_at from measures_repository where  created_at!="" order by repository_id;')
except:
    print 'repository_useful_data_for_indicators failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'create view datasets_categorized_referenced_and_distinct_repository_id_referencing as select distinct c.identifier,c.category,d.repository_id from results_search_open_data as d  join usa_city_datasets_categorized as c on (d.identifier=c.identifier)  where repository_id in (select repository_id from repository_useful_data_for_indicators) order by c.category,c.identifier,d.repository_id')
except:
    print 'datasets_categorized_referenced_and_distinct_repository_id_referencing failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'create view datasets_categorized_not_referenced as select distinct identifier,category,NULL as repository_id from usa_city_datasets_categorized   where identifier not in (select identifier from datasets_categorized_referenced_and_distinct_repository_id_referencing) order by category,identifier')
except:
    print 'datasets_categorized_not_referenced failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'create view categories_total_references as select category,count (*) as total_references from datasets_categorized_referenced_and_distinct_repository_id_referencing group by category order by category')
except:
    print 'categories_total_references failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'create view categories_total_datasets_in as select category,count (distinct identifier) total_datasets_in_category from usa_city_datasets_categorized group by category order by category') 
except:
    print 'categories_total_datasets_in failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'create view categories_total_datasets_no_referenced as select category,count (distinct identifier) as total_datasets_no_referenced from datasets_categorized_not_referenced group by category order by category')
except:
    print 'categories_total_datasets_no_referenced failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'create view categories_total_datasets_referenced as select category,count (distinct identifier) as total_datasets_referenced from datasets_categorized_referenced_and_distinct_repository_id_referencing group by category order by category')
except:
    print 'categories_total_datasets_referenced failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'create view categories_total_repositories_referencing as select category,count (distinct repository_id) as total_repositories_referencing from datasets_categorized_referenced_and_distinct_repository_id_referencing group by category order by category')
except:
    print 'categories_total_repositories_referencing failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'create view categories_contributors as select category,sum(total_contributors) as contributors from (select distinct d.repository_id,r.total_contributors,d.category from repository_useful_data_for_indicators as r join datasets_categorized_referenced_and_distinct_repository_id_referencing as d on d.repository_id=r.repository_id order by d.repository_id,r.total_contributors,d.category) group by category order by category')
except:
    print 'categories_contributors failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'create view categories_contributions as select category, sum(total_contributions) as contributions from (select distinct d.repository_id,r.total_contributions,d.category from repository_useful_data_for_indicators as r join datasets_categorized_referenced_and_distinct_repository_id_referencing as d on d.repository_id=r.repository_id order by d.repository_id,r.total_contributions,d.category) group by category order by category')
except:
    print 'categories_contributions failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'create view categories_subscribers as select category, sum(subscribers_count) as subscribers from (select distinct d.repository_id,r.subscribers_count,d.category from repository_useful_data_for_indicators as r join datasets_categorized_referenced_and_distinct_repository_id_referencing as d on d.repository_id=r.repository_id order by d.repository_id,r.subscribers_count,d.category) group by category order by category')
except:
    print 'categories_subscribers failed'
conn.commit()

try:
    socrata_data_update_cursor=conn.cursor()    
    socrata_data_update_cursor.execute(
        'create view categories_madurity_total as select category, round(sum( (strftime('%s','2015-11-24 19:19:39 ')-strftime('%s',created_at))/((strftime('%s','2015-11-24 19:19:39 ')-strftime('%s',updated_at))*1.0)),3) as madurity_total from (select distinct d.repository_id,r.created_at,r.updated_at,d.category from repository_useful_data_for_indicators as r join datasets_categorized_referenced_and_distinct_repository_id_referencing as d on d.repository_id=r.repository_id order by d.repository_id,r.created_at,r.updated_at,d.category) group by category order by category')
except:
    print 'categories_madurity_total failed'
conn.commit()

  
print '--BD  updated!'
conn.close()
print '--BD  closed!'

