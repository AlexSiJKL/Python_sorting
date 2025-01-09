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

# Insertion sort implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_el = arr[i]
        j = i - 1
        
        # until the correct position for the current element is found
        while current_el < arr[j] and j >= 0:
            arr[j + 1] = arr[j]     # Shift the element to the right
            j -= 1
        arr[j + 1] = current_el     # Insert the current element at its correct position
    return arr

sorted_data = insertion_sort(data)
print(sorted_data)