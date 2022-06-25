def quickSort(arr):
    if len(arr) > 1:
        pivot = arr.pop()
        lower_arr = []
        higher_arr = []
        for num in arr:
            if num > pivot:
                higher_arr.append(num)
            else:
                lower_arr.append(num)
        return quickSort(lower_arr) + [pivot] + quickSort(higher_arr)
    return arr

print(quickSort([9,7,1,2,6,5]))