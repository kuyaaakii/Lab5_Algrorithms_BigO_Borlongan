from constants import *

# Generate Dataset A
dataset_a = []

for i in range(SEED_DIGIT):
    value = ID_SUM + i
    dataset_a.append(value)

# Generate Dataset B
dataset_b = []

for i in range(ARTIST_LENGTH):
    value = NAME_LENGTH + i
    dataset_b.append(value)

# Merge the two sorted datasets
merged_dataset = []

i = 0
j = 0
comparisons = 0

while i < len(dataset_a) and j < len(dataset_b):
    comparisons += 1

    if dataset_a[i] <= dataset_b[j]:
        merged_dataset.append(dataset_a[i])
        i += 1
    else:
        merged_dataset.append(dataset_b[j])
        j += 1

# Append any remaining records
while i < len(dataset_a):
    merged_dataset.append(dataset_a[i])
    i += 1

while j < len(dataset_b):
    merged_dataset.append(dataset_b[j])
    j += 1

# Verify the final order
ordered = True

for i in range(len(merged_dataset) - 1):
    if merged_dataset[i] > merged_dataset[i + 1]:
        ordered = False
        break

# Display results
print("Department A Dataset:", dataset_a)
print("Department B Dataset:", dataset_b)
print("Consolidated Dataset:", merged_dataset)

print("\nNumber of Records Before Consolidation:",
      len(dataset_a) + len(dataset_b))
print("Number of Records After Consolidation:",
      len(merged_dataset))
print("Comparison Count:", comparisons)
print("Ordering Verification:", ordered)

print("\nTime Complexity: O(n + m)")
print("Space Complexity: O(n + m)")
