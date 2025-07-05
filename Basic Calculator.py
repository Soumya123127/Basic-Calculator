multi = ("+", "*")
single = ("-", "/", "%")

while True:
    op = input("Enter an operator (+, -, *, /, %): ").strip()

    if op in multi:
        num = input(f"Enter numbers to {'add' if op == '+' else 'multiply'}, separated by spaces: ")
        num_list = [float(n) for n in num.split()]

        if op == "+":
            result = sum(num_list)
            print(f"The sum is: {result}")
        else:
            result = 1
            for num in num_list:
                result *= num
            print(f"The product is: {result}")

    elif op in single:
        # Using a list to store two numbers
        pair = [float(input("Enter the first number: ")), float(input("Enter the second number: "))]

        if op == "-":
            result = pair[0] - pair[1]
            print(f"The difference is: {result}")
        elif op == "/":
            if pair[1] != 0:
                result = pair[0] / pair[1]
                print(f"The quotient is: {result}")
            else:
                print("Error: Division by zero is not allowed.")
        elif op == "%":
            result = pair[0] % pair[1]
            print(f"The remainder is: {result}")

    else:
        print("Invalid operator. Please enter one of +, -, *, /, %.")

    choice = input("Do you want to perform another calculation? (y/n): ").strip().lower()
    if choice != "y":
        print("Goodbye!")
        break
