class Person:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        if gender.lower() not in ("male", "female"):
            print("Error: Gender should be male or female")
        self.gender = gender

    def __str__(self):
        return f"{self.name} {self.surname} - " \
               f"{self.gender}, {self.age} years old"


narek = Person("Narek", "Aslanyan", 24, "Male")
print(narek)
