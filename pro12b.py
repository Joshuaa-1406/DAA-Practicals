def binomial_dp(n,k):
    c = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                c[i][j] = 1
            else:
                c[i][j] = c[i - 1][j - 1] + c[i - 1][j]
    return c[n][k]

n, k = 5, 2
print(binomial_dp(n, k))
print("Dynamic programming complexity: O(n*k)Worst case")