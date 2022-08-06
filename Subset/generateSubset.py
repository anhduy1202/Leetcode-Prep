def subset(arr):
    subsets = []
    subsets.append([])
    for num in arr:
        for i in range(len(subsets)):
            list1 = list(subsets[i])
            list1.append(num)
            subsets.append(list1)
    return subsets
print(subset([1,5,3]))
