# File Read & Write Challenge with Error Handling
# This program first creates an input file,
# then reads it, processes the content,
# and writes the result to a new output file.

# STEP 1: Create and write to input.txt
try:
    with open("input.txt", "w") as file:
        file.write("Python is a powerful programming language.\n")
        file.write("File handling allows data storage and retrieval.\n")
        file.write("Error handling prevents program crashes.\n")
        file.write("This assignment practices read and write operations.\n")
        file.write("Learning Python is both useful and fun.\n")

    print("✅ 'input.txt' created successfully.\n")

except Exception as error:
    print("❌ Failed to create input.txt:", error)

# STEP 2: Ask the user for the filename to read
filename = input("Enter the name of the file to read: ")

try:
    # STEP 3: Open and read the file
    with open(filename, "r") as file:
        content = file.read()

    # STEP 4: Process the content
    uppercase_text = content.upper()      # Convert text to uppercase
    word_count = len(content.split())     # Count number of words

    # STEP 5: Write processed content to output.txt
    with open("output.txt", "w") as file:
        file.write("MODIFIED TEXT:\n")
        file.write(uppercase_text)
        file.write("\n\n")
        file.write(f"WORD COUNT: {word_count}")

    # STEP 6: Success message
    print("\n✅ File processed successfully!")
    print("📄 Output written to 'output.txt'")

# Handle error if the file does not exist
except FileNotFoundError:
    print("❌ Error: The file does not exist.")

# Handle error if the file cannot be read
except PermissionError:
    print("❌ Error: Permission denied. Cannot read the file.")

# Handle any other unexpected errors
except Exception as error:
    print("❌ An unexpected error occurred:", error)
