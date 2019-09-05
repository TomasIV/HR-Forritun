"""Design an algorithm that finds the maximum positive integer input by a user.  
   The user repeatedly inputs numbers until a negative value is entered.
 
Make sure that you write up the algorithm before starting to code.
Then implement the algorithm in Python. Put your algorithmic description as a comment in the program file."""
 
"""
Algorithm
1. take input from the user
2. max_int = 0
3. state that if the number is more than or equal to 0 a while loop will run
4. the while loop will compare user input to the max_int and if its bigger the input becomes the max_int
"""
run = True
max_int = 0
while run:
    user_input = int(input("Enter a number: "))
    if user_input >= 0:
        if user_input > max_int:
            max_int = user_input
    else:
        run = False
print (max_int)