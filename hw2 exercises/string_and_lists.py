# Muthee Francis
# hw2
# strings_and_lists.py
# Oct 18, 2015

# Exercise 4.1 working with lists

import numpy as np

def sum_all(number_list):
    return sum(number_list)


#test cases
#print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
#print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])

def cumulative_sum(number_list):
    return np.cumsum(number_list)

#test cases
#print cumulative_sum([1,2,3])
#print cumulative_sum([4,5,6,7])

def pig_latin(my_word):
    vowels =  [ 'a', 'e', 'i', 'o', 'u' ]
    if my_word[0] in vowels:
       my_word =  my_word+'hay'
    else:
        my_word = my_word.replace(my_word[0],'')+my_word[0]+'ay'
    return my_word

#test cases
#print pig_latin('boot')
#print pig_latin('image')
        
