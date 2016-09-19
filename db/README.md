 This folder contains a SQLite database called OpenDataCatalog.sqlite (compressed in OpenDataCatalog.zip).
 This database is the result of carrying out in the correct order the different processes and executing the scripts of the Socrata Github Smart City Application.
 Thus, the database contains the next elements:
 
 - A table called socrata_customer, which stores data about the organizations using Socrata Open Data technology, with the next fields:
  -"id_customer" INTEGER PRIMARY KEY NOT NULL
  - "customer_name" TEXT
  - "type" TEXT
  - "location_name" TEXT DEFAULT (null) 
  - "country" TEXT
  - "open_data_site_url" TEXT,
  - "api_dcat_url" TEXT,
  - "api_data_url" TEXT,
  - "longitude" TEXT,
  - "latitude" TEXT
