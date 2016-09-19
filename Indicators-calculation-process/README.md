Execute the script create_views_for_calculating_indicators.py for creating useful views to calculate the indicators used by the AHP component of the Application. Concretely this script creates the following views:

- A view called repository_useful_data_for_indicators, which only shows repository_id, total_contributors, total_contributions, subscribers_count, created_at, updated_at of the repositories in the measures_repository table when info about the creation date exists (created_at!=""). These fields are those ones used to calculate most of the indicators of this Application. 
- A view called datasets_categorized_referenced_and_distinct_repository_id_referencing, which only shows a row with identifier, category and repository_id of every dataset of USA cities referenced by a repository of Github. Although a repository references several times a dataset, only appears 1 row in the view. 
- A view called datasets_categorized_not_referenced, which only shows a row with identifier, category and repository_id as NULL of every dataset of USA cities not referenced by a repository of Github.

---

- A view called categories_total_references, which shows, for every category, the number of total references from Github to datasets of the category.
- A view called categories_total_datasets_in, which shows, for every category, the number of datasets of the category, referenced or not in Github. 
- A view called categories_total_datasets_no_referenced, which shows, for every category, the number of datasets of the category not referenced in Github. 
- A view called categories_total_datasets_referenced, which shows, for every category, the number of datasets of the category referenced in Github. 
- A view called categories_total_repositories_referencing, which shows, for every category, the number of distinct repositories of Github referencing datasets of the category. 

---

- A view called categories_contributors, which shows, for every category, the sum of total_contributors of the distinct repositories referencing every category. 
- A view called categories_contributions, which shows, for every category, the sum of total_contributions of the distinct repositories referencing every category. 
- A view called categories_subscribers, which shows, for every category, the sum of subscribers_count of the distinct repositories referencing every category.
- A view called categories_madurity_total, which shows, for every category, the total maturity of the distinct repositories referencing every category. Maturity is computed using 2 lifetimes, project lifetime (PL) and last update lifetime (LUL) and the formula is: PL/LUL. Thus, maturity projects will be those ones with elderly PL ann a low LUL. 
