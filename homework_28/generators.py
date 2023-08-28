import random


def generate_number(start, end):
    for i in range(5, 100):
        yield i


gen_numbers = generate_number(3, 6)
while True:
    # print(gen_numbers)
    # print(next(gen_numbers))
    # print(next(gen_numbers))
    # print(next(gen_numbers))
    try:
        print(next(gen_numbers))
    except StopIteration:
        print("Value not found")
        break
# numbers = (i for i in range(5, 100))

# # print(numbers)
# # print(type(numbers))
# iter_numbers = iter(numbers)
# print(iter_numbers)
# print(next(iter_numbers))
# print(next(iter_numbers))
# print(next(iter_numbers))
# print(next(iter_numbers))
# print(next(iter_numbers))
# print(next(iter_numbers))
# print(next(iter_numbers))
# print(next(iter_numbers))
# print(next(iter_numbers))


