import random
import time


def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)


def countingSort(arr):
    max_val = max(arr)
    counts = [0] * (max_val + 1)
    sorted_arr = []
    for num in arr:
        counts[num] += 1
    for i in range(len(counts)):
        sorted_arr.extend([i] * counts[i])
    return sorted_arr


def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def generateArray(size):
    return [random.randint(1, 1000) for _ in range(size)]


def measureSortingTime(sort_function, array):
    start_time = time.time()
    sorted_array = sort_function(array)
    sorting_time = time.time() - start_time
    return sorting_time, sorted_array


array_size = 10000000
random_array = generateArray(array_size)

quickSortTime, quickSortedArray = measureSortingTime(quickSort, random_array)

countingSortTime, countingSortedArray = measureSortingTime(countingSort, random_array)

heapSortTime, heapSortedArray = measureSortingTime(heapSort, random_array)

print(f"Quicksort: {quickSortTime} s")
print(f"CountingSort: {countingSortTime} s")
print(f"Heapsort: {heapSortTime} s")
