
It is neccesary to do the next steps:
- Create or reuse a SQLite database called OpenDataCatalogs.sqlite located in the project folder /db
    (The details of the estructure of this db are available in the README of its folder)
- Execute socrata_customer.py in ordet to get the institutions that use Open Data Socrata Portals. 
    (This script uses bdUtils, jsonUtils and urlUtils scripts)
    (By default, the script accessed to a SQLite database called OpenDataCatalogs.sqlite located in the project folder /db with a table called socrata_customer with the next fields:
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
    
