# Task 2: Write and Append Data to a File

# Step 1: Take user input and write to output.txt
user_input = input("Enter text to write to the file: ")

try:
    with open("output.txt", "w") as file:  # 'w' mode overwrites if file exists
        file.write(user_input + "\n")
    print("Data successfully written to output.txt.")
except Exception as e:
    print(f"An error occurred while writing: {e}")

# Step 2: Append additional data
append_input = input("\nEnter additional text to append: ")

try:
    with open("output.txt", "a") as file:  # 'a' mode appends data
        file.write(append_input + "\n")
    print("Data successfully appended.")
except Exception as e:
    print(f"An error occurred while appending: {e}")

# Step 3: Read and display the final content
try:
    print("\nFinal content of output.txt:")
    with open("output.txt", "r") as file:
        for line in file:
            print(line.strip())
except Exception as e:
    print(f"An error occurred while reading: {e}")
