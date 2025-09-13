# Module 5: Files, Exceptions, and Errors in Python
# Task 1: Read a File and Handle Errors

try:
    # Open the file in read mode
    with open("sample.txt", "r") as file:
        print("Contents of sample.txt:\n")
        # Read and print each line
        for line in file:
            print(line.strip())
except FileNotFoundError:
    # Handle the case where the file does not exist
    print("Error: The file 'sample.txt' was not found. Please make sure it exists.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"An unexpected error occurred: {e}")
