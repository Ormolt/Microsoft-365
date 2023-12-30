import os
from random import randint
import time  # For adding delays

for i in range(1, 365):

    for j in range(0, randint(1, 10)):
        d = str(i) + ' days ago'
        with open('file.txt', 'a') as file:
            file.write(d)
        os.system('git add .')
        os.system(f'git commit --date="{d}" -m "Generated commit"')
        time.sleep(1)  # Optional delay to avoid duplicate timestamps
            
os.system('git push -u origin main')






