class Family:
    def say_hi(self):
        print("Hi from family")


class Father(Family):
    pname = "Father"

    # def say_hi(self):
    #     print("Hi from Father")


class Mother(Family):
    pname = "Mother"

    def say_hi(self):
        print("Hi from mother")


class Child(Father, Mother):
    # super().say_hi()
    pass


ch = Child()
ch.say_hi()
