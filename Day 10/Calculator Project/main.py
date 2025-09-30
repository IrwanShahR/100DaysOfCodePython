def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    continue_calculating = True
    num1 = float(input("What's the first number?: "))
    for i in operations:
        print(i)
    while continue_calculating:
        input_operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation = operations[input_operation]
        answer = (calculation(num1, num2))
        print(f"{num1} {input_operation} {num2}","=", f"{answer}")



        yes_no = input(f"Type y to continue calculating with {answer}, or type n to start a new calculation: ")
        if yes_no == "y":
            num1 = answer
            for i in operations:
                print(i)
        else:
            continue_calculating = False
            print("\n" * 20)
            calculator()


calculator()

