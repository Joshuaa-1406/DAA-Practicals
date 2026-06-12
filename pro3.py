def selection_sort(arr):
    n,c,s = len(arr),0,0
    for i in range(n-1):
        m = i
        for j in range(i+1,n):
            c += 1
            if arr[j] < arr[m]:
                m = j
        if m != i:
            arr[i],arr[m] = arr[m],arr[i]
            s += 1

    print("Sorted array:", arr)
    print(f"Comparisons:{c} \nSwaps: {s}")
    print("Complexity: O(n^2) Average case")

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
