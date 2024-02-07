import openpyxl


def insert_data_into_excel(file_path, sheet_name, new_data):
    # Load the existing workbook
    workbook = openpyxl.load_workbook(file_path)

    # Select the sheet to insert data
    sheet = workbook[sheet_name]

    # Find the next available row
    next_row = sheet.max_row + 1

    # Insert new data into the sheet
    for data_row in new_data:
        sheet.append(data_row)

    # Save the changes
    workbook.save(file_path)
    workbook.close()


# Example usage
file_path = "C:\\python-selenium\\pythonseleniumProject1\\Learning Python\\RajDeshmukh_DailyUpdates.xlsx"
sheet_name = "Sheet1"
new_data = [
    ["26-01-2024", "9", "6", "Done", "Selenium", "-"]
    # Add more rows as needed
]

insert_data_into_excel(file_path, sheet_name, new_data)
