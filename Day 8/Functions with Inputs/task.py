def greet(name):
    print("Hello")
    print("Bye")
    print("See you later")
    print (f"Hi {name}")


greet("Irwan")
#Irwan is now going to be passed to name in the main function
#name is the parameter. Irwan is the argument


#function with 2 parameters
def greet_with(name, location):
    print(f"Hi {name}, how are you?")
    print(f"How is it in {location}?")


greet_with(location = "Singapore", name = "Irwan")