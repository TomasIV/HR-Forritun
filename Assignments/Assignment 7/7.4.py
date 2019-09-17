"""
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Write a function named is_prime that takes an integer argument and returns True if the number is prime and False otherwise.
(Assume that the argument is an integer greater than 1, i.e. no need to check for erroneous input.)

Also write code that calls the function and prints out a message saying that the given number is a prime or not.

Example input/output:
Input an integer greater than 1: 7
7 is a prime

Input an integer greater than 1: 6
6 is not a prime
"""
# is_prime function definition goes here
def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return
            else:
                return (True)
    
num = int(input("Input an integer greater than 1: "))
num_is_prime = is_prime(num)
if num_is_prime:
    print (num, "is a prime")
else:
    print (num, "is not a prime")
# Call the function here and print out the appropriate message