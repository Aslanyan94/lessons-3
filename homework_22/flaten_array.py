def flatten_array(array: list)->list:
    result = []
    global i
    i += 1
    global j

    print(i, array)

    for item in array:
        if isinstance(item, (list, tuple)):
            result.extend(flatten_array(item))
        else:
            print(f"J: {j}\t\t item: {item}")
            j += 1
            result.append(item)
    return result


i = 0
j = 1
# call 1 [1, 2,
#     call 2 [ 3, 4, "5"].extend([6, 20, 20]) -> [3, 4, 5, 6, 20, 20]
#         call 3 [6].extend([20, 20]), -> [6, 20, 20]
#             call 4 [ 20, 20 -> [20, 20]

nested_ls = [1, 2, [3, 4, "5", [6, (20, 20), 7], 8], 9]
ls = flatten_array(nested_ls)
print(ls)