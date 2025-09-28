programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}


print(programming_dictionary["Function"])

programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)
print(programming_dictionary["Loop"])

#starting with empty dict, or to wipe existing dict
#empty_dictionary = {}


#Edit an item in a dict
programming_dictionary["Bug"] = " A moth in your computer"

#prints A moth in your computer
print(programming_dictionary["Bug"])

#loop through dictionary. This only prints the keys
for key in programming_dictionary:
    print(key)
    #retrive value using key
    print(programming_dictionary[key])




