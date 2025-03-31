from art import logo
print(logo)


def add(n1, n2):
    return n1 + n2
# TODO: Write out
# the other 3 functions - subtract, multiply and divide.

def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

#my_favorite_operation = add
# stores function as a variable
# don't use () after it

# TODO: Add these 4 functions into a dictionary
# as the values. Keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    # leave off () so the function is STORED, not triggered
}

# TODO: Use the dictionary operations to perform
#  the calculations. Multiply 4 * 8 using the dictionary.

# print(operations["*"](4, 8))
continue_calculation = True
first_number = ""

while continue_calculation:
    if first_number == "":
        first_number = float(input("Type the first number: "))
    else:
        for key in operations:
            print(key)
        select_operation = input("Select which operation you want: ")
        second_number = float(input("Type the second number: "))

        total = operations[select_operation](first_number, second_number)
        print(f"{first_number} {select_operation} {second_number} = {total}")
        will_continue = input(f"Do you want to continue with {total}? y or n: ")
        if will_continue == "n":
            first_number = ""
        elif will_continue == "y":
            first_number = total










