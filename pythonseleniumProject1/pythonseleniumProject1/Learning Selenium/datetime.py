from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Format the date and time as a string
formatted_datetime = current_datetime.strftime("%Y_%m_%d_%H_%M_%S")

# Print the formatted date and time
print("Current Date and Time:", formatted_datetime)
