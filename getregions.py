import requests
import pandas as pd
import time

start = time.time()

url = 'https://api.builtin.com/regions'
data = requests.get(url).json()

ids = []
names = []
aliases = []
urls = []

for i in data:
    ids.append(i['id'])
    names.append(i['name'])
    aliases.append(i['alias'])
    urls.append(i['url'])

df = pd.DataFrame(
    {
        "id": ids,
        "name": names,
        "alias": aliases,
        "url": urls
    }
)

df.to_csv('data/region.csv',index=False) 

end = time.time()
print("Regions parsing time:",end - start)