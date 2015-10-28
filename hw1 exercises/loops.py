# Muthee Francis
# loops.py
# Oct 18, 2015

# Exercise 2.2

# imports
from __future__ import division

# part 1 ( A program that prints decimals)
def decimalEquivalents():
    my_numbers = range(2,11)
    #round the decimals to two decimal places and print 
    for x in my_numbers:
        print round( (1/x), 2)
        
# Part 2 (A program that prompts for a number and loops to zero)
def loopInput():
    user_number = raw_input ('Please enter a number : ')
    try:
        val = int(user_number)
        if val < 0 :
            print 'please enter a positive number'
        elif val > 50 :
            print 'The number is too big, enter a small number'
        else:
            print str(val) + '\n'
            while (val):
                val = val - 1
                print (val)
                print ''
    except ValueError:
        print('please enter a number')

# part 3 (A program that calculates exponentials)
def calculateExponent():
    try:
        base = int(raw_input('Please enter a base : '))
        expo = int(raw_input('Please enter an exponent : '))
        for i in range(0, expo):
            print (base ** expo)
            expo = expo - 1
            print (base ** expo)
    except ValueError:
        print 'Please enter a number'
        
# Part 4 (program that lets the user enter an even number)
def evenNumber():
    try:
        while True:
            user_number =float(raw_input('Please a number divisible by two : '))
            print type (user_number)
            if (user_number % 2) != 0 :
                print 'Sorry !!! Please try again'
            else:
                print 'Congratulations !!! You entered a number divisible by two'
                break
    except ValueError:
        print 'Please enter a number'
        
#function calls
#decimalEquivalents()
#loopInput()
calculateExponent()
#evenNumber()   

