# Opening and reading the file
    with open("sample.txt", "r") as file:
        print("File content:\n")
        
 # Reading line by line
        for line in file:
            print(line.strip())

# Handling error if file does not exist
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
