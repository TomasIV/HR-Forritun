# Your function definition goes here
def fibo(x):
    n1 = 0
    n2 = 1
    counter = 0
    if x == 1:
        return 1
    elif x > 1:
        printer = ""
        while counter < x:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            str_n1 = str(n1)
            printer += str_n1 + " "
            counter += 1
        return printer

n = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here    
is_n_fibo = fibo(n)
print (is_n_fibo)