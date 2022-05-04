import os
import stat
import time 


MAX_CHAR_LENGTH = 512
MIN_CHAR_LENGTH = 150
NEWLINE_CHAR = "<N>"

d = "repos"
full_paths = []
for dirpath, dirnames, filenames in os.walk(d):
    for f in filenames:
        full_path = os.path.join(dirpath,f)
        full_paths.append(full_path)
print(len(full_paths))         # 1589


with open("python_data.txt","a",encoding='utf-8') as file:
    for fpath in full_paths:
        try:
            data  = open(fpath,"r",encoding='utf-8').read() 
            # to remove this (UnicodeDecodeError: 'charmap' codec) error we have use encoding='mbcs'
            fd = data.replace("\n",NEWLINE_CHAR)
            if 100 < len(data) <= MAX_CHAR_LENGTH:
                file.write(fd+"\n")
            else :
                sd = fd.split(f"{NEWLINE_CHAR}{NEWLINE_CHAR}")
                substring = ""
                for split in sd:
                    substring += split+f"{NEWLINE_CHAR}{NEWLINE_CHAR}"
                    if MIN_CHAR_LENGTH < len(substring) <= MAX_CHAR_LENGTH:
                        file.write(substring+"\n")
                        substring = ""  
        except Exception as e:
            print(str(e))                

