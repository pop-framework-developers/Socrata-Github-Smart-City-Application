(By default, these scripts accesses to a SQLite database called OpenDataCatalogs.sqlite located in the project folder /db, the     details of the estructure of this db are available in the README of its folder)

It is neccesary to do the next steps:

- Execute socrata_customers.py in ordet to get the institutions that use Open Data Socrata Portals.
    - This script uses bdUtils, jsonUtils and urlUtils scripts
    - The script stores the information in the socrata_customers table of the OpenDataCatalogs.sqlite database
- Socrata open data portals may have 2 different json which all the information about the datasets of the portal: dcat.json and     data.json and, in many cases, they don't contain the same information. So, it is necessary to execute 2 different scripts:
    - socrata_dcat.py stores the info contained in dcat.json files about all datasets of every Socrata Open Data Portal in the socrata_dcat table of the OpenDataCatalogs.sqlite database  
    - socrata_data.py stores the info contained in data.json files about all datasets of every Socrata Open Data Portal in the socrata_data table of the OpenDataCatalogs.sqlite database 
    
