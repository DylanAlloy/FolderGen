import os
import time
print("Folder Creation Utility by Dylan Moore")
print("---------------------------------------")
time.sleep(1)
print("Make sure that you are running this inside the directory you wish to create multiple folders.")
print(" ")
x = input("How many folders?:")
i = x
for _ in range(x):
    newpath = r'./' + str(i)
    if not os.path.exists(newpath):
	   os.makedirs(newpath)
	   i -= 1
