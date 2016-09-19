 This folder contains a SQLite database called OpenDataCatalog.sqlite (compressed in OpenDataCatalog.zip).
 This database is the result of carrying out, in the correct order, the different processes and executing the scripts of the Socrata Github Smart City Application.
 Thus, the database contains the next elements:
 
 - A table called socrata_customers, which stores data about the organizations using Socrata Open Data technology, with the next characteristics:
  - "id_customer" INTEGER PRIMARY KEY NOT NULL
  - "customer_name" TEXT
  - "type" TEXT
  - "location_name" TEXT DEFAULT (null) 
  - "country" TEXT
  - "open_data_site_url" TEXT,
  - "api_dcat_url" TEXT,
  - "api_data_url" TEXT,
  - "longitude" TEXT,
  - "latitude" TEXT

 - A table called socrata_data, which stores the info of every dataset contained in the data.json of socrata portals, with the next characteristics:
  - "identifier" TEXT NOT NULL
  - "api_url" TEXT
  - "landingPage" TEXT
  - "publisher" TEXT
  - "keyword" TEXT
  - "theme" TEXT 
  - "title" TEXT 
  - "issued" TEXT 
  - "modified" TEXT
  - "description" TEXT
  - "id_customer" INTEGER,
  - PRIMARY KEY (identifier,id_customer)
  - FOREIGN KEY(id_customer) REFERENCES "socrata_customers"(id_customer)
  
 - A table called socrata_dcat, which stores the info of every dataset contained in the dcat.json of socrata portals, with the next characteristics:
  - "identifier" TEXT NOT NULL
  - "webService" TEXT
  - "accessURL" TEXT
  - "feed" TEXT
  - "keyword" TEXT
  - "theme" TEXT
  - "title" TEXT
  - "created" TEXT
  - "releaseDate" TEXT
  - "modified" TEXT
  - "description" TEXT
  - "id_customer" INTEGER
  - PRIMARY KEY (identifier,id_customer)
  - FOREIGN KEY(id_customer) REFERENCES "socrata_customers"(id_customer)
  
 - A view called Socrata_DATA_CITY_USA, which shows useful information of every dataset contained in the data.json of socrata portals of USA cities, made with the next query:
  - select distinct identifier, keyword, theme, title,description from socrata_data where id_customer in (select id_customer from socrata_customers where type="City" and country="USA")
  
 - A view called Socrata_DCAT_CITY_USA, which shows useful information of every dataset contained in the dcat.json of socrata portals of USA cities, made with the next query:
  - select distinct identifier, keyword, theme, title,description from socrata_data where id_customer in (select id_customer from socrata_customers where type="City" and country="USA")
  
- A view called USA_CITY_IDS_WITH_THEME_OR_KEYWORD, which only shows identifier, theme and keyword of the USA cities datasets when, at least, a theme or a keyword exists because without one of them it may be too difficult to categorize the datasets. This view is the one used by the Github-ETL process for searching references to the datasets in Github. It is made with the next query:
  - select distinct identifier,theme,keyword from (select identifier,theme,keyword from socrata_data_city_usa union select identifier,theme,keyword from socrata_dcat_city_usa) where theme!="" or keyword !="" order by theme,keyword
 
- A table called usa_city_datasets_categorized, which stores the same rows as the USA_CITY_IDS_WITH_THEME_OR_KEYWORD but with 3 more columns: title, description and category. That is, those ones when, at least, a theme or keyword exist. This table is the one used by the experts for carrying out the categorization process of the datasets. So, initially, the field category is null for every row. It also contains the title and the description of every row for helping in those cases where experts might be doubting among one or more categories when a dataset does not contain a theme. In summary, this table has the next characteristics:
 - "IDENTIFIER" TEXT PRIMARY KEY  NOT NULL
 - "THEME" TEXT
 - "KEYWORD" TEXT
 - "TITLE" TEXT
 - "DESCRIPTION" TEXT
 - "CATEGORY" TEXT
 
- A table called results_search_open_data, which stores the info retrieved from Github with a row for every reference from a Github repository to a dataset of USA cities. In summary, this table has the next characteristics:
  - "identifier"TEXT
  - "theme"	TEXT
  - "keyword" TEXT
  - "file_name" TEXT
  - "file_path" TEXT
  - "file_url" TEXT
  - "repository_id" TEXT
  - "repository_name" TEXT
  - "repository_url" TEXT
  - "user_id" TEXT
  - "user_name" TEXT
  - "user_url" TEXT
  - "score" TEXT

- A table called measures_repository, which stores a row for every repository of Github which references datasets of USA cities with useful information about the repository. In summary, this table has the next characteristics:
  - "repository_id" TEXT
  - "user_id" TEXT
  - "stargazers_count" TEXT
  - "watchers_count" TEXT
  - "language" TEXT
  - "forks_count" TEXT
  - "subscribers_count" TEXT
  - "network_count" TEXT
  - "created_at" TEXT
  - "updated_at" TEXT
  - "pushed_at" TEXT
  - "total_contributors" TEXT
  - "total_contributions" TEXT

- A view called repository_useful_data_for_indicators, which only shows repository_id, total_contributors, total_contributions, subscribers_count, created_at, updated_at of the repositories in the measures_repository table when info about the creation date exists (created_at!=""). These fields are those ones used to calculate most of the indicators of this Application. It is made with the next query:
  - select distinct repository_id,total_contributors,total_contributions,subscribers_count,created_at,updated_at from measures_repository where  created_at!="" order by repository_id
  
- A view called datasets_categorized_referenced_and_distinct_repository_id_referencing, which only shows a row with  identifier, category and repository_id of every dataset of USA cities referenced by a repository of Github. Although a repository references several times a dataset, only appears 1 row in the view. It is made with the next query:
  - select distinct c.identifier,c.category,d.repository_id from results_search_open_data as d  join usa_city_datasets_categorized as c on (d.identifier=c.identifier) where repository_id in (select repository_id from repository_useful_data_for_indicators) order by c.category,c.identifier,d.repository_id
 
- A view called datasets_categorized_not_referenced, which only shows a row with  identifier, category and repository_id as NULL of every dataset of USA cities not referenced by a repository of Github. It is made with the next query:
  - select distinct identifier,category,NULL as repository_id from usa_city_datasets_categorized   where identifier not in (select identifier from datasets_categorized_referenced_and_distinct_repository_id_referencing) order by category,identifier

- A view called categories_total_references, which shows, for every category, the number of total references from Github to datasets of the category. It is made with the next query:
  - select category,count(*) as total_references from datasets_categorized_referenced_and_distinct_repository_id_referencing group by category order by category

- A view called categories_total_datasets_in, which shows, for every category, the number of datasets of the category, referenced or not in Github. It is made with the next query:
  - select category,count (distinct identifier) total_datasets_in_category from usa_city_datasets_categorized group by category order by category

- A view called categories_total_datasets_no_referenced, which shows, for every category, the number of datasets of the category not referenced in Github. It is made with the next query:
  - select category,count (distinct identifier) as total_datasets_no_referenced from datasets_categorized_not_referenced group by category order by category 

- A view called categories_total_datasets_referenced, which shows, for every category, the number of datasets of the category referenced in Github. It is made with the next query:
  - select category,count (distinct identifier) as total_datasets_referenced from datasets_categorized_referenced_and_distinct_repository_id_referencing group by category order by category

- A view called categories_total_repositories_referencing, which shows, for every category, the number of distinct repositories of Github referencing datasets of the category. It is made with the next query:
  - select category,count (distinct repository_id) as total_repositories_referencing from datasets_categorized_referenced_and_distinct_repository_id_referencing group by category order by category

- A view called categories_contributors, which shows, for every category, the sum of total_contributors of the distinct repositories referencing every category. It is made with the next query:
  - select category,sum(total_contributors) as contributors from (select distinct d.repository_id,r.total_contributors,d.category from repository_useful_data_for_indicators as r join datasets_categorized_referenced_and_distinct_repository_id_referencing as d on d.repository_id=r.repository_id order by d.repository_id,r.total_contributors,d.category) group by category order by category
  
- A view called categories_contributions, which shows, for every category, the sum of total_contributions of the distinct repositories referencing every category. It is made with the next query:
  - select category, sum(total_contributions) as contributions from (select distinct d.repository_id,r.total_contributions,d.category from repository_useful_data_for_indicators as r join datasets_categorized_referenced_and_distinct_repository_id_referencing as d on d.repository_id=r.repository_id order by d.repository_id,r.total_contributions,d.category) group by category order by category
  
- A view called categories_subscribers, which shows, for every category, the sum of  subscribers_count of the distinct repositories referencing every category. It is made with the next query:
  - select category, sum(subscribers_count) as subscribers from (select distinct d.repository_id,r.subscribers_count,d.category from repository_useful_data_for_indicators as r join datasets_categorized_referenced_and_distinct_repository_id_referencing as d on d.repository_id=r.repository_id order by d.repository_id,r.subscribers_count,d.category) group by category order by category

- A view called categories_madurity_total, which shows, for every category, the total maturity of the distinct repositories referencing every category. Maturity is computed using 2 lifetimes, project lifetime (PL) and last update lifetime (LUL) and the formula is: PL/LUL. Thus, maturity projects will be those ones with elderly PL ann a low LUL. It is made with the next query:
  - select category, round(sum( (strftime('%s','2015-11-24 19:19:39 ') - strftime('%s',created_at)) / ((strftime('%s','2015-11-24 19:19:39 ') - strftime('%s',updated_at))*1.0)),3) as madurity_total from (select distinct d.repository_id,r.created_at,r.updated_at,d.category from repository_useful_data_for_indicators as r join datasets_categorized_referenced_and_distinct_repository_id_referencing as d on d.repository_id=r.repository_id order by d.repository_id,r.created_at,r.updated_at,d.category) group by category order by category


