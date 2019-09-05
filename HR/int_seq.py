counter = 0
even_counter = 0
odd_counter = 0
cumulative_total = 0
user_input = 1
largest_num = 0
while user_input > 0:
    user_input = int(input("Enter an integer: "))
    if user_input > 0:
        cumulative_total += user_input
        print ("Cumulative total:", cumulative_total)
    if user_input > largest_num:
        largest_num = user_input
    if user_input >0:
        if user_input%2 == 0:
            even_counter += 1
        else:
            odd_counter +=1
    
    


if largest_num > 0:
    print ("Largest number:", largest_num)
    print ("Count of even numbers:", even_counter)
    print ("Count of odd numbers:", odd_counter)
