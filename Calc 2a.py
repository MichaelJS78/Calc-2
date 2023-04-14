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

print('Welcome to Basic Calculator')

# Have reconfigured program to start with operation menu
while True:

    print("Select operation 1-Division, 2-Multiplication, 3-Addition, 4-Subtraction, 5-Quit")

    try:
        operation = int(input("Choose operation 1/2/3/4/5: "))
        if operation < 1 or operation > 5:
            print('Number not valid. Please try again')
            continue
        elif operation == 5:
            print('Thank you for using Basic Calculator')
            break
    except ValueError:
        print('Please enter a number between 1 and 5')
        continue

    while True:
        try:
            value1 = float(input ('Enter 1st number: '))
            while True:
                try:
                    value2 = float(input ('Enter second number: '))
                    break
                except ValueError:
                    print('Please enter a numerical value')
                    continue
        except ValueError:
            print('Please enter a numerical value')
            continue

        if operation == 1:
            print(value1, "/", value2, "=", divide(value1, value2))

        elif operation == 2:
            print(value1, "*", value2, "=", multiplication(value1, value2))
        elif operation == 3:
            print(value1, "+", value2, "=", addition(value1, value2))
        elif operation == 4:
            print(value1, "-", value2, "=", subtraction(value1, value2))

        print('Thank you')
        break


