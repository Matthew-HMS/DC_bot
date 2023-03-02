# open the file in read and write mode
file = open("test.txt", "r+")

# read the content of the file
content = file.read()
print("The original content of the file is:")
print(content)

# modify the content of the file
file.write("\nThis is a modified text.\n") # write a new line at the beginning of the file

# read the modified content of the file
file.seek(0) # move the cursor to the beginning of the file
modified_content = file.read()
print("The modified content of the file is:")
print(modified_content)

# close the file
file.close()