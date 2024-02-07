import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=2)

    def insert_data(self, key, value):
        self.data[key] = value
        self.save_data()

    def retrieve_data(self, key):
        return self.data.get(key)

# Example usage
file_path = "data_file.json"

# Create an instance of the DataHandler class
data_handler = DataHandler(file_path)

# Insert data into the file using key-value pairs
data_handler.insert_data("username", "raj")
data_handler.insert_data("password", "raj@123")

# Retrieve data using keys
username = data_handler.retrieve_data("username")
password = data_handler.retrieve_data("password")

# Print retrieved data
print("Username:", username)
print("Password:", password)

# Example using Selenium (assuming you have a webpage with username and password fields)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/")

# Use the retrieved data in Selenium
username_input = driver.find_element(By.NAME, "username")  # Replace with the actual ID or selector of the username input field
password_input = driver.find_element(By.NAME, "password")  # Replace with the actual ID or selector of the password input field

# Enter the retrieved data into the input fields
username_input.send_keys(username)
password_input.send_keys(password)
time.sleep(4)
# Perform other actions or submit the form as needed

# Close the browser
driver.quit()
