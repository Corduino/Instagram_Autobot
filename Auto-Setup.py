import os
import time

os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
time.sleep(2)
os.system("python F:\Personal\Auto-Memepage\Program and Packages\get-pip.py")
time.sleep(2)
os.system("pip install InstagramAPI")
#Chaning the Reddit fetch master or Praw to useing urllib python
os.system("pip install -r Instagram-API-python/requirements.txt")
#os.system("pip install -r reddit-fetch-master/requirements.txt")
#os.system("python reddit-fetch-master\grab_pictures.py -s funny -n 10 -t day")
time.sleep(100)
