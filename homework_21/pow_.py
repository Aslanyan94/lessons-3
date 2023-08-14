def pow_(a, n):
    if a == 1:
        return 1
    if a == 0:
        return 0
    if n == 0:
        return 1
    # 5 ** 4, 5 * (5 ** 3)
    return a * pow_(a, n - 1)
