import time
import random
from copy import deepcopy

# Heapsort Implementation
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Custom Merge Sort
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Comparison Function
def compare_sorts():
    sizes = [1000, 5000, 10000]
    for size in sizes:
        print(f"\n--- Sorting Comparison for Size: {size} ---")
        original = [random.randint(0, 100000) for _ in range(size)]

        for case_name, case in {
            "Random": deepcopy(original),
            "Sorted": sorted(original),
            "Reverse": sorted(original, reverse=True)
        }.items():

            print(f"\nInput: {case_name}")

            # Heapsort
            arr1 = deepcopy(case)
            start = time.time()
            heapsort(arr1)
            print(f"Heapsort: {(time.time() - start):.6f} seconds")

            # Quicksort (Python built-in Timsort)
            arr2 = deepcopy(case)
            start = time.time()
            sorted_arr2 = sorted(arr2)
            print(f"Quicksort (Python built-in): {(time.time() - start):.6f} seconds")

            # Merge Sort
            arr3 = deepcopy(case)
            start = time.time()
            sorted_arr3 = mergesort(arr3)
            print(f"Merge Sort: {(time.time() - start):.6f} seconds")

# Run the comparison
compare_sorts()
