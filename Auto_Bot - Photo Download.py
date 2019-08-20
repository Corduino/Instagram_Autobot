import urllib
import urllib.request
import re
#Loads up the desired site into the object "site", has all the information inside it
#"https://www.reddit.com/r/greentext/
site = urllib.request.urlopen("https://www.python.org", data = None)
#Looks as the object "Site" and find the first instance of a header and image downloads then clips that part of the file off so that the next header and image can be found later
    #Repeat until done X amount of times
i = 0
while i < 3:
        #Search / Store first header     ##Error is that I think site isnt a regulat Pattern string so it cant be used ... Find a way to covert it from the url object to a string
    site_pattern = re.compile(site)
    header_Start = site_pattern.search("title style>")
    print(header_Start)
    
        #Search / Download first Picture
    #Picture_Start = re.search();
        #Cut "site" to allow for next search

        #Run Auto-bot Photo Upload.py
    
    print("Run", i)
    i += 1
