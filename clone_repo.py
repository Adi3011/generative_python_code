from github import Github
ACCESS_TOKEN = open("token.txt","r").read()
g=Github(ACCESS_TOKEN)
print(g.get_user())


import time 
import os
from datetime import datetime

end_time = time.time()
start_time = end_time - 86400

for i in range(3):
    try:  
        start_time_str = datetime.utcfromtimestamp(start_time).strftime('%Y-%m-%d')
        end_time_str = datetime.utcfromtimestamp(end_time).strftime('%Y-%m-%d')
        query = f"language:python created:{start_time_str}..{end_time_str}"
        print(query)
        end_time -= 86400
        start_time -= 86400

        result = g.search_repositories(query)
        print(result.totalCount)
        for repository in result:
            print(f"{repository.clone_url}")
            print(f"{repository.owner.login}")
            os.system(f"git clone {repository.clone_url} repos/{repository.owner.login}/{repository.name}" )
            print(f"current start time {start_time}")
    except Exception as e:
        print(str(e))
        print("Broke for some reason...")
        time.sleep(120)
print("finished, your new end time should be", start_time)
# print(datetime.utcfromtimestamp(start_time).strftime('%Y-%m-%d'))
# print(datetime.utcfromtimestamp(end_time).strftime('%Y-%m-%d'))