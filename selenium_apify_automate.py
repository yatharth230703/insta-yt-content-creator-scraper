from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time  # Import time module

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--enable-chrome-browser-cloud-management")

# Set up WebDriver with Chrome options
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ytmp3s.nu/6Fuo/")

# Find the search box using the updated method
search_box = driver.find_element(By.NAME, 'Convert')

# Type in a search term and submit
search_box.send_keys('https://www.youtube.com/watch?v=7JXomLN8YUU')
search_box.send_keys(Keys.RETURN)

# Wait for a specified time to observe the results
time.sleep(30)  # Wait for 30 seconds

# Close the browser
driver.quit()


