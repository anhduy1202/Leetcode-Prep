def flattenListRecursion(nested):
    # If the list is empty, the function returns the list.
    if nested == []:
        return nested
     # Otherwise, use the function with the sublists as parameters
     # recursively until the entire list is flattened.
    if isinstance(nested[0], list):
        return flattenListRecursion(nested[0]) + flattenListRecursion(nested[1:])
    return nested[:1] + flattenListRecursion(nested[1:])

print(flattenListRecursion([1,[2,3,4]]))