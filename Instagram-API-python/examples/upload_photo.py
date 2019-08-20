#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
#import Reddit-Scraper as RS

InstagramAPI = InstagramAPI("autobot_memer", "passwordformemeaccount")
InstagramAPI.login()  # login

photo_path = 'E:\Personal\Auto-Memepage\Data\BM.JPG'
caption = "Sample photo"
InstagramAPI.uploadPhoto(photo_path, caption=caption)
print("Photo Uploaded")
