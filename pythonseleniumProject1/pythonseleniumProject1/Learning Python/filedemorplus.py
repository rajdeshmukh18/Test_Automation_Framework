# Open a file in 'r+' mode
with open('demo.txt', 'r+') as file:
    # Read content from the file
    content = file.read()
    print("Read content:", content)

    # Move the file pointer to the beginning
    file.seek(0)

    # Write new content to the file
    file.write("New content added!")

    # Move the file pointer to the end (optional, depends on your use case)
    #file.seek(0, 2)
    file.seek(0)
    # Read the modified content
    modified_content = file.read()
    print("Modified content:", modified_content)
