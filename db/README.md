 This folder contains a SQLite database called OpenDataCatalog.sqlite (compressed in OpenDataCatalog.zip).
 This database is the result of carrying out in the correct order the different processes and executing the scripts of the Socrata Github Smart City Application.
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
 
 
