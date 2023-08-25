class Parent:
    def __init__(self, name, age):
        self.pname = name
        self.page = age

    def info(self):
        return f"{self.pname} {self.page} years old"


class Child(Parent):
    def __init__(self, pname, page, name, surname, age):
        super().__init__(pname, page)
        self.name = name
        self.surname = surname
        self.age = age
        # Parent.__init__(self, pname, page)

    def __str__(self):
        return f"{self.name} {self.surname} is {self.age} years old.\n\t" \
               f"Parent: {self.info()}"


ch = Child("Ann", 50, "Vazgen", "Asatryan", 25)
print(ch)
