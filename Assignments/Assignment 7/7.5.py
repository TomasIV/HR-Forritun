"""
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward, such as madam or racecar.
Sentence-length palindromes may be
written when allowances are made for adjustments to capital letters, punctuation, and word dividers, such as "
", "Was it a car or a cat I saw?" or "No 'x' in Nixon".

Write a function that takes a string as an argument and returns True if the string is a palindrome and False otherwise.
Also write code that calls the function with the input as an argument and prints out the appropriate message.

Example input/output:

 

Enter a string: No 'x' in Nixon.
"No 'x' in Nixon." is a palindrome.

Enter a string: blabla
"blabla" is not a palindrome.
"""
# palindrome function definition goes here
def is_palindrome(a_str):
    a_str = a_str.casefold()
    rev_str = reversed(a_str)
    if list(a_str) == list(rev_str):
        return True
in_str = input("Enter a string: ")
is_str_palindrome = is_palindrome(in_str)
if is_str_palindrome:
    print (in_str, "is a palindrome.")
else:
    print (in_str, "is not a palindrome.")
# call the function and print out the appropriate message