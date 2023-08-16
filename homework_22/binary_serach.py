def binary_search(numbers_ls, search):
    start = 0
    end = len(numbers_ls)

    while start < end:
        mid = (start + end) // 2
        if search == numbers_ls[mid]:
            return mid

        elif search < numbers_ls[mid]:
            end = mid
        elif search > numbers_ls[mid]:
            start = mid + 1
            # 4 6


numbers = [1, 2, 3, 5, 8, 9, 9, 11]
search_number = 9

index = binary_search(numbers, search_number)
print("Index:", index)

