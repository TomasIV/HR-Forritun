"""
Write a function that takes an integer as an argument and returns True if the number 
is within the range 1 to 555 (not inclusive, i.e. neither 1 nor 555 are in range).

Also write a statement that calls the function with the given input as an argument.

Example input/output:

Enter a number: 1
1 is outside the range!

Enter a number: 7
7 is in range.
"""
# The function definition goes here
def in_range(x):
    if (x > 1) and (x < 555):
        return (True)
    else:
        return

num = int(input("Enter a number: "))
if in_range(num) == True:
    print (num, "is in range.")
else:
    print (num, "is outside the range!")
# You call the function here