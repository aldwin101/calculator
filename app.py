import addition
import division
import multiplication
import subtraction

try:
    print("1. Addition \n2. Division \n3. Multiplication \n4. Subtraction ")
    selection = int(input('Select operation above using the number key: '))

    num1 = int(input('Enter first number: \n'))
    num2 = int(input('Enter second number: \n'))

    if selection == 1:
        print(addition.add_numbers(num1, num2))
    elif selection == 2:
        print(division.divide_numbers(num1, num2))
    elif selection == 3:
        print(multiplication.multiply_numbers(num1, num2))
    elif selection == 4:
        print(subtraction.subtract_numbers(num1, num2))
    else:
        print("Invalid entry. Please try again!")
except ValueError:
    print("Invalid value. Please try again!")
