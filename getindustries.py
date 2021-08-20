import requests
import pandas as pd
import time

start = time.time()

url = 'https://api.builtin.com/company-types'
data = requests.get(url).json()

ids = []
names = []
aliases = []
urls = []

for i in data:
    ids.append(i['id'])
    names.append(i['name'])
    aliases.append(i['alias'])
    
df = pd.DataFrame(
    {
        "id": ids,
        "name": names,
        "alias": aliases
    }
)   

df.to_csv('data/industry.csv',index=False) 

end = time.time()
print("Industries parsing time:",end - start)