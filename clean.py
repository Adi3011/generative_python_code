import os
import stat
import time 
from tqdm import tqdm

d = "repos"
for dirpath, dirnames, filenames in tqdm(os.walk(d)):
    for f in filenames:
        full_path = os.path.join(dirpath,f)
        print(dirpath)
        print(f)
 
        if full_path.endswith(".py"):
            print(f"keeping {full_path}")
        else:
            print(f"deleting {full_path}")
            if os.path.exists(full_path) and d in full_path :
                os.chmod(full_path,stat.S_IWRITE) #to delete read-only and binary files too.
                os.remove(full_path) 
            else:
                print("something is wrong buddy!")
                time.sleep(60)  
        if len(os.listdir(dirpath)) == 0:  # if the directory gets empty then delete it too
            os.rmdir(dirpath)


    time.sleep(0.5)     
    