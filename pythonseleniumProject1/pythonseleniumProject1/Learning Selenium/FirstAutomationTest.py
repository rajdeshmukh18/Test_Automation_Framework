from selenium import webdriver
import time

chrome_service = webdriver.chrome.service.Service(executable_path="C:\\browserdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)

driver.get('https://www.google.com')
print(driver.title)
print(driver.current_url)
driver.maximize_window()

# Adding a delay of 5 seconds (you can adjust the duration)
time.sleep(5)

# Or, you can wait for user input to close the browser
input("Press Enter to close the browser...")

# Close the browser
driver.quit()
