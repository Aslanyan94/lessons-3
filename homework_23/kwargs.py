def printer(*args, **kwargs):
    print("####### In printer function #########")
    print(kwargs)
    print(args)
    print("######################################")



printer(a=7, b=8)
printer(b=20, a=543, c=27)

info = dict(name="Arayik", age=18)
printer(**info)
output = "name: {name}\t\tage: {age}".format(**info)
print(output)

printer(1, 2, 4, "hi", hi="hello", name="ACA")

dt = dict(end="\tWow\nhi", sep="##yuhoo##")

print(2, 3, 4, **dt)