import requests
import pandas as pd
import time

start = time.time()

url = 'https://api.builtin.com/job-subcategories'
data = requests.get(url).json()

ids = []
names = []
for container in data.keys():
    container_data = data[container]
    for i in container_data:
        ids.append(i['id'])
        names.append(i['name'])
        
    #names.append(data[container])
 
   
df = pd.DataFrame(
    {
        'id': ids,
        'name': names
    }
)
  
df.to_csv('data/subcategory.csv',index=False)      

end = time.time()
print("Subcategories parsing time:",end - start)
