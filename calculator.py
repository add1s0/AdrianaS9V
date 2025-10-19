while True:
    print("\nMENU:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    choice = input("Choose an option between 1 & 5: ")

    if choice == "5" or choice.lower() == "exit":
        print("Goodbye!")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1" or choice.lower() == "add":
        print("Result:", num1 + num2)
    elif choice == "2" or choice.lower() == "subtract":
        print("Result:", num1 - num2)
    elif choice == "3" or choice.lower() == "multiply":
        print("Result:", num1 * num2)
    elif choice == "4" or choice.lower() == "divide":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed!")
    else:
        print("Invalid option! Please try again.")
