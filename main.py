import subprocess
import time

start = time.time()
subprocess.run("python getjobsANDcompanies.py & python getindustries.py & python getjobsubcategories.py & python getregions.py", shell=True)

end = time.time()
print('Total parsing time:',end - start)