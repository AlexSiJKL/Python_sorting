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

# Selection sort implementation
def selection_sort(arr):
    sorted_data = []
    while data: # Continue until data is empty
        current_min = arr[0]   # Assume the first element is the minimum
        current_min_index = 0   # Index of the minimum element
        
        # Find the minimum element in the data
        for i in range(1, len(arr)):    # Start from the second element
            if arr[i] < current_min:
                current_min = arr[i]
                current_min_index = i
        
        # Append the minimum element to the sorted list
        sorted_data.append(current_min)

        # Remove the minimum element from the original list
        arr.pop(current_min_index)

    return sorted_data

print(selection_sort(data))