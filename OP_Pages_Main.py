# %%
# Importing Libraries
# Webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait as wait

# URL data
from bs4 import BeautifulSoup
import re

# Waiting Time
from time import sleep

# %%
# Importing Functions
from OP_Pages_AdWall import adwall

# Importing Variables
from OP_Pages_Profile_Chrome import chrome_options

# %%
# Variables
# Path to (my) folder
saving_path = "C:/Users/nicol/Documents/Animes Mangás HQs/One Piece/"
saving_folder = "1101 - 1200"

# URL
urlbase = "https://mangareader.to/read/one-piece-3/en/chapter-"
chapter = "1103"
url = urlbase + chapter

# HTML important content
ad_wall_finder = "z-index: 2147483647"
privacy_iframe_id = '/html/body/iframe[1]'
reject_all_xpath = '/html/body/div[4]/div/div[2]/div/div[4]/div[2]/div[2]/span/div/span'
vertical_xpath = '//*[@id="first-read"]/div[1]/div/div[3]/a[1]'
vertical_images_xpath = '//*[@id="vertical-content"]'
img_div_class = 'iv-card loaded'

# %%
# Webdriver

# Instancing Webdriver
driver = webdriver.Chrome(chrome_options)

# Starting page
driver.get(url)

# Current tab
current_tab = driver.current_window_handle

# %%
# Dealing with Advertising
adwall(driver, ad_wall_finder, current_tab)


# %%
# Reject All Cookies
reject_all_btn = driver.find_element(By.XPATH, reject_all_xpath)
reject_all_btn.click()

# %%
# Setting Images to Vertical
driver.find_element(By.XPATH, vertical_xpath).click()

# %%
# Scroll to the end of the page
driver.find_element(By.TAG_NAME, "html").send_keys(Keys.END)
sleep(2)
driver.find_element(By.TAG_NAME, "html").send_keys(Keys.END)
sleep(2)
driver.find_element(By.TAG_NAME, "html").send_keys(Keys.END)

# %%
full_url = driver.page_source
driver.quit()

# %%
soup = BeautifulSoup(full_url, "html.parser")
img_links = soup.find_all("img", {"class": re.compile("image-vertical")})

# %%
for i in range(0, len(img_links)):
    img_links[i] = str(img_links[i]).split('src="')[1][:-4].replace('amp;', '')
img_links

# %%
#
for i in
