import sys


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("error")
        sys.exit(1)
    return a // b


def validate_number(str_number):
    pass
    # return int or float number


def is_validate_action(action: str, symbols: dict):
    # + * ...
    return action in symbols.keys()


def validate_input(expression, symbols):
    # validate splited expression
    # validate_number(...)
    # is_validate_action(...)
    ...
    pass


SYMBOLS = {
    "+": "add",
    "*": "multiply"
}

expression = input("Input expression: ")
# "5.7 + 6 jhlk" ["5.7", "+", "6"]

splited = expression.split()    # ["5.7", "+", "6"]
print("splited =", splited)

first_number = float(splited[0])
symbol = splited[1]
second_number = float(splited[-1])
print(f"first = {first_number}: action = {symbol} second = {second_number}")

function_str_name = SYMBOLS[symbol]
print("function_str_name =", function_str_name, type(function_str_name))

# equal add or multiply without quote
function_ref = globals()[function_str_name]
print(f"function ref = {function_ref}, function type = {type(function_ref)}")
print(f"function ref add = {add}, function type = {type(add)}")

# is equal add(first_number, second_number)
result = function_ref(first_number, second_number)
# result = add(first_number, second_number)

print(result)

