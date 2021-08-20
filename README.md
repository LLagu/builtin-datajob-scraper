# builtin-datajob-scraper
## Simple scraper for builtin.com's Data Science jobs

builtin-datajob-scraper returns five csv files:

1. jobs.csv: main table, contains the description of every scraped job. Contains the ids (FK) of the other tables (use LEFT JOIN)
2. company.csv
3. industry.csv
4. region.csv
5. subcategory.csv

The jupyter notebook found in the repository reads the data from a manually updated sqlite database (created using [DB Browser for SQLite](https://sqlitebrowser.org/) and last updated on 20/08/2021) but of course it's possible to read the csv files directly.

There are many fields that are not scraped from the websiteby default. To see and add the missing ones one must use the builin.com apis to check the fields, add it the to the main for loop and add a new column when creating the dataframe/csv file.

**Example**
Let's say we want to get the timezone name from the region table
```
import requests
import pandas as pd

url = 'https://api.builtin.com/regions'
data = requests.get(url).json()

#first region keys
print(data[0].keys())

# print result:
# dict_keys(['id', 'name', 'site_name', 'code', 'state', 'country', 'timezone_name', 'url', 'alias', 'facebook', 'linked_in', 'twitter', 'created_at', 'updated_at', 'locations'])

timezones_array = []
for i in data:
    timezones_array.append(i['timezone_name'])
    
df = pd.DataFrame(
    {
        "timezone": timezones_array
    }
)

df.to_csv('data/test.csv',index=False) 

```

**APIs links**
  - [jobs and companies (first 20 results,edit url parameters to see more)](https://api.builtin.com/services/job-retrieval/legacy-jobs?categories=147&subcategories=&experiences=&industry=&regions=&locations=&remote=2&per_page=20&page=1&search=&sortStrategy=recency&jobs_board=true&national=true)
  - [industries](https://api.builtin.com/company-types)
  - [subcategories](https://api.builtin.com/job-subcategories)
  - [regions](https://api.builtin.com/regions)
