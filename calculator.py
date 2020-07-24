

while True:
    print("options")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'devide' to devide two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'quit' to quit two numbers")
    user_input = input(": ")
    
    if user_input == "quit":
        break
    elif user_input == "add":
        num1 = float(input("Enter a number;"))
        num2 = float(input("Enter a another number:"))
        result = str(num1 + num2)
        print("the answer is " + result)
    elif user_input == "subtract":
        num1 = float(input("Enter a number;"))
        num2 = float(input("Enter a another number:"))
        result = str(num1 - num2)
        print("the answer is " + result)
    elif user_input == "devide":
        num1 = float(input("Enter a number;"))
        num2 = float(input("Enter a another number:"))
        result = str(num1 / num2)
        print("the answer is " + result)
    elif user_input == "multiply":
        num1 = float(input("Enter a number;"))
        num2 = float(input("Enter a another number:"))
        result = str(num1 * num2)
        print("the answer is " + result)
        
    else:
        print("unknown input")
