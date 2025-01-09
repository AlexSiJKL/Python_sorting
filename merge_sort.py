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

# Merge sort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_part = merge_sort(arr[:mid])
    right_part = merge_sort(arr[mid:])

    # Merging the two sorted parts
    sorted_data = []
    i = j = 0

    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            sorted_data.append(left_part[i])
            i += 1
        else:
            sorted_data.append(right_part[j])
            j += 1
    
    # Adding the remaining elements
    sorted_data.extend(left_part[i:])
    sorted_data.extend(right_part[j:])
    
    return sorted_data

print(merge_sort(data))