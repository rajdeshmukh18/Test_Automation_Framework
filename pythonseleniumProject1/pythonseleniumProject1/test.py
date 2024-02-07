from selenium import webdriver


chrome_service = webdriver.chrome.service.Service(executable_path="C:\\browserdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)

driver.get('https://www.google.com')