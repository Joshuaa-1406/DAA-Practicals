def factorial_nr(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

n = int(input("Enter a number: "))
print(f"Factorial of {n} is {factorial_nr(n)}")
print("Complexity: O(n) Average case")
