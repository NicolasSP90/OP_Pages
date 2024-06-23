# %%
# Importing Libraries
# Webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Waiting Time
from time import sleep

# %%
# Importing Functions
from OP_Pages_AdWall import adwall

from OP_Pages_Download_IMG import download_img

from OP_Pages_Folder import folder_chapter

from OP_Pages_URL_List import list_img_url

# from OP_Pages_Path_Handle import chapter_list

# Importing Driver Profile
from OP_Pages_Profile_Chrome import chrome_options

# %%
# Variables

# Path to (my) folder
chapter = "1098"
folder_path = "C:/Users/nicol/Documents/Animes Mangás HQs/One Piece/1101 - 1200/"

# Replace When Ready:
# Path to .exe folder
# folder_path, chapters_downloaded = chapter_list()
# chapter = str(int(max(chapters_downloaded))+1)

chapter_folder_path = folder_chapter(folder_path, chapter)

# URL
urlbase = "https://mangareader.to/read/one-piece-3/en/chapter-"
url = urlbase + chapter

# %%
# HTML important content
ad_wall_finder = "z-index: 2147483647"
privacy_iframe_id = '/html/body/iframe[1]'
reject_all_xpath = '/html/body/div[4]/div/div[2]/div/div[4]/div[2]/div[2]/span/div/span'
vertical_xpath = '//*[@id="first-read"]/div[1]/div/div[3]/a[1]'
images_class = "image-vertical"
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
sleep(2)

full_url = driver.page_source
driver.quit()

# %%
img_list = list_img_url(full_url, images_class)

# %%
for link, index in zip(img_list, range(0, len(img_list))):
    download_img(link, chapter_folder_path, index)
