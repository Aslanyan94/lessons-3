class A:

    def say_hi(self):
        print("Class A say hi")


class B(A):

    def hello(self):
        print("Hello")


b = B()
b.say_hi()
b.hello()

# b = B()
# b.say_hi()