This is a semi-automated process that must be carried out by experts.
Concretely, the experts have the table usa_city_datasets_categorized of the OpenDataCatalogs.sqlite database which consists of the identifier, theme, keyword, title and description of  the datasets of Usa cities that, at least, havea a theme or a keyword.
The table also has the category field, initially as null, which is the one that must be filled in by the experts according to the categories established for the specific application of the POP Framework. 
For this specific application to Smart Cities, the proposed categories are:
- Administration & Finance
- Business
- Demographics
- Education
- Ethics & Democracy
- Geospatial
- Health
- Recreation & Culture
- Safety
- Services
- Sustainability
- Transport & Infrastructure
- Urban Planning & Housing
- Welfare

As a result of this process, the datasets that can be categorized will include this category in the  usa_city_datasets_categorized table.

In this specific application, the experts had to categorize the 8960 datasets available of USA cities with theme or keywords.

Firstly, they studied the different 215 themes of the datasets and developed a script that categorizes every dataset in a category according to its theme. The script is called Semi_automated_categorization.py and is available in this folder. As a result, 8299 datasets were categorized to one of the categories, 650 datasets without theme still had category as NULL and  11 datasets were categorized as 'Others' because none of them had a clear category and so, they were discarded due to they were not useful to be used in the application.

At this point, the experts had to choose between discarding the 650 datasets without theme or trying to categorize them, one by one, using the keyword field together with the title and the description fields. In this case the experts chose the second option and the result of this 'one by one' categorization of the 650 datasets without theme can be see executing this query against the OpenDataCatalogs.sqlite database:
- select distinct identifier,category,keyword,title,description from  USA_CITY_DATASETS_CATEGORIZED  WHERE theme="" order by category,keyword,title,description

At the end ot this process, the table usa_city_datasets_categorized of the OpenDataCatalogs.sqlite contained the datasets of USA cities together with their category.
