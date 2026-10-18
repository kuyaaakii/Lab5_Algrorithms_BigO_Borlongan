from constants import *

# Generate the original incident records
record_count = NAME_LENGTH + ARTIST_LENGTH

original_records = []

for i in range(record_count):
    incident = ID_SUM + i
    original_records.append(incident)

# Rotate the records using SEED_DIGIT
rotation_point = SEED_DIGIT % len(original_records)

rotated_records = (
    original_records[rotation_point:]
    + original_records[:rotation_point]
)

# Generate the target incident using ID_SUM and ARTIST_SUM
target = ID_SUM + (ARTIST_SUM % record_count)

# Binary search for a target in a rotated sorted list
def rotated_binary_search(data, target):
    low = 0
    high = len(data) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2

        comparisons += 1
        if data[mid] == target:
            return mid, comparisons

        comparisons += 1
        if data[low] <= data[mid]:

            comparisons += 1
            if data[low] <= target:

                comparisons += 1
                if target < data[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:
                low = mid + 1

        else:
            comparisons += 1
            if data[mid] < target:

                comparisons += 1
                if target <= data[high]:
                    low = mid + 1
                else:
                    high = mid - 1

            else:
                high = mid - 1

    return -1, comparisons


# Linear search for comparison
def linear_search(data, target):
    comparisons = 0

    for i in range(len(data)):
        comparisons += 1

        if data[i] == target:
            return i, comparisons

    return -1, comparisons


# Perform both searches
binary_position, binary_comparisons = rotated_binary_search(
    rotated_records, target
)

linear_position, linear_comparisons = linear_search(
    rotated_records, target
)

# Display the results
print("Original Dataset:", original_records)
print("Rotated Dataset:", rotated_records)
print("Target Incident:", target)

print("\nBinary Search")
print("Position:", binary_position)
print("Comparisons:", binary_comparisons)

print("\nLinear Search")
print("Position:", linear_position)
print("Comparisons:", linear_comparisons)

print("\nComplexity Analysis")
print("Binary Search: O(log n) time, O(1) extra space")
print("Linear Search: O(n) time, O(1) extra space")