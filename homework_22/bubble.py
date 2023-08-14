def bubble_sort(array):
    k = 0
    for i in range(len(array)):
        is_swapped = False
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_swapped = True
            k += 1
            print(i, array)
        if not is_swapped:
            break
    print(k)
    return array


# ls = [5, 1, 4, 2, 8]
ls = [2, 1, 4, 8, 10]

sorted_ls = bubble_sort(ls)
print("sorted ls =", sorted_ls)