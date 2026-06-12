def factorial_r(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_r(n - 1)

    # OR use This single line code.
    # return 1 if n<=1 else n*factorial_r(n-1)

n = int(input("Enter a number: "))
print(f"Factorial of {n} is {factorial_r(n)}")
print("Complexity: O(n) Average case")