from pprint import pprint


def function_a():
    function_var = 4234
    print("function_a")
    print("######## locals #########")
    print(locals())
    print("#########################")


function_a()
print(function_var)

a = 5
h = "fasdasfd"
ls = []
s = set([1, 4, 7])
print("########### globals #########")
pprint(globals())
print("#############################")
pprint(locals())


