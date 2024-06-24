import math

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr, start, end):
    n = end - start + 1
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def introsort_util(arr, start, end, max_depth):
    size = end - start + 1
    if size < 16:
        insertion_sort(arr, start, end)
    elif max_depth == 0:
        heap_sort(arr, start, end)
    else:
        pivot = partition(arr, start, end)
        introsort_util(arr, start, pivot - 1, max_depth - 1)
        introsort_util(arr, pivot + 1, end, max_depth - 1)

def introsort(arr):
    max_depth = 2 * math.floor(math.log2(len(arr)))
    introsort_util(arr, 0, len(arr) - 1, max_depth)

# Example usage
if __name__ == "__main__":
    arr = [3, 2, 5, 1, 7, 4, 8, 6]
    introsort(arr)
    print("Sorted array:", arr)
