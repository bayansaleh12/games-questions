# take the first number from user.
first_number = float(input("enter the first number:\t"))

# take the operation from the user.
operation = input("enter the operation (+, -, *, /):\t")

# take the second number from user.
second_number = float(input("enter the second number:\t"))


# create function to calculate the result.
def calculate(first_number, operation, second_number):
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    elif operation == '*':
        return first_number * second_number
    elif operation == '/':
        if second_number != 0:  # Avoid division by zero
            return first_number / second_number
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"


# print the result for the user
print(first_number, operation, second_number, f"= {calculate(first_number, operation, second_number)}")

