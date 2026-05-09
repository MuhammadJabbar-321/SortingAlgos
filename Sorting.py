import time

# Selection Sort
def selection_sort(arr):# function for sorting
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(n): #outter for loop
        min_index = i

        for j in range(i + 1, n):#inner for loop
            comparisons += 1
            if arr[j] < arr[min_index]:#comparison
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]#swap values
        swaps += 1

    return comparisons, swaps
# Bubble Sort
def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return comparisons, swaps
# Quick Sort
def quick_sort(arr):
    comparisons = 0

    def partition(low, high):
        nonlocal comparisons

        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            comparisons += 1

            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick(low, high):
        if low < high:
            pi = partition(low, high)
            quick(low, pi - 1)
            quick(pi + 1, high)

    quick(0, len(arr) - 1)

    return comparisons

# Merge Sort

def merge_sort(arr):
    comparisons = 0

    def merge(left, right):
        nonlocal comparisons

        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparisons += 1

            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(a):
        if len(a) <= 1:
            return a

        mid = len(a) // 2
        left = sort(a[:mid])
        right = sort(a[mid:])

        return merge(left, right)

    sorted_arr = sort(arr)

    for i in range(len(arr)):
        arr[i] = sorted_arr[i]

    return comparisons

# Test Arrays

test_cases = {
    "5 Sorted": [1, 2, 3, 4, 5],
    "5 Reverse": [5, 4, 3, 2, 1],
    "100 Sorted": list(range(1, 101)),
    "100 Reverse": list(range(100, 0, -1))
}

# Timing Function (Average of 3 runs)

def measure_time(func, arr):
    total_time = 0

    for _ in range(3):
        copy_arr = arr.copy()

        start = time.time()
        result = func(copy_arr)
        end = time.time()

        total_time += (end - start)

    avg_time = total_time / 3
    return avg_time, result


# Running Experiments

algorithms = {
    "Selection Sort": selection_sort,
    "Bubble Sort": bubble_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort
}

for name, func in algorithms.items():
    print("\n==============================")
    print(name)
    print("==============================")

    for case, arr in test_cases.items():
        avg_time, result = measure_time(func, arr)

        print("\nCase:", case)
        print("Average Time:", round(avg_time, 8), "seconds")

        if isinstance(result, tuple):
            print("Comparisons:", result[0])
            print("Swaps:", result[1])
        else:
            print("Comparisons:", result)