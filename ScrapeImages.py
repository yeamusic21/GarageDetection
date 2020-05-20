# Resources:
# https://gist.github.com/genekogan/ebd77196e4bf0705db51f86431099e57

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib2
import argparse
import urllib.request

searchterm = 'garage' # will also be the name of the folder
url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
# NEED TO DOWNLOAD CHROMEDRIVER, insert path to chromedriver inside parentheses in following line
browser = webdriver.Chrome('C:/Users/Matt/Downloads/chromedriver_win32/chromedriver.exe')
browser.get(url)
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
counter = 0
succounter = 0

if not os.path.exists(searchterm):
    os.mkdir(searchterm)

for _ in range(500):
    browser.execute_script("window.scrollBy(0,10000)")

for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
    counter = counter + 1
    print("Total Count:", counter)
    print("Succsessful Count:", succounter)
    print("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])

    img = json.loads(x.get_attribute('innerHTML'))["ou"]
    imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]

    try:
        path = 'C:/Users/Matt/Desktop/Personal/GarageDetection/GitHub/GarageDetection/GarageImages'
        urllib.request.urlretrieve(img, path)
        succounter += 1
    except Exception as e:
        print(e)

print succounter, "pictures succesfully downloaded"
browser.close()