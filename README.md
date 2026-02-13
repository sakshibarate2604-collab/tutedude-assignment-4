# tutedude-assignment-4
done by sakshi barate python code only 
assignment:4
 Module 5: 
Files, Exceptions, and Errors in Python
Task 1:
 Read a File and Handle Errors
Python Program
try:
    # Opening and reading the file
    with open("sample.txt", "r") as file:
        print("File content:\n")
        
        # Reading line by line
        for line in file:
            print(line.strip())

# Handling error if file does not exist
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
✔ Explanation
open("sample.txt", "r") → Opens file in read mode

with → Automatically closes the file

for line in file → Reads file line by line

FileNotFoundError → Handles missing file error

✔ Expected Output
:If file exists
File content:
Hello World
Welcome to Python
:If file does not exist
Error: The file 'sample.txt' does not exist.
: Task 2: Write and Append Data to a File
: Python Program
# Taking user input
data = input("Enter some data: ")

# Writing data to file
with open("output.txt", "w") as file:
    file.write(data + "\n")

print("Data written successfully.")

# Appending additional data
extra_data = input("Enter additional data to append: ")

with open("output.txt", "a") as file:
    file.write(extra_data + "\n")

print("Data appended successfully.")

# Reading final content
print("\nFinal content of file:")

with open("output.txt", "r") as file:
    print(file.read())
Explanation
"w" → Writes data (overwrites file)

"a" → Appends data

"r" → Reads file

: Expected Output (Example)
If user enters:

Enter some data: 25
Enter additional data to append: Python is easy
Output:

Data written successfully.
Data appended successfully.

Final content of file:
25
Python is easy
GitHub Submission Structure
Your repository should look like this:

Module5-Files-Exceptions-Python

: task1_read_file.py
:task2_write_append.py
:README.md
: README.md Content (Copy This)
# Module 5: Files, Exceptions, and Errors in Python

## Task 1: Read File and Handle Errors
This program reads a file named sample.txt 
and prints its content line by line.
 It also handles the error if the file does not exist.

## Task 2: Write and Append Data
This program:
- Takes user input and writes it to output.txt
- Appends additional input to the same file
- Reads and displays the final file content

:Technologies Used
- Python
