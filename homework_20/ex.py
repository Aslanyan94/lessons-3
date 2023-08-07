from pprint import pprint


def b():
    print("function b")


def a(text):
    print("function a")
    return text


c = 543
pprint(globals())
# print(a("fdsa"))
# a("fsda")
print(b)

value_c = globals()["c"]
print(value_c)

function = globals()["a"]
result_1 = function("ffff")
print(result_1)

result_2 = globals()["a"]("Hello")
print(result_2)
# print(function)
# a("aaaa")