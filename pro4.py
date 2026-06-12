def bubble_sort(arr):
    n,c = len(arr),0
    for i in range(n):
        s = False
        for j in range(0, n-i-1):
            c += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                s = True
        if not s:
            break
    case = "Best case O(n)" if c < n-1 else "Average/Worst case O(n^2)"
    print("Sorted array:", arr)
    print(f"Comparisons: {c}")
    print(f"Complexity: {case}")

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)