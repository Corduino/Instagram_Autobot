from InstagramAPI import InstagramAPI as IgAPI
import os,time
#import Reddit-Scraper as RS

account_name = "corduino"
password = "passwordformemeaccount"

IgAPI = IgAPI(account_name, password)
f = open("caption.txt", "r")
caption = f.read()
f.close()
IgAPI.login()  # login


#Make this Able to change based on a fed in extended variable from A scraper
photo_path = 'C:/Users/Cordin/Desktop/Instagram_Autobot-master/Meme.png'
IgAPI.uploadPhoto(photo_path, caption=caption + "\n.\n.\n#meme #memes #funny #memesdaily #dankmemes #lol #funnymemes #dank #like #follow #humor #lmao #dankmeme #love #fortnite #anime #edgymemes #comedy #f #fun #instagram #dailymemes #offensivememes #edgy #ol #funnymeme #cringe #haha #minecraft #bhfyp")
print("Photo Uploaded")

time.sleep(1)
#logout
IgAPI.logout()



