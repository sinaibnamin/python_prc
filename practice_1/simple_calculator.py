num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operator = input("Enter operator (+, -, *, /): ")

match operator:

    case "+":
        print("Result =", num1 + num2)

    case "-":
        print("Result =", num1 - num2)

    case "*":
        print("Result =", num1 * num2)

    case "/":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Division by zero is not allowed")

    case _:
        print("Invalid operator")