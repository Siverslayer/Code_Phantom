import subprocess

def create_and_write_file(file_path, code):
    try:
        # Open the file in write mode with UTF-8 encoding
        with open(file_path, 'w', encoding='utf-8') as file:
            # Write the code to the file
            file.write(code)
        print(f"File {file_path} created and code written successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file and writing the code: {e}")

def run_file(file_path):
    try:
        # Execute the file using subprocess
        subprocess.run(['python', file_path])
    except Exception as e:
        print(f"An error occurred while running the file: {e}")

# The path where you want to create the file
file_path = r""

# The code you want to put in the file
code = """
# The code you want
"""

# Create the file and write the code in it
create_and_write_file(file_path, code)

# Run the file
run_file(file_path)
