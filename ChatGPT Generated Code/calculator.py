def calculator():
    while True:
        print("Select operation.")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter choice(1/2/3/4/5): ")
        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                print(num1, "+", num2, "=", num1 + num2)
            elif choice == '2':
                print(num1, "-", num2, "=", num1 - num2)
            elif choice == '3':
                print(num1, "*", num2, "=", num1 * num2)
            elif choice == '4':
                if num2 == 0:
                    print("Cannot divide by zero!")
                else:
                    print(num1, "/", num2, "=", num1 / num2)
            elif choice == '5':
                break
        else:
            print("Invalid Input")


calculator()

"""
This code defines a function called "calculator()". The function runs in an infinite loop until the user selects option 5 (Exit).

Inside the loop, the script first prints out the available operations (1. Add, 2. Subtract, 3. Multiply, 4. Divide, 5. Exit) and prompts the user to make a choice by entering a number from 1 to 5.

It then checks if the input is valid (if it's in the list ['1', '2', '3', '4', '5']), if it is, it prompts the user to enter two numbers (num1 and num2) and performs the corresponding operation based on the user's choice. If the choice is 4 (Divide), it checks if num2 is equal to 0 and if it is, it prints "Cannot divide by zero!" and continues the loop. If num2 is not equal to 0, it performs the division and prints the result.

If the user's choice is 5, the script breaks out of the loop and the function ends. If the input is invalid, it prints "Invalid Input" and continues the loop.

The script then calls the calculator() function at the end, to start the program.
"""
