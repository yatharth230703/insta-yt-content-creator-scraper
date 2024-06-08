from selenium import webdriver

# Set up WebDriver (assuming Chrome)
driver = webdriver.Chrome()

# Open a YouTube video
driver.get("https://www.youtube.com/watch?v=4-BWFsE_TQE")

# Optionally, interact with the page (e.g., skip ads, adjust settings)
