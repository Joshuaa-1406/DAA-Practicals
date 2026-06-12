def matrix_mult(A,B):
    r1,c1,c2 = len(A),len(B[0]),len(B)
    result = [[0 for _ in range(c2)] for _ in range(r1)]
    ops = 0
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]
                ops += 1
    print(f"Number of operations: {ops}")
    return result

A = [[1,2],[3,4]]
B = [[1,2],[3,4]]
print(matrix_mult(A,B))
print("Complexity: O(n^3) Average case")