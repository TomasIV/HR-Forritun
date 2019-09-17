"""
Write a function named count_case that takes a string as an argument and returns 
the count of upper case and lower case characters in the string (in that order). 

Also write a statement that calls the function with the given input as an argument.

Example input/output:

Enter a string: However, Marie found the best solution.
Upper case count:  2
Lower case count:  30
"""
def count_case(string):
    count1 = 0
    count2 = 0
    for i in string:
        if (i.isupper()):
            count1 += 1
        elif (i.islower()):
            count2 += 1
    return (count1, count2)

user_input = input("Enter a string: ")

# Call the function here
upper, lower = count_case(user_input)

print("Upper case count: ", upper)
print("Lower case count: ", lower)