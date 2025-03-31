'''
def my_function():
    return 3 * 2 # this return outputs the result of 3 * 2

output = my_function() # my_function is replaced with the output of return

print(output) # output will equal 6
'''
# capitalize names with title
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    # return replaces the function call with the output
    return (f" {formatted_f_name} {formatted_l_name}")
# give the function call a variable
formatted_string = format_name("anTHonY", "scOTt")
print(formatted_string)
# or:
# print(formatted_string = format_name("anTHonY", "scOTt"))






