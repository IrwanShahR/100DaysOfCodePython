print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 12
        print("The ticker price is $5.")
    elif age <= 18:
        bill = 7
        print("The ticker price is $7.")
    else:
        bill = 12
        print("The ticker price is $12.")


    photo = input("Do you want a photo? Type Y/N ")
    if photo == "Y":
        bill = bill +3

    print(f"Your total bill is ${bill}.")

else:
    print("Sorry you have to grow taller before you can ride.")
