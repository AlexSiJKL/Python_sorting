import os

# Define the filename
filename = "input.txt"
# Get the current directory of the script
current_directory = os.path.dirname(os.path.abspath(__file__))
path = current_directory

try:
    # Open the file and process its contents
    with open(os.path.join(path, filename), "r") as file:
        # Read all lines and convert them into a flat list of integers
        data = [int(num) for line in file for num in line.split(',')]
except Exception as e:
    # Print an error message if the file cannot be read or processed
    print("Failed to read file:", e)
    data = []

sorted_data = []

# Selection sort implementation
while data:             # Continue until data is empty
    min_el = data[0]    # Assume the first element is the minimum
    min_el_index = 0    # Index of the minimum element
    
    # Find the minimum element in the data
    for i in range(1, len(data)):    # Start from the second element
        if data[i] < min_el:
            min_el = data[i]
            min_el_index = i
    
    # Append the minimum element to the sorted list
    sorted_data.append(min_el)

    # Remove the minimum element from the original list
    data.pop(min_el_index)

print(sorted_data)