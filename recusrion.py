def fibonacci(n):
    if n <= 0:
        return 0  # Base case: F(0) = 0
    elif n == 1:
        return 1  # Base case: F(1) = 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive call

# Example Input
print(fibonacci(6))  # Expected Output: 8



def find_subsets(arr):
    subsets = []  # Initialize an empty list to store subsets
    subsets.append([])  # Add the empty subset

    for i in arr:
        # Add each element to the existing subsets
        new_subsets = [subset + [i] for subset in subsets]
        subsets.extend(new_subsets)  # Extend the subsets with the new subsets

    return subsets  # Return the list of subsets

# Example usage
print(find_subsets([1, 2]))