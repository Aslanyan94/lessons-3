class Animal:
    def __init__(self, animal_type):
        self.type = animal_type

    def can_fly(self, name):
        if self.type == "bird" and name != "Penguin":
            return True
        return False

    def __str__(self):
        return self.type


class Bird(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__("bird")
        # Animal.__init__(self, "bird")

    def __str__(self):
        # self.can_fly(self.name)
        return f"{self.name} is {self.type}:\n\t Can flay {self.can_fly(self.name)}"

penguin = Bird("Penguin")
parrot = Bird("Parrot")

print(penguin)
print(parrot)

is_fly = penguin.can_fly("Cit")
is_fly = penguin.can_fly(penguin.name)
print(is_fly)

# print(penguin)
