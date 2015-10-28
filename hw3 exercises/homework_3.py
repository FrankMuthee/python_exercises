# Muthee Francis
# hw3
# homework_3.py
# Oct 18, 2015

# Exercises 5.1 - 5.5
import math
import fileinput
import os

# Exercise 5.1 (Finding Bugs)
'''
1) b is parsed but its not defined
   Should have been defined first.

2) neg_b variable is assigned to num but neither of them
   is defined with a value . Should first be assigned

3 function negate and large_num will throw an exception on
  passing a string . 
  
'''

# Exercise 5.2 (Mutability)
'''
 Mutable - Objects whose value can be changed once they are
 created. Eg list, dictionaries

 Immutable - Objects whose value cannot be changed once they
 are created. Eg tuple
'''

# Exercise 5.3 (Collision detection of balls)
def ball_collide(ball1, ball2):
        ball1_x, ball1_y, ball1_r = ball1[0], ball1[1], ball1[2]
        ball2_x, ball2_y, ball2_r = ball2[0], ball2[1], ball2[2]
        # Distance between any given two balls (applying maths formula)
        square_distance =((ball2_x - ball1_x ) ** 2 ) + ((ball2_y-ball1_y)**2)
        distance = math.sqrt(square_distance)
        radii_sum = ball1_r + ball2_r
        
        if distance <= radii_sum :
            return True
        else:
            return False

# printing output of a function call
# print ball_collide((0, 0, 1), (3, 3, 1)) 
# print ball_collide((5, 5, 2), (2, 8, 3)) 
# print ball_collide((7, 8, 2), (4, 4, 3)) 

# Exercise 5.4 (Introduction to dictionaries)
        
#global dict
class_dict = {'SMA103':'Algebra', 'UCU100':'Comm Skills'}

def add_class(class_num, desc, class_dict):
        class_dict.update({class_num:desc})
        print class_dict

# Example of adding a class
# add_class('SCT402', 'Quality Assurance', class_dict)

def print_classes(course, class_dict):
    try:
        if class_dict[course]:
            print class_dict[course]
    except KeyError:
        print 'No course ' +course+ ' classes taken'
             
# Example of printing
#print_classes('SMA103', class_dict) # prints course Algebra
#print_classes('SMA102', class_dict) # prints course not taken

# Exercises (Address Book)
def buildAddrBook(fileName):
    if os.path.isfile(fileName):
       my_dict = {}        
       my_file = open(fileName, 'r')
       for line in my_file:
           split_line = line.split(',')
           f_names, l_names, phone_n, address = \
                                                split_line[0],split_line[1],\
                                                split_line[2], split_line[3]
           my_dict.update({f_names +','+l_names : [phone_n+','+address]})
           #print my_dict
           #return my_dict
    else:
        print 'File does not exist'
        
    return my_dict

#call function                
addrBook = buildAddrBook('rawAddresses.csv')
#print addrBook

def changeEntry(addrBook, entry,field,new_value):
    addrBook =  buildAddrBook('rawAddresses.csv')
    
    for k, v in addrBook.iteritems():
        if k == entry and field == 'name':
            addrBook[new_value] =addrBook.pop(entry)
            return addrBook
        if k == entry and field == 'phoneNumber':
            for item in addrBook[k]:
                new_item = item.split(',')
                new_item[0] = new_value
                addrBook[k] = new_item[0]+','+new_item[1]
                return addrBook
        if k == entry and field == 'emailAddress':
            for item in addrBook[k]:
                new_item = item.split(',')
                new_item[1] = new_value
                addrBook[k] = new_item[0]+','+new_item[1]
                return addrBook
                

#testcase for new values everytimes
#if it returns
print ''
print changeEntry(addrBook, 'Manchu,Foo','name','Munialo,Christopher')
print ''
print changeEntry(addrBook, 'Nadal,Rafael','phoneNumber','(878) 878-3933')
print ''
print changeEntry(addrBook, 'Mellark,Peeta','emailAddress','melaka@gmail.com')
