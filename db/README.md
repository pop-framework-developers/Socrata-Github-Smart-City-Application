 This folder contains a SQLite database called OpenDataCatalog.sqlite with the next elements:
 
    - A table called socrata_customer with the next fields:
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
