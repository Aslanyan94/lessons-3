def function(b):
    def second():
        nonlocal c
        c += 6
        print(c)
    a = 5
    # global c
    c = 5
    second()



    print("the value of variable c is ", c)
    print("locals: \n", locals())
    second()


def function_2():
    def sub_function():
        name = "Company"
        print(name)
    # name = "ACA"
    sub_function()


# name = "LLC"


c = 6

# print("Globals: \n", globals())
# print("Locals: \n", locals())
function("Hiiii")
# print(c)
# function_2()



for i in range(10):
    print(locals())
    c = i ** 2

print(i)
print(c)