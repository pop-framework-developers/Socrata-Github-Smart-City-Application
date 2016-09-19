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
  
  A table called socrata_dcat, which stores the info of every dataset contained in the dcat.json of socrata portals, with the next characteristics:
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
  
  A view called Socrata_DATA_CITY_USA, which shows useful information of every dataset contained in the data.json of socrata portals of USA cities, made with the next query:
  - select distinct identifier, keyword, theme, title,description from socrata_data where id_customer in (select id_customer from socrata_customers where type="City" and country="USA")
  
  A view called Socrata_DCAT_CITY_USA, which shows useful information of every dataset contained in the dcat.json of socrata portals of USA cities, made with the next query:
  - select distinct identifier, keyword, theme, title,description from socrata_data where id_customer in (select id_customer from socrata_customers where type="City" and country="USA")
  
