def binary_search(arr, target):
    low, high, c = 0, len(arr) - 1, 0
    while low <= high:
        mid = (low + high) // 2
        c += 1
        if arr[mid] == target:
            case = "Best case O(1)" if c == 1 else "Average case O(log n)"
            print(f"Found at index {mid} \ncomparisons: {c} \n{case}")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    print(f"Not found. Comparison count: {c}; Worst case O(log n)")
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
binary_search(arr, int(input("Enter the target number to search: ")))