import json
import os


class DataHandler:
    def __init__(self, base_file_path, max_file_size_kb=0.2):
        self.base_file_path = base_file_path
        self.max_file_size = max_file_size_kb * 1024  # Convert to bytes
        self.current_file_path = None
        self.data = self.load_data()

    def load_data(self):
        if not os.path.exists(self.base_file_path):
            return {}

        with open(self.base_file_path, 'r') as file:
            data = json.load(file)
            return data

    def save_data(self):
        with open(self.current_file_path, 'w') as file:
            json.dump(self.data, file, indent=2)

    def insert_data(self, key, value):
        if self.current_file_path is None or os.path.getsize(self.current_file_path) > self.max_file_size:
            self.create_new_file()

        self.data[key] = value
        self.save_data()

    def create_new_file(self):
        file_number = len([f for f in os.listdir('.') if f.startswith('data_file')]) + 1
        new_file_path = f"data_file_{file_number}.json"
        self.current_file_path = new_file_path
        self.data = {}
        self.save_data()


# Example usage
base_file_path = "data_file.json"

# Create an instance of the DataHandler class
data_handler = DataHandler(base_file_path)

# Insert data into the file until the file size reaches 10 KB
for i in range(20):  # Inserting 20 key-value pairs for demonstration
    data_handler.insert_data(f"key_{i}", f"value_{i}")

# You can check the created files in the current working directory

# Print the current file path and size
print("Current File Path:", data_handler.current_file_path)
print("Current File Size:", os.path.getsize(data_handler.current_file_path), "bytes")