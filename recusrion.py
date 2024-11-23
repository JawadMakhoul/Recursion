def fibonacci(n):
    if n <= 0:
        return 0  # Base case: F(0) = 0
    elif n == 1:
        return 1  # Base case: F(1) = 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive call

# Example Input
print(fibonacci(6))  # Expected Output: 8


