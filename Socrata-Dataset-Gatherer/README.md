(By default, these scripts accesses to a SQLite database called OpenDataCatalogs.sqlite located in the project folder /db, the     details of the estructure of this db are available in the README of its folder)

It is neccesary to do the next steps:

- Execute socrata_customers.py in ordet to get the institutions that use Open Data Socrata Portals. To do this, Socrata has available http://goo.gl/qTTxfP a dataset containing the main data about its open data customers, including their open data portals URL and the type of institution.
    - This script uses bdUtils, jsonUtils and urlUtils scripts
    - The script stores the information in the socrata_customers table of the OpenDataCatalogs.sqlite database
- Socrata open data portals may have 2 different json which all the information about the datasets of the portal: dcat.json and     data.json and, in many cases, they don't contain the same information. So, it is necessary to execute 2 different scripts:
    - socrata_dcat.py stores the info contained in dcat.json files about all datasets of every Socrata Open Data Portal in the socrata_dcat table of the OpenDataCatalogs.sqlite database  
    - socrata_data.py stores the info contained in data.json files about all datasets of every Socrata Open Data Portal in the socrata_data table of the OpenDataCatalogs.sqlite database 
- Create 2 views that only contain the data in dcat.json and data.json of USA cities. So, it is necessary to execute 2 different scripts:      
    - create_view_socrata_data_city_usa.py creates the view Socrata_DATA_CITY_USA of the OpenDataCatalogs.sqlite database  
    - create_view_socrata_dcat_city_usa.py creates the view Socrata_DCAT_CITY_USA of the OpenDataCatalogs.sqlite database
- Execute create_view_usa_city_ids_with_theme_or_keyword.py creates the view USA_CITY_IDS_WITH_THEME_OR_KEYWORD  of the OpenDataCatalogs.sqlite database. This script creates a view that only contains identifier, theme and keyword of the USA cities datasets when, at least, a theme or a keyword exists because without one of them it may be too difficult to categorize the datasets. This view is the one used by the Github-ETL process for searching references to the datasets in Github.
- Execute create_table_usa_city_datasets_categorized.py which creates the table view usa_city_datasets_categorized of the OpenDataCatalogs.sqlite database.  This table is made up of identifier, theme, keyword, title, description and category and  contains the same rows as the USA_CITY_IDS_WITH_THEME_OR_KEYWORD view. That is, those ones when, at least, a theme or keyword exist. This table is the one used by the experts for carrying out the categorization process of the datasets. So, initially, the field category is null for every row. It also contains the title and the description of every row for helping in those cases where experts might be doubting among one or more categories when a dataset does not contain a theme.
