# Importing Libraries
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from WebDriver_Close_All_Tabs import close_all_tabs


# Function
def adwall(driver, ad_wall_finder, current_tab):

    # Creating an ad variable to loop
    ad = True
    while ad:

        # The ads will come up after a short time. It's no use trying other waiting types (aka webdriver waiting)
        sleep(10)

        # Storing URL content
        url_content = driver.page_source

        # Checking if the advertising content is in it
        if ad_wall_finder in url_content:

            # Instancing action to the Webdriver
            action = ActionChains(driver)

            # Moving cursor to the top of the website
            action.move_by_offset(0, 0)
            action.perform()

            # Click in the corner of the site body (just to pop up unwanted ads)
            action.click().perform()

            # Switch to the main tab
            driver.switch_to.window(current_tab)
            print("Ads Up")

        # if it IS NOT, break the loop
        else:
            print("No Ads")
            ad = False

    # Close all tabs
    close_all_tabs(driver, current_tab)
