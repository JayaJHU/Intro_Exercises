"""
Define a function that counts elements the elements in a list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
"""

"""
Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
"""

"""
Write a function translate() that encrypts a phrase into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun") should return the string "tothohisos isos fofunon".
"""

"""
Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
    Define a third function that processes (multiply, addition, factorial, etc) the returned outputs of the sum() and multiply() function
"""

"""
Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I".
"""

"""
Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.

"""

"""
 This function sequence below outputs a 2x2 grid:
 
 
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

Write a function that draws a similar grid with four rows and four columns.

Take it further: format each square with a unique number using functions

"""

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print '+ - - - -',

def print_post():
    print '|        ',

def print_beams():
    do_twice(print_beam)
    print '+'

def print_posts():
    do_twice(print_post)
    print '|'

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()
