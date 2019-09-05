"""
Algorithm
for  the sequence 1, 2, 3, 6, 11, 20, 37.
the algorithm for this sequence is to take the first 3 numbers and the sum of those
number will become the fourth number, 
so to get the fifth number you take the second, third and fourth number to and the sum
will be the fifth number (2+3+6 = 11)
so the algorith will be num_1 num_2 and num_3
and the sum of those is the new num
num_1 will become num _2
num_2 will become num_3
and num_3 will become the sum of num_1, num_2 and num_3
then print the sum
"""

n = int(input("Enter the length of the sequence: ")) # Do not change this line
num_1 = 1
num_2 = 2
num_3 = 3
counter = 3
while counter <= n:
    sum = num_1 + num_2 + num_3
    print (sum)
    counter += 1
    num_1 = num_2
    num_2 = num_3
    num_3 = sum
    