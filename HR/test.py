n = int(input("Enter the length of the sequence: ")) # Do not change this line
num_1 = 1
num_2 = 2
num_3 = 3
counter = 3
print (num1, num2, num3)
while counter <= n:
    sum = num_1 + num_2 + num_3
    print (sum)
    counter += 1
    num_1 = num_2
    num_2 = num_3
    num_3 = sum
