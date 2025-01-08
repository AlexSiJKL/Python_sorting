import random
import os.path

# Generate a list of 1000 unique random integers between 0 and 9999
unique_values = random.sample(range(10000), 1000)

# Get the current working directory
current_directory = os.getcwd()

# Define the file name
file_name = "input.txt"

# Construct the file path
file_path = os.path.join(current_directory, file_name)

# Save data to the file
with open(file_path, "w") as file:
    file.write(', '.join(map(str, unique_values)))

print(f"File saved at: {file_path}")