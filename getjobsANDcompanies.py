import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

start = time.time()

#first API request to get total number of jobs
url = "https://api.builtin.com/services/job-retrieval/legacy-jobs/?categories=147&subcategories=&experiences=&industry=&regions=&locations=&remote=2&per_page=20&page=1&search=&sortStrategy=recency&jobs_board=true&national=false"
tmp_data = requests.get(url).json()
job_all_count = tmp_data['job_all_count']
#get all jobs with a single API request (format base url's &per_page parameter with the total jobs available)
complete_url = "https://api.builtin.com/services/job-retrieval/legacy-jobs/?categories=147&subcategories=&experiences=&industry=&regions=&locations=&remote=2&per_page={}&page=1&search=&sortStrategy=recency&jobs_board=true&national=false".format(job_all_count)
data = requests.get(complete_url).json()
#print("TOT: ",job_all_count, "\nPARSED: ", len(data['jobs']))

#support arrays
job_titles=[]
companies = []
job_description = []
levels = []
dates = []
locations = []
technologies = []
subcategories = []
subcategories1 = []
subcategories2 = []
subcategories3 = []
industries = []
industries1 = []
industries2 = []
industries3 = []

for job in data['jobs']:
    job_titles.append(job['title'])
    companies.append(job['company_id'])
    job_description.append(job['body'])
    levels.append(job['experience_level'])
    try:
        dates.append(job['sort_job'])    
    except:
        dates.append('')
    locations.append(job['location'])
    try:
        subcategories.append(str(job['sub_category_id']).translate({ord(i): None for i in '[]'}))   
    except:
        subcategories.append('')
    try:
        subcategories1.append(str(job['sub_category_id'][0]).translate({ord(i): None for i in '[]'}))   
    except:
        subcategories1.append('')
    try:
        subcategories2.append(str(job['sub_category_id'][1]).translate({ord(i): None for i in '[]'}))   
    except:
        subcategories2.append('')
    try:
        subcategories3.append(str(job['sub_category_id'][2]).translate({ord(i): None for i in '[]'}))   
    except:
        subcategories3.append('')
    industries.append(str(job['industry_id']).translate({ord(i): None for i in '[]'}))
    try:
        industries1.append(str(job['industry_id'][0]).translate({ord(i): None for i in '[]'}))   
    except:
        industries1.append('')
    try:
        industries2.append(str(job['industry_id'][1]).translate({ord(i): None for i in '[]'}))   
    except:
        industries2.append('')
    try:
        industries3.append(str(job['industry_id'][2]).translate({ord(i): None for i in '[]'}))   
    except:
        industries3.append('')
    
    '''link = job['alias']
    print(link)
    pageurl = 'https://builtin.com{}'.format(link)
    print(pageurl)
    data2 = requests.get(url)
    pagecontent = data2.content
    soup=BeautifulSoup(pagecontent,features="html.parser")
    tech = []
    for t in soup.findAll('span',attrs={'class': 'full-stack-item'}):
        tech.append(t.text) 
    technologies.append(tech)'''

'''print(
    len(job_titles),
    len(companies),
    len(companies),
    len(job_description),
    len(levels),
    len(dates),
    len(locations)
)'''

#create and export the dataframe
df = pd.DataFrame({'position': job_titles,

                   'company': companies,

                   'description': job_description,
                   
                   'level': levels,
                   
                   'date': dates,
                   
                   'location': locations,
                   
                   'subcategory_array': subcategories,
                   
                   'subcategory_1': subcategories1,
                   
                   'subcategory_2': subcategories2,
                   
                   'industry_array': industries,
                   
                   'industry1': industries1,
                   
                   'industry2': industries2,
                   
                   'industry3': industries3
                   
                   #'Tech': technologies
                   
                   
                   })

df.to_csv('data/jobs.csv',index=False)

#get companies

distinct_companies = set(companies)
#distinct_companies = str(companies).translate({ord(i): None for i in '[]'})
distinct_companies = list(distinct_companies)
n = 1000
c_args = [distinct_companies[i:i + n] for i in range(0, len(distinct_companies), n)]

c_ids = []
c_regions = []
c_titles = []

for elem in c_args:
    ids = str(elem).translate({ord(i): None for i in '[]'})
    url = 'https://api.builtin.com/companies/frontend/company-details?company_ids={}'.format(elem)
    data = requests.get(url).json()
    for i in data:
        c_ids.append(i['id'])
        c_regions.append(i['region_id'])
        c_titles.append(i['title'])


dfc = pd.DataFrame(
    {
        'id': c_ids,
        'region': c_regions,
        'name': c_titles
    }
)

dfc.to_csv('data/company.csv',index=False)

end = time.time()
print("Jobs and companies parsing time:",end - start)



