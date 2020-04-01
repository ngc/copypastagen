import json
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from selenium.webdriver.chrome.options import Options
import os
from time import sleep

links = [] #stores links for each representation page
target = [] #stores name of targeted country
location = [] #stores name of targetted representation's location (country)
address = [] #stores email address for its respective row


#Make chromedriver headless
chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_dir = "/usr/lib/chromium-browser/chromedriver"

#Get embassy page (contains email element) and initialize webdriver with test link
driver = driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_dir)
driver.get("https://www.reddit.com/r/copypasta/top/?sort=top&t=week")


#iterate through different embassy links stored
#scrape each email from each link
set = False
for i in range(len(links)):

    country = ""
    content = driver.page_source
    soup = BeautifulSoup(content, 'lxml')

    for match in soup.findAll('h2', attrs={'class':'entry-title'}):
        country = match.text

    for nation in range(len(targetraw)):
        if(targetraw[nation] in country):
            country = targetraw[nation]

    for match in soup.findAll('li', attrs={'id':'email'}):
        print("Fetched email " + match.text[5:] + " " + str(i) + "/" + str(numberofLinks) + " " + str(i/numberofLinks * 100)[:5] + "% for " + country)
        address.append(match.text[5:]) #prevents substring 'Email' from being added to email address string
        target.append(country)
