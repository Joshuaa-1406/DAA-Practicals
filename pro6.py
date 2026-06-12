def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])

    result,i,j = [],0,0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1
    return result + L[i:] + R[j:]

arr = [38, 27, 43, 3, 9, 82, 10]
print("Sorted array:", merge_sort(arr))
print("Complexity: O(n log n) Average case")
