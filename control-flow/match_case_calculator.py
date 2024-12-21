firstNumber=int(input("Enter the first number: "))
secondNumber=int(input("Enter the second number: "))
operation=input("Choose the operation (+, -, *, /): ")

match operation:
    case '+':
        print(f" The result is {firstNumber+secondNumber}")
    case '-':
        print(f"The result is {firstNumber-secondNumber}")
    case '*':
        print(f"The result is {firstNumber*secondNumber}")
    case '/':
        if secondNumber != 0:
            print(f"The result is {firstNumber/secondNumber}")
        else:
            print("Cannot divide by zero")