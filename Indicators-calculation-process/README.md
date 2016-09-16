Import from result_search_open_data.csv to a table with the same name in the database using import tools of sqllite.

Import from measures_repository.csv to a table with the same name in the database using import tools of sqllite.


----------------------------------Primera 1 Es la versión reducida de rep_user_stats_with_food_and_others
create view repository_useful_data_for_indicators as select distinct repository_id,total_contributors,total_contributions,subscribers_count,created_at,updated_at from measures_repository where  created_at!="" order by repository_id;

----------------------------------Primera 1 

----------------------------------Segunda 2 Devuelve el identificador categorizado y los distintos repositorios que referencian al dataset
create view datasets_categorized_referenced_and_distinct_repository_id_referencing as select distinct c.identifier,c.category,d.repository_id from results_search_open_data as d  join usa_city_datasets_categorized as c on (d.identifier=c.identifier)  where repository_id in (select repository_id from repository_useful_data_for_indicators) order by c.category,c.identifier,d.repository_id

----------------------------------Segunda 2


create view useful_data_for_indicators as select distinct d.identifier,d.category,d.repository_id,total_contributors,total_contributions,subscribers_count,created_at,updated_at from dataset_category_repository as d left outer  join ( select * from measures_repository where  created_at!="" ) as r on (d.repository_id=r.repository_id)

create view useful_data_for_indicators as select distinct d.identifier,d.category,d.repository_id,total_contributors,total_contributions,subscribers_count,created_at,updated_at from dataset_category_repository as d left outer  join ( select * from measures_repository where  created_at!="" ) as r on (d.repository_id=r.repository_id)  order by d.category,d.identifier,d.repository_id;

create view repository_useful_data_for_indicators as select distinct repository_id,total_contributors,total_contributions,subscribers_count,created_at,updated_at from measures_repository where  created_at!="" order by repository_id;

create view dataset_category_repository_useful_data_for_indicators as select * from dataset_category_repository d left join repository_useful_data_for_indicators   as r on d.repository_id=r.repository_id where d.repository_id="" or d.repository_id in (select repository_id from  repository_useful_data_for_indicators where created_at is not null)