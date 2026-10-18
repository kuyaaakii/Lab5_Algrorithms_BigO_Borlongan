
# [EXERCISE 3] E-COMMERCE ORDER PROCESSING

from constants import *
import random
import time

# Generate student-specific order values
record_count = NAME_LENGTH + ARTIST_LENGTH
orders = []

for i in range(record_count):
    value = ID_SUM + ARTIST_SUM + (i * (SEED_DIGIT + 1))
    orders.append(value)


# Bubble Sort
def bubble_sort(data):
    comparisons = 0
    movements = 0
    n = len(data)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            comparisons += 1

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                movements += 3
                swapped = True

        if not swapped:
            break

    return data, comparisons, movements


# Selection Sort
def selection_sort(data):
    comparisons = 0
    movements = 0
    n = len(data)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1

            if data[j] < data[min_index]:
                min_index = j

        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
            movements += 3

    return data, comparisons, movements


# Insertion Sort
def insertion_sort(data):
    comparisons = 0
    movements = 0
    n = len(data)

    for i in range(1, n):
        key = data[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if data[j] > key:
                data[j + 1] = data[j]
                movements += 1
                j -= 1
            else:
                break

        data[j + 1] = key
        movements += 1

    return data, comparisons, movements


# Generate the three input conditions
sorted_orders = orders.copy()
reverse_orders = sorted_orders[::-1]

random_orders = orders.copy()
random.Random(SEED_DIGIT).shuffle(random_orders)

conditions = [
    ("Sorted", sorted_orders),
    ("Reverse", reverse_orders),
    ("Random", random_orders)
]

algorithms = [
    ("Bubble Sort", bubble_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort)
]


# Run and compare the algorithms
for condition_name, original_data in conditions:
    print("\nInput Condition:", condition_name)
    print("Original Orders:", original_data)

    for algorithm_name, algorithm in algorithms:
        data = original_data.copy()

        start_time = time.perf_counter()
        result, comparisons, movements = algorithm(data)
        end_time = time.perf_counter()

        execution_time = end_time - start_time

        # Verify the result
        correct = result == sorted(original_data)

        print("\n", algorithm_name)
        print("Sorted Orders:", result)
        print("Comparisons:", comparisons)
        print("Movements:", movements)
        print(f"Execution Time: {execution_time:.8f} seconds")
        print("Sorting Correct:", correct)


# Complexity analysis
print("\nBig O Analysis")
print("Bubble Sort: Best O(n), Average O(n^2), Worst O(n^2)")
print("Selection Sort: Best/Average/Worst O(n^2)")
print("Insertion Sort: Best O(n), Average O(n^2), Worst O(n^2)")
print("Auxiliary Space: O(1) for all three algorithms")
