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

# Heap sort implementation
def sift_down(arr, i, n):
    while 2 * i + 1 < n:                        # While there is a left child
        j = 2 * i + 1                           # Left child index
        # If there is a right child and it is greater than the left child
        if 2 * i + 2 < n and arr[2 * i + 2] > arr[j]:
            j = 2 * i + 2   # Update j to the right child index
        # If the parent is greater than or equal to the largest child
        if arr[i] >= arr[j]:
            break                               # The heap property is satisfied
        else:
            arr[i], arr[j] = arr[j], arr[i]     # Swap the parent with the larger child
            i = j                               # Move down to the child index


def heap_sort(arr):
    n = len(arr)
    # Create max heap
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, i, n)                    # Sift down to maintain heap property
    
    # Sort in ascending order
    for i in range(n - 1, 0, -1):
        # Swap the root of the heap (largest element) with the last element
        arr[0], arr[i] = arr[i], arr[0]
        # Restore the heap property for the reduced heap
        sift_down(arr, 0, i)
    
    return arr

# Example usage:
sorted_data = heap_sort(data)
print(sorted_data)