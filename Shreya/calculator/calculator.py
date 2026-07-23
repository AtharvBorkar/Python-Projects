try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print = int(input("what kind of operation you want to perform: press + for addition\npress - for subtraction\npress * for multiplication\npress / for division\n))   "))
    o = input("Enter operation:")
    match 0:
        case "+":
            print("Addition of a and b is:", a + b)
        case "-":
            print("Subtraction of a and b is:", a - b)
        case "*":
            print("Multiplication of a and b is:", a * b)
        case "/":
            print("Division of a and b is:", a / b)
        case _:
            print("Invalid operation")
except Exception as e:
    print("Enter a valid value of a and b.")
    