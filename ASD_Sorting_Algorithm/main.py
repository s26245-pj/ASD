import time


def main():
    def generate_sorted_arrays():
        sizes = [2000, 4000, 8000, 16000, 32000]
        arrays = []
        for size in sizes:
            array = [i for i in range(1, size + 1)]
            arrays.append(array)
        return arrays

    sorted_arrays = generate_sorted_arrays()

    def generate_unsorted_arrays():
        sizes = [2000, 4000, 8000, 16000, 32000]
        arrays = []
        for size in sizes:
            array = [size - i for i in range(size)]
            arrays.append(array)
        return arrays

    unsorted_arrays = generate_unsorted_arrays()

    def sort_array(arr):
        for j in range(1, len(arr)):
            key = arr[j]
            i = j - 1
            while i >= 0 and arr[i] > key:
                arr[i + 1] = arr[i]
                i -= 1
            arr[i + 1] = key
        return arr

    def measure_sorting_time(sorting_function, array):
        start_time = time.time()
        sorting_function(array)
        end_time = time.time()
        return end_time - start_time

    def check_complexity(arrays, measure_time_function, tables_are_sorted, sorting_function):
        for array in arrays:
            sorting_time = measure_time_function(sorting_function, array)

            if tables_are_sorted:
                n = len(array)
            else:
                n = sum(array)

            ratio = n / sorting_time

            print(ratio)

    print("Complexity for sorted tables:")
    check_complexity(sorted_arrays, measure_sorting_time, True, sort_array)
    print("\nComplexity for unsorted tables:")
    check_complexity(unsorted_arrays, measure_sorting_time, False, sort_array)

main()
