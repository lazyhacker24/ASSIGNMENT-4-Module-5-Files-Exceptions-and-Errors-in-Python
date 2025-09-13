# Task: Read sample.txt and print line by line with line numbers

try:
    with open("sample.txt", "r") as file:
        print("Reading file content:")
        for i, line in enumerate(file, start=1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("Error: This file 'sample.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
