
def a():
    def b():
        print("nested function b")
        return None
    print("function a")
    return b


def c():
    print("functino c")


def less_15(x):
    return x > 15
# print(a())


ls = [1, 20, 25, 12, 7]
filtered = list(filter(less_15, ls))
print(filtered)
