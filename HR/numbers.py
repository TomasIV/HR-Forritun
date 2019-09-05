"""Finds and prints all positive two digit numbers whose square of the sum of its digits is equal to the number.
Finds and prints all positive numbers < 100 with exactly 10 divisors. 
Each number, fulfilling the above conditions, found by the program is printed out in a separate line."""
num = 10
while num < 100:
    sum_num = 0
    first_num = num // 10
    second_num = num % 10
    num += 1
print (sum_num)