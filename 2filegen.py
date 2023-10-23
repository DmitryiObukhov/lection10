import string
import os
from random import randint

file_summary = []

if not os.path.exists("files"):
    os.mkdir("files")

for letter in string.ascii_lowercase:
    filename = f"files/{letter}.txt"
    number = randint(1, 100)
    with open(filename, "w") as file:
        file.write(str(number))
    file_summary.append(f"{filename}: {number}")

with open("summary.txt", "w") as summary_file:
    for line in file_summary:
        summary_file.write(line + '\n')
