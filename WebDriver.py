# %%
# Importing Libraries
# Webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

from time import sleep

from bs4 import BeautifulSoup
import re

# %%
# Importing Functions
from WebDriver_AdWall import adwall

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
# Private Browsing Profile
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('prefs', {'profile.default_content_setting_values.cookies': 2})
chrome_options.add_experimental_option('prefs', {"profile.block_third_party_cookies": True})
chrome_options.add_experimental_option("useAutomationExtension", False)

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

# %%
full_url = driver.page_source

# %%
soup = BeautifulSoup(full_url, "html.parser")
tags_div = soup.find_all("div", {"class": re.compile(img_div_class)})
print(tags_div)

# %%
"""# Checking for the Privacy iframe
# try:
    # Checking of the iframe of the Privacy Tab
    # wait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, privacy_iframe_id)))

    # Finding the Reject All button and clicking it
    # reject_cookies = driver.find_element(By.XPATH, reject_all_cookies_xpath)
    # reject_cookies.click()

# finally:
print("2")

# Second AdWall
# adwall(ad_wall_finder)
print("3")

# Vertical
# driver.find_element(By.XPATH, vertical_xpath).click()
print("4")

# Third AdWall
# adwall(ad_wall_finder)

# close_all_tabs()
print("5")

# Storing the page html
# url_content = driver.page_source
# driver.quit()
# print(url_content)

# soup = BeautifulSoup(page, "html.parser")
# tags_div = soup.find_all("div", {"class": re.compile(r"iv-card loaded")})
# print(tags_div)
sleep(1000)"""
