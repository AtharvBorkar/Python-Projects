try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("what kind of operation you want to perform?. Press + for addition\nPress - for subtraction\nPress * for multiplication\nPress / for division")

    o = input("Enter the operation: ")
    match o:
        case "+":
            print(f"The sum of {a} and {b} is: {a + b}")
        case "-":
            print(f"The difference between {a} and {b} is: {a - b}")
        case "*":
            print(f"The product of {a} and {b} is: {a * b}")
        case "/":
            if b != 0:
                print(f"The quotient of {a} divided by {b} is: {a / b}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation. Please enter a valid operation (+, -, *, /).")    

except Exception as e:
    print("Invalid input. Please enter valid integers.")