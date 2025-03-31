# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

# Functions with more than one input

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
# greet_with("Anthony Scott", "St. Charles")
# reads the position so name will be first
# positional argument
# could use:
def greet_with(name, location):
    print(f"What is it like in {location}, {name}?")
greet_with(location="Saint Charles", name="Anthony")