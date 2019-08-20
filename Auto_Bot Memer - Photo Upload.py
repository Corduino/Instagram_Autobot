from InstagramAPI import InstagramAPI as IgAPI
#import Reddit-Scraper as RS

account_name = "autobot_memer"
password = "passwordformemeaccount"

IgAPI = IgAPI(account_name, password)
IgAPI.login()  # login


#Make this Able to change based on a fed in extended variable from A scraper
photo_path = 'E:\Personal\Auto-Memepage\Photo Data\BM.JPG'
caption = "Sample photo"
IgAPI.uploadPhoto(photo_path, caption=caption)
print("Photo Uploaded")


#logout
IgAPI.logout()



