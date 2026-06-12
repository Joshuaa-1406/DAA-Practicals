def insertion_sort(arr):
    n,c,s = len(arr),0,0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            c += 1
            s += 1
        arr[j + 1] = key

    print("Sorted array:", arr)
    print(f"Comparisons:{c} \nSwaps: {s}")
    print("Complexity: O(n^2) Average case")

arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)