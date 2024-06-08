from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ask user for the YouTube URL

youtube_url = input("Please enter the YouTube URL: ")

# Set up WebDriver
driver = webdriver.Chrome()
print("Opening webpage...")
driver.get("https://ytmp3s.nu/6Fuo/")
print("Page loaded.")

try:
    # Check if there's an iframe and switch
    iframes = driver.find_elements(By.TAG_NAME, 'iframe')
    if iframes:
        print("Switching to iframe.")
        driver.switch_to.frame(iframes[0])

    print("Locating input box...")
    input_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "url"))  # Adjust based on actual ID if different
    )
    print("Input box found.")
    input_box.clear()
    input_box.send_keys(youtube_url)

    print("Locating Convert button...")
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='submit'][@value='Convert']"))
    )
    print("Button found.")
    button.click()
    print("Button clicked.")

    # Wait for the 'Download Now' button to appear and click it
    print("Waiting for 'Download Now' button to appear...")
    download_button = WebDriverWait(driver, 120).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Download')]"))  # Adjust XPath as needed
    )
    print("'Download Now' button found.")
    download_button.click()
    print("'Download Now' button clicked.")

    # Additional delay to observe the actions or let downloads start
    print("Process complete. Closing in 30 seconds...")
    time.sleep(30)

finally:
    print("Script ending, browser will close.")
    driver.quit()  # Ensure the browser closes cleanly

