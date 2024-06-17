from bs4 import BeautifulSoup

from selenium import webdriver

import requests
import re

urlbase = "https://mangareader.to/read/one-piece-3/en/chapter-"
chapter = "1103"
url = urlbase + chapter

# XPaths
vertical_xpath = '/html/body/div[1]/div[4]/div/div[1]/div/div[3]/a[1]'

# Instancing Webdriver
driver = webdriver.Chrome()

print(url)
req = requests.get(url, headers={"User-Agent": "Chrome"})

page = req.text
print(page)
soup = BeautifulSoup(page, "html.parser")

tags_div = soup.find_all("div", {"class": re.compile(r"iv-card loaded")})

print(tags_div)
