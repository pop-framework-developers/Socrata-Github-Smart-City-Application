This is a semi-automated process that must be carried out by experts.
Concretely, the experts have the table usa_city_datasets_categorized of the OpenDataCatalogs.sqlite database which consists of the identifier, theme, keyword, title and description of  the datasets of Usa cities that, at least, havea a theme or a keyword.
The table also has the category field, initially as null, which is the one that must be filled in by the experts according to the categories established for the specific application of the POP Framework. 
For this specific application to Smart Cities, the proposed categories and example datasets of every one are:

- Administration & Finance
  - Audits and Reports,City Finance and Budget, City Government, Fees, Liabilities and Assets, Purchasing, Revenue
- Business
  - City Businesses,Community & Economic Development,Growing Economy,Regulated Industries
- Demographics
  - Census,CitiStat,Forecasts,Neighborhoods,Statistics
- Education
  - Schools, Youth
- Ethics & Democracy
  - City Management and Ethics,Elections,Ethics,Expenditures,General Information,Governance,Government,Human Relations,Human Resources,Legislation,People,Permitting,Public Works,Taxes
- Geospatial
  - Geographic Locations and Boundaries, Mapping, Location, GIS
- Health
  - Public Health,Human Services,Social Services
- Recreation & Culture
  - Arts and Culture,Events,Greenways,Historic Preservation,Library,Parks,Recreation,Tourism
- Safety
  - Crime,Emergency,Fire,Police,Public Safety
- Services
  - 311 Call Center,City Services,Community,Customer Service,Facilities,Government Buildings and Structures,Inspectional Services,Public Property,Public Services,Service Requests
- Sustainability
  - Energy and Environment,Natural Resources,Sustainability,Waste Management,Food,Agriculture
- Transport & Infrastructure
  - Airports,City Infrastructure,Transportation,Parking,Streetcar,Traffic
- Urban Planning & Housing
  - Area Plans,Buildings,City Facilities,City Parks and Tree Data,Construction,Development,Housing,Land Use,Urban Planning
- Welfare
  - Insurance, Life Enrichment, Quality of Life,Pension,Retirement,Sanitation,Social Services

As a result of this process, the datasets that can be categorized will include this category in the  usa_city_datasets_categorized table.

In this specific application, the experts had to categorize the 8960 datasets available of USA cities with theme or keywords.

Firstly, they studied the different 215 themes of the datasets and developed a script that categorizes every dataset in a category according to its theme. The script is called Semi_automated_categorization.py and is available in this folder. As a result, 8299 datasets were categorized to one of the categories, 650 datasets without theme still had category as NULL and  11 datasets were categorized as 'Others' because none of them had a clear category. The dataset in the category 'Others' must be ignored after when the calculations of the indicators have been made.

At this point, the experts had to choose between discarding the 650 datasets without theme or trying to categorize them, one by one, using the keyword field together with the title and the description fields. In this case the experts chose the second option and the result of this 'one by one' categorization of the 650 datasets without theme can be see executing this query against the OpenDataCatalogs.sqlite database:
- select distinct identifier,category,keyword,title,description from  USA_CITY_DATASETS_CATEGORIZED  WHERE theme="" order by category,keyword,title,description

At the end ot this process, the table usa_city_datasets_categorized of the OpenDataCatalogs.sqlite contained the datasets of USA cities together with their category.
