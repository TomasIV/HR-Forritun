"""
Write a function named find_min that takes two numbers as arguments and returns the minimum of the two.
Also write a statement that calls the function using the given input as arguments.
"""
def find_min(x, y):
    if x > y:
        return y
    else:
        return x
# find_min function definition goes here

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
    
# Call the function here
minimum = find_min(first, second)
print("Minimum: ", minimum)