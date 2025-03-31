
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
# print(programming_dictionary["Bug"]) #the key here is a string so use ""

#add entry
programming_dictionary["Loop"] = "doing something over and over"

#sometimes good to start with empty dictionary
empty_dictionary = {}

#wipe a dictionary
#programming_dictionary = {}

#edit an item in a dictionary
programming_dictionary["Bug"] = "new definition"

#Loop through a dictionary
for key in programming_dictionary:
    print(key) #will only print the key
    print(programming_dictionary[key]) #will print value