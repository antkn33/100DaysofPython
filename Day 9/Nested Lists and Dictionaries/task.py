
# {
#     Key: [List], #list as a value fo the key
#     Key2: {Dictionary} #Dictionary as avalue for key
# }

# Nested List

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

#Print just "Lille"
#print(travel_log["France"][1])

#nested or 2D List

nested_list = ["A", "B", ["C", "D"]]

#Print out letter "D"
# my solution:
#print(nested_list[-1][-1])

#instructor:
#print(nested_list[2][1])
#the [C,D] list in the 2nd item

# dictionary in another dictionary
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

#access stuttggart
#solve process
print(travel_log["Germany"])
print(travel_log["Germany"]["cities_visited"])
print(travel_log["Germany"]["cities_visited"][2])

