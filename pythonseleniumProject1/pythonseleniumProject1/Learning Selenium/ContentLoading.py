from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (specify the path to your chromedriver.exe)
chrome_service = webdriver.chrome.service.Service(executable_path="C:\\browserdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)

# Navigate to a website
driver.get("https://www.google.com")
print("Page Title:", driver.title)

# Maximize the browser window
driver.maximize_window()

# Find the search box, enter a query, and submit the form
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium WebDriver")
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search")))
    print("Search results loaded successfully.")
except Exception as e:
    print("Error:", e)

# Click on the first search result link
first_result_link = driver.find_element(By.CSS_SELECTOR, "h3 a")
first_result_link.click()

# Wait for the page to load completely
WebDriverWait(driver, 10).until(EC.title_contains("Selenium WebDriver"))

# Print the current URL
print("Current URL:", driver.current_url)

# Close the browser window
driver.quit()
