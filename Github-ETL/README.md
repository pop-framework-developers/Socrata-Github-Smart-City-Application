This folder contains the processes that aim to get required data from Github. These processes have been developed by using Pentaho Data Integration (http://community.pentaho.com/projects/data-integration/). There are two processes:

1. get_opendata_github_data.ktr. This process gets URLs from files in Github that refers to a unique open-dataset identifier of Socrata. The following parameters are required: Github connection data (parameters client_id, client_secret, token, and user), as well as path and file name of the SQLite database where the Socrata identifiers are stored (parameter sqlite_file).	This process	
uses the identifier stored in the  USA_CITY_IDS_WITH_THEME_OR_KEYWORD view (from SQLite database) to look for references in Github code, the result of this search is the results_search_open_data.csv (compressed in a ZIP file). This file has the following fields:
identifier: of the Socrata dataset
theme: topic of the dataset
keyword: keywords related to the dataset
file_name: name of the file that contains a reference to the dataset with the identifier.
file_path: path of the file that contains a reference to the dataset with the identifier.
file_url: full URL of the file that contains a reference to the dataset with the identifier.
repository_id: id of the repository that contains a file that refers to the dataset with the identifier.	
repository_name: name of the repository that contains a file that refers to the dataset with the identifier.	
repository_url: URL of the repository that contains a file that refers to the dataset with the identifier.
user_id: id of the user that owns the repository that contains a file that refers to the dataset with the identifier.	
user_name: name of the user that owns the repository that contains a file that refers to the dataset with the identifier. 
user_url: URL of the user that owns the repository that contains a file that refers to the dataset with the identifier. 	
score: given by Github to the search (the higher, the better). 	


-get_opendata_github_repositories_and_users.ktr.  the data gathered about the repositories referencing dataset of USA cities is stored in measures_repository.csv....
