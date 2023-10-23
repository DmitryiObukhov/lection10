import shutil

with open("copy1.txt", 'w') as file:
    content = file.write("Content.\nMore content.")

with open("copy1.txt", 'r') as file:
    content = file.read()

content_upper = content.upper()
current_file = "copy1.txt"
copy_of_file = "copy2.txt"
shutil.copy(current_file, copy_of_file)

with open(copy_of_file, 'w') as copy_file:
    copy_file.write(content_upper)
