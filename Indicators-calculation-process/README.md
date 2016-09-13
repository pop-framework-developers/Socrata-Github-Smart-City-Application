Import from result_search_open_data.csv to a table with the same name in the database using import tools of sqllite.

Import from measures_repository.csv to a table with the same name in the database using import tools of sqllite.


create view dataset_category_repository as select distinct d.identifier,c.category,d.repository_id from dataset_references_full_list as d  join usa_city_datasets_categorized as c on (d.identifier=c.identifier) order by c.category

create view useful_data_for_indicators as select distinct d.identifier,d.category,d.repository_id,total_contributors,total_contributions,subscribers_count,created_at,updated_at from dataset_category_repository as d left outer  join ( select * from measures_repository where  created_at!="" ) as r on (d.repository_id=r.repository_id)

create view useful_data_for_indicators as select distinct d.identifier,d.category,d.repository_id,total_contributors,total_contributions,subscribers_count,created_at,updated_at from dataset_category_repository as d left outer  join ( select * from measures_repository where  created_at!="" ) as r on (d.repository_id=r.repository_id)  order by d.category,d.identifier,d.repository_id;

create view repository_useful_data_for_indicators as select distinct repository_id,total_contributors,total_contributions,subscribers_count,created_at,updated_at from measures_repository where  created_at!="" order by repository_id;

create view dataset_category_repository_useful_data_for_indicators as select * from dataset_category_repository d left join repository_useful_data_for_indicators   as r on d.repository_id=r.repository_id where d.repository_id="" or d.repository_id in (select repository_id from  repository_useful_data_for_indicators where created_at is not null)
