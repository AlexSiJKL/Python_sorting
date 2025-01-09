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

# Bubble sort implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        # Compare elements in the unsorted part of the array
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps occurred during the pass, the array is already sorted
        if not swapped:
                break
    return arr

print(bubble_sort(data))