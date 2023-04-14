# Python Program to Make a Simple Calculator
# Debugged version of original code

def multiplication(num1, num2):
    return num1 * num2


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


while True:
    value1 = int(input("Enter 1st number: "))
    value2 = int(input("Enter 2nd number: "))

# Have included option to quit
    print("Select operation 1-Division, 2-Multiplication, 3-Addition, 4-Subtraction, 5-Quit")

# Exception handling added for operation
    try:
        operation = int(input("Choose operation 1/2/3/4/5: "))
        if operation < 1 or operation > 5:
            print('Number not valid. Please try again')
            continue
        elif operation == 5:
            print(quit())
            break
    except ValueError:
        print('Please enter a number between 1 and 5')
        continue


    if operation == 1:
        print(value1, "/", value2, "=", divide(value1, value2))

    elif operation == 2:
        print(value1, "*", value2, "=", multiplication(value1, value2))
    elif operation == 3:
        print(value1, "+", value2, "=", addition(value1, value2))
    elif operation == 4:
        print(value1, "-", value2, "=", subtraction(value1, value2))

