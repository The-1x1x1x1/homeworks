import os
shut=input("do you wish to shut down? (y/n): ")

if shut=="n":
    exit()
else:
    os.system("shutdown /s /t 3")