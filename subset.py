def generate_subsets(arr):
    def backtrack(start, current_subset):
        subsets.append(list(current_subset))
        for i in range(start, len(arr)):
            current_subset.append(arr[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()
        return
    subsets = []
    backtrack(0, [])
    return subsets

arr = [1, 2]
result = generate_subsets(arr)
print(result)