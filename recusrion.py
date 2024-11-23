def fibonacci(n):
    if n <= 0:
        return 0  
    elif n == 1:
        return 1  
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # main line in the code ( how the rec works )


print(fibonacci(6))  

#####################################################################

def findSubsets(arr):
    subsets = []  # list to store subsets
    subsets.append([])  

    for i in arr:
        new_subsets = [subset + [i] for subset in subsets]
        subsets.extend(new_subsets)  
    return subsets 


print(findSubsets([1, 2]))