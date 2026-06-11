def binomial_bf(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return binomial_bf(n - 1, k - 1) + binomial_bf(n - 1, k)

n, k = 5, 2
print(binomial_bf(n, k))
print("Brute force complexity: O(2^n)Worst case")