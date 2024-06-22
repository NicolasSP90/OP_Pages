# Importing Libraries
from selenium import webdriver

# Private Browsing Profile
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('prefs', {'profile.default_content_setting_values.cookies': 2})
chrome_options.add_experimental_option('prefs', {"profile.block_third_party_cookies": True})
chrome_options.add_experimental_option("useAutomationExtension", False)
