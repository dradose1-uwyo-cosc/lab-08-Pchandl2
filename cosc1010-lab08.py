# Peyton Chandler
# UWYO COSC 1010
# 11/4/24
# Lab 08
# Lab Section: 11
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def checkifintorfloat(string_to_check):
    returnValue = False
    try:
        returnValue = int(string_to_check)
        return returnValue
    except ValueError:
        try:
            if string_to_check.count('.') == 1:
                returnValue = float(string_to_check)
                return returnValue
            else:
                return False
        except ValueError:
            return False
    #return returnValue
print(checkifintorfloat("3.141596"))
print(checkifintorfloat("abs"))
print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m,b, x_lower, x_upper):
    if not isinstance(x_lower, int) or not isinstance(x_upper, int):
        return False

    if x_lower > x_upper:
        return False

    y_values = []
    for x in range(x_lower, x_upper+1):
        y=m*x+b
        y_values.append(y)
    return y_values
while True:
    user_input = input("enter m,b, x_lower, and x_upper values or exit to exit: ")
    if user_input == "exit":
        break
    try:
        m,b, x_lower, x_upper = map(float, user_input.split())
        x_lower, x_upper = int(x_lower), int(x_upper)
        result = slope_intercept(m, b, x_lower, x_upper)
        print("y values: ",result)
    except ValueError:
        print("invalid input, try different values")

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null


def positive_squareroot(number):
    if number < 0:
        return "negative"
    return number ** 0.5

def quadratic_solver(a,b,c):
    discriminant = b**2 -4*a*c
    sqrt_discriminant = positive_squareroot(discriminant)
    
    if sqrt_discriminant == "negative":
        return "nonreal solutions"
    
    x1 = (-b + sqrt_discriminant) / (2*a)
    x2 = (-b - sqrt_discriminant) / (2*a)
    return x1, x2
while True:
    try:
        a = float(input("Enter coefficient for a: "))
        b = float(input("Enter coefficient for b: "))
        c = float(input("Enter coefficient for c: "))

        if a == 0:
            print("coefficient a cannot be zero")
            continue

        x1, x2 = quadratic_solver(a,b,c)

        if x1 or x2 is not None:
            print(f"the solutions are: root 1 = {x1}, and root 2 = {x2}")
        else:
            print("No real solutions")
        break
    except ValueError:
        print("enter valid numbers")

    