import os

curdir=os.getcwd()  # cwd stand for (current working directory)
print(curdir)

os.mkdir("newDIr")   # for makeing directory

import time
time.sleep(2)
os.rename("newDIr", "fuckyoiu")
time.sleep(2)
os.rmdir("fuckyoiu")   # for removeing directory
 
