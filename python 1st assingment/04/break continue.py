terminate_program = False
while not terminate_program:
    number1 = int(input("Please enter a number: "))
    number2 = int(input("Please enter another number: "))

    while True:
        operation = input("Please enter add/sub or quit to exit: ")
        if operation == "quit":
            terminate_program = True
            break
        if operation not in ["add", "sub"]:
            print("Unknown operation!")
            continue
        if operation == "add":
            print("Result is", number1 + number2)
            break
        if operation == "sub":
            print("Result is", number1 - number2)
            break