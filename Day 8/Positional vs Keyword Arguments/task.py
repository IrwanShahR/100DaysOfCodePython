# Functions with input

#def greet_with_name(name):
 #   print(f"Hello {name}")
  #  print(f"How do you do {name}?")


#greet_with_name("Jack Bauer")


def calculate_love_score(name1, name2):
    combine = (name1 + name2).upper()
    count1 = 0
    for char in combine:
        if char == "T":
            count1  += 1
        elif char == "R":
            count1 += 1
        elif char == "U":
            count1 += 1
        elif char == "E":
            count1 += 1

    count2 = 0
    for char in combine:
        if char == "L":
            count2  += 1
        elif char == "O":
            count2 += 1
        elif char == "V":
            count2 += 1
        elif char == "E":
            count2 += 1

    print(str(count1) + str(count2))


calculate_love_score("Angela Yu", "Jack Bauer")