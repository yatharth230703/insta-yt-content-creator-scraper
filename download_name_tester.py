import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
import os 

# Load URLs from an Excel file
filenames=[]
excel_path = r'C:\Users\Yatharth\Desktop\desktop1\AI\pgagi\yt_selenium_try\Copy of AI Project Data Training Sheet.xlsx'  
df = pd.read_excel(excel_path)
urls = df['Reference URL'].tolist() 

def random_click(driver):
    """Function to perform a random click within the browser window."""
    window_size = driver.get_window_size()
    x = random.randint(0, window_size['width'] - 1)
    y = random.randint(0, window_size['height'] - 1)
    action = ActionChains(driver)
    action.move_by_offset(x, y).click().perform()
    print(f"Randomly clicked at ({x}, {y}).")
    action.move_by_offset(-x, -y).perform() 
download_path = r"C:\Users\Yatharth\Desktop\desktop1\AI\pgagi\yt_selenium_try\downloaded_vids"
def print_page_source(driver):
    print("Printing page source for diagnostics...")
    print(driver.page_source[:5000])  # Print first 5000 characters of the page source
def automator (url,l):

    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,  # Disable confirmation dialog
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    driver = webdriver.Chrome(options=chrome_options)
    instagram_url = url

    # Set up WebDriver
    

    try:
        # Navigate to the website
        driver.get("https://instavideosave.net/audio")
        #print("Opening webpage...")
        
        # Wait until the page is loaded
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        #print("Page loaded.")

        # Locate the input box using a more specific selector
        #print("Locating input box...")
        try:
            input_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='url'][name='url']"))
            )
            #print("Input box found.")
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
            #print("Advertisement close button found.")
            close_ad_button.click()
            #print("Advertisement closed.")
        except Exception as e:
            print("No advertisement to close or close button not found.")
        
        # Submit the form by locating the correct button and clicking it
        #print("Locating and clicking the Download button...")
        try:
            submit_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
            )
            #print("Download button found and clicked.")
            submit_button.click()
        except Exception as e:
            print(f"Failed to locate or click the Download button: {str(e)}")
            print_page_source(driver)
            raise
       
        # Wait for and click the "Download Audio" button
        #print("Waiting for 'Download Audio' button to appear...")
        try:
            download_audio_button = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Download Audio')]"))
            )
            # Scroll into view and then click using JavaScript
            driver.execute_script("arguments[0].scrollIntoView(true);", download_audio_button)
            driver.execute_script("arguments[0].click();", download_audio_button)
            #print("Download Audio button found and clicked.")
        except Exception as e:
            print(f"Failed to locate or click the 'Download Audio' button: {str(e)}")
            print_page_source(driver)
            raise
        random_click(driver)
        
        #print("Process complete. Closing in 30 seconds...")
        time.sleep(30)
        time.sleep(10)  # Example: Wait 10 seconds for the download to complete

        files = os.listdir(download_path)
        if files:
            downloaded_file_name = files[l]  # Assumes only one file is downloaded
            print("Downloaded file:", downloaded_file_name)
            filenames.append(downloaded_file_name)
        else:
            print("No files downloaded.")

    finally:
        print("Script ending, browser will close.")
        driver.quit()  
    #return url
l=0
for i in urls:
    automator(i,l)
    print ("the following link has been processed : " , i )
    l+=1
