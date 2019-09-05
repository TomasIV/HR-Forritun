"""
Algorithm
1. max_int = 0
2. make a while loop
3. take an input from the user
4. state that if the number is more than or equal to 0 and if the user input is more than the max_int,
   max_int becomes the number input by the user
5. else stop the loop and print the max_int
"""
run = True
max_int = 0
while run:
    num_int = int(input("Input a number: "))
    if num_int >= 0:
        if num_int > max_int:
            max_int = num_int
    else:
        run = False
<<<<<<< HEAD
print ("The maximum is", max_int)
=======
print ("The maximum is", max_int)
>>>>>>> f22b50a1a36d22e1bb261a454871a7dec68222a4
