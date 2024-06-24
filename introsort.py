import math

# Import the math module for mathematical functions like log2 and floor.

def insertion_sort(arr, left, right):
    # Define an insertion sort function for sorting small subarrays.
    for i in range(left + 1, right + 1):
        # Iterate through the array from the second element to the rightmost element.
        key = arr[i]
        # The key is the element to be positioned correctly.
        j = i - 1
        # Start comparing with the element before the key.
        while j >= left and arr[j] > key:
            # Move elements greater than key to one position ahead.
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        # Place the key in its correct position.

def heapify(arr, n, i):
    # Define a heapify function to maintain the heap property.
    largest = i
    l = 2 * i + 1
    # Left child index.
    r = 2 * i + 2
    # Right child index.
    if l < n and arr[l] > arr[largest]:
        # If left child is larger than root.
        largest = l
    if r < n and arr[r] > arr[largest]:
        # If right child is larger than largest so far.
        largest = r
    if largest != i:
        # If largest is not the root, swap them.
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected sub-tree.
        heapify(arr, n, largest)
def heap_sort(arr, start, end):
    # Define a heap sort function.
    n = end - start + 1
    # Calculate the size of the heap.
    for i in range(n // 2 - 1, -1, -1):
        # Build a max heap.
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        # Extract elements from the heap.
        arr[i], arr[0] = arr[0], arr[i]
        # Move current root to end.
        heapify(arr, i, 0)
        # Call heapify on the reduced heap.
def partition(arr, low, high):
    # Define the partition function for quicksort.
    pivot = arr[high]
    # Choose the rightmost element as pivot.
    i = low - 1
    # Index of smaller element.
    for j in range(low, high):
        # Iterate through the array.
        if arr[j] <= pivot:
            # If current element is smaller than or equal to pivot.
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            # Swap it with the element at i.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # Place pivot in correct position.
    return i + 1
    # Return the partition index.
def introsort_util(arr, start, end, max_depth):
    # Define the utility function for introsort.
    size = end - start + 1
    # Calculate the size of the subarray.
    if size < 16:
        # Use insertion sort for small arrays.
        insertion_sort(arr, start, end)
    elif max_depth == 0:
        # Switch to heap sort if maximum depth is reached.
        heap_sort(arr, start, end)
    else:
        # Otherwise, use quicksort.
        pivot = partition(arr, start, end)
        # Partition the array.
        introsort_util(arr, start, pivot - 1, max_depth - 1)
        # Sort the left subarray.
        introsort_util(arr, pivot + 1, end, max_depth - 1)
        # Sort the right subarray.

def introsort(arr):
    # Define the main introsort function.
    max_depth = 2 * math.floor(math.log2(len(arr)))
    # Set the maximum depth limit.
    introsort_util(arr, 0, len(arr) - 1, max_depth)
    # Call the utility function to start sorting.


# Example usage
if __name__ == "__main__":
    arr = [3, 2, 5, 1, 7, 4, 8, 6]
    # Define an array to be sorted.
    introsort(arr)
    # Call introsort on the array.
    print("Sorted array:", arr)
    # Print the sorted array.
