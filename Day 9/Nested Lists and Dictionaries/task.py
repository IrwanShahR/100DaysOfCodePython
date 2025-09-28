travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

#print Lille
print(travel_log["France"])
print(travel_log["France"][1])


nested_list = ["A", "B", ["C", "D"]]
#print C
print(nested_list)
print(nested_list[2][0])

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

#print Stuttgart
print(travel_log["Germany"]["cities_visited"][2])
#prints total visits to France
print(travel_log["France"]["total_visits"])