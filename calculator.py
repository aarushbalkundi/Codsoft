def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x/y


while 1:   
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print('''Select operation:)
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit''')

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        print("Result:", num1+num2)
    elif choice == '2':
        print("Result:", num1-num2)
    elif choice == '3':
        print("Result:", num1*num2)
    elif choice == '4':
        print("Result:", num1/num2)
    else:
        exit()