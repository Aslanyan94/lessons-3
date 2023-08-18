
class Fruit:

    SORT = "bla"

    def __init__(self, name, color):
        self.name = name
        self.fruit_color = color

    def description(self):
        return f"Fruit {self.name} has color {self.fruit_color}"


golden = Fruit("apple", "Yellow")

org = Fruit("orange", "Orange")


text = "hello world"
text.split()
print(golden.name)
print(org.name)


print(golden.description())
print(org.description())

print(golden.SORT)
print(org.SORT)