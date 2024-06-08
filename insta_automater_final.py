import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to print page source when an error occurs
def print_page_source(driver):
    print("Printing page source for diagnostics...")
    print(driver.page_source[:5000])  # Print first 5000 characters of the page source

# Ask user for the Instagram URL at the beginning of the script
instagram_url = input("Please enter the Instagram URL: ")

# Set up WebDriver
driver = webdriver.Chrome()
def random_click(driver):
    """Function to perform a random click within the browser window."""
    window_size = driver.get_window_size()
    x = random.randint(0, window_size['width'] - 1)
    y = random.randint(0, window_size['height'] - 1)
    action = ActionChains(driver)
    action.move_by_offset(x, y).click().perform()
    print(f"Randomly clicked at ({x}, {y}).")
    action.move_by_offset(-x, -y).perform() 
try:
    # Navigate to the website
    driver.get("https://instavideosave.net/audio")
    print("Opening webpage...")
    
    # Wait until the page is loaded
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print("Page loaded.")

    # Locate the input box using a more specific selector
    print("Locating input box...")
    try:
        input_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='url'][name='url']"))
        )
        print("Input box found.")
        input_box.clear()
        input_box.send_keys(instagram_url)
        input_box.send_keys(Keys.TAB)  # To trigger any JavaScript that runs on losing focus
        time.sleep(2)  # Wait a bit for any JavaScript processing
    except Exception as e:
        print(f"Failed to locate input box: {str(e)}")
        print_page_source(driver)
        raise

    # Attempt to close any advertisement that may be covering the page elements
    try:
        close_ad_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Close')]"))  # Adjust the XPath as necessary
        )
        print("Advertisement close button found.")
        close_ad_button.click()
        print("Advertisement closed.")
    except Exception as e:
        print("No advertisement to close or close button not found.")

    # Submit the form by locating the correct button and clicking it
    print("Locating and clicking the Download button...")
    try:
        submit_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        print("Download button found and clicked.")
        submit_button.click()
    except Exception as e:
        print(f"Failed to locate or click the Download button: {str(e)}")
        print_page_source(driver)
        raise

    # Wait for and click the "Download Audio" button
    print("Waiting for 'Download Audio' button to appear...")
    try:
        download_audio_button = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Download Audio')]"))
        )
        # Scroll into view and then click using JavaScript
        driver.execute_script("arguments[0].scrollIntoView(true);", download_audio_button)
        driver.execute_script("arguments[0].click();", download_audio_button)
        print("Download Audio button found and clicked.")
    except Exception as e:
        print(f"Failed to locate or click the 'Download Audio' button: {str(e)}")
        print_page_source(driver)
        raise
    random_click(driver)

    print("Process complete. Closing in 30 seconds...")
    time.sleep(30)

finally:
    print("Script ending, browser will close.")
    driver.quit()  
