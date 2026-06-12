def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            c = i + 1
            case ="Best Case 0(1)" if c == 1 else "Worst Case O(n)" if c == len(arr) else "Average Case O(n)"
            return f"Element found at index {i} \nComparisons {c} \n{case}"
    return "Element not found in the array."

# Example usage
arr = [23, 34, 3, 4, 45,1]
# arr = list(map(int,input("Enter the number separated by comma:").split()))
result = linear_search(arr, int(input("Enter the target element: ")))
print(result)
