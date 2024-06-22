# Function to Close all tabs
def close_all_tabs(driver, current_tab):

    # List of tabs
    all_tabs = driver.window_handles

    # Closing each tab that is NOT the main tab
    for window in all_tabs:
        if window != current_tab:
            driver.switch_to.window(window)
            driver.close()
            driver.switch_to.window(current_tab)
    print("Closed")
