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
