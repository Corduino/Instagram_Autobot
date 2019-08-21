import urllib
import urllib.request
import re
from urllib.request import urlopen, Request
import os,time
#Loads up the desired site into the object "site", has all the information inside it
while true:
    site = urlopen(Request("https://www.reddit.com/r/memes/", headers={'User-Agent': 'Mozilla'}), data = None) #b'title style>'
    #site = urllib.request.urlopen("https://www.python.org", data = None)
    #Looks as the object "Site" and find the first instance of a header and image downloads then clips that part of the file off so that the next header and image can be found later
    i = 0
            #Search / Store first header     ##Error is that I think site isnt a regulat Pattern string so it cant be used ... Find a way to covert it from the url object to a strin
    global caption
    site_string = site.read(1000000) # posts are about 100 lines apart which is something in charecters idk
    site_string = site_string[385000:] # Change to pick starting post
    site_string = site_string.decode()
    site_string = site_string.replace("-"," ")
    #site_string = site_string[400000:] 
    #Repeat until done X amount of times
    while i < 20:
        #This is the Caption finder, it find the caption for the image and saves it in type string
        #print(site_string)
        found = site_string.find('<h3 class="_eYtD2XCVieq6emjKBH3m">')
        if found:
            #print(site_string)
            print("found it at ", found)
            site_string = site_string[found + 33:]
            #print(site_string)
            caption_end = site_string.find('</')
            caption = site_string[:caption_end]
            print(site_string)
            print(caption)
            f = open("caption.txt", "w")
            f.write(caption)
            f.close()
            time.sleep(2)
            #Search / Download first Picture
            site_string = site_string[100:]
        found = site_string.find('https://preview.redd.it/')
        if found:
            print("found it at ", found)
            site_string = site_string[found:]
           # print(site_string)
            photo_link_end = site_string.find('"')
            photo_link = site_string[:photo_link_end]
            photo_link = photo_link.replace(" ","-")
            photo_link = photo_link.replace("amp;",'')
            print(photo_link)
            urllib.request.urlretrieve(photo_link, "Meme.png")
            #Cut "site" to allow for next search
            site_string = site_string[photo_link_end:]
            #Run Auto-bot Photo Upload.py
        if i != 0:
            time.sleep(900)
        os.system("Python C:/Users/Cordin/Desktop/Instagram_Autobot-master/Auto_Bot__Photo_Upload.py")
        print("Run", i)
        i += 1
