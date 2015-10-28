# Muthee Francis
# Homework 1
# Oct 6, 2015
# homework_1.py

# Exercises 1.2-1.4

        # Exercise 1.2
        
# function to print the board 
def drawTicTacBoard():
    print ('   |  | ')
    print " -------- "
    print ('   |  | ')
    print " -------- "    
    print ('   |  | ')
    
# call the function to draw the tic-tac-toe board
#drawTicTacBoard()

        # Exercise 1.3

# function that prints tic-tac-toe board by using variables
def tictactoeBoard():
    x,y,z = "   |  | "," -------- "," \n "
    print z+x+z + y+z + x+z + y+z + x+z
    
# call tic-tac-toe program
#tictactoeBoard()

        # Exercise 1.4
# function for input of user details
def userDetails():
    first_name = raw_input('Enter your first name : ')
    last_name = raw_input('Enter your last name : ')
    print "Enter your date of birth : "
    birth_month = raw_input('Month ? ')
    birth_day = raw_input('Day ? ')
    birth_year = raw_input('Year ? ')

    print first_name + ' ' +  last_name + " was born on " \
        + birth_month + ' ' +  birth_day + ", " + birth_year
    
#call function for user details
userDetails()
