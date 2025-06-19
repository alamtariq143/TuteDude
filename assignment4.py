# Task 1: Read a File and Handle Errors 

from pathlib import Path
file_path = Path('sample.txt')
try:
    with open('sample.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: The file {file_path} was not found.")

# Task 2: Write and Append Data to a File
with open('output.txt', 'w') as file:
    file.write("Enter text to write to the file: Hello, Python!\nData successfully written to output.txt.")

with open('output.txt', 'a') as file:
    file.write("\nEnter additional text to append: Learning file handling in Python\nData successfully append.")
    
with open('output.txt', 'r') as file:
    content = file.read()
    print(content)