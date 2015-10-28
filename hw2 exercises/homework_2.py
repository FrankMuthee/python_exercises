# Name: Muthee Francis
# Section : hw2
# homework_2.py
# Oct 18, 2015

# Exercise 3.1 [Rock paper scissors]
from __future__ import division
import math
import random
# function to determine winner
def determineWinner(player_one, player_two):
    if (player_one == 'rock' and player_two == 'paper'):
        print "Player 2 wins"
    elif (player_one == 'rock' and player_two == 'scissors'):
        print "Player 1 wins"
    elif (player_one == 'rock' and player_two == 'rock'):
        print "Its a tie"

    elif (player_one == 'paper' and player_two == 'rock'):
        print "Player 1 wins"
    elif (player_one == 'paper' and player_two == 'scissors'):
        print "Player 2 wins"
    elif (player_one == 'paper' and player_two == 'paper'):
        print "Its a tie"

    elif (player_one == 'scissors' and player_two == 'scissors'):
        print "Its a tie"
    elif (player_one == 'scissors' and player_two == 'rock'):
        print "Player 2 wins"
    elif (player_one == 'scissors' and player_two == 'paper'):
        print "Player 1 wins"

# function to prompt the game
def playerChoice():

    #loop the game once its run on until one decides to quit
    #This avoids re-running the rps.py file everytime the players want to play
    while True:
        print  "\n" + "-----@-- Welcome to rock-paper-scissor game session --@-----" + "\n"
        user_decision = raw_input ('Should we proceed [ Q for quit] ')
        if user_decision == 'Q':
            break
        else:
            choices = ['scissors','rock','paper']
            
            #loop until player_one user to enters an object defined in choices 
            while True:
                player_one = raw_input("Player 1 ? ")
                if player_one not in choices:
                    print "This is not a valid object selection"
                else:
                    break
                
            #loop until player_two user to enters an object defined in choices
            while True:
                player_two = raw_input("Player 2 ? ")
                if player_two not in choices:
                    print "This is not a valid object selection"
                else:
                    break
            #determine the winner by calling the function that determines the winner
            determineWinner(player_one , player_two)
#call function
#playerChoice()

# Exercise 3.2

def multadd():
    #angle_test
    first_value = (math.ceil(276/19))
    second_value = (2*(math.log(12))/(math.log(7)))
    ceiling_test = first_value + second_value
    angle_test = math.sin(math.pi/4) + (math.cos(math.pi/4)/2)
    
    return 'ceiling_test : ' + str(ceiling_test) + ' angle_test : ' + str(angle_test)

# test
#print multadd()

# Function yikes
def yikes(x):
    y = math.exp(-x)
    return (y * x) + (math.sqrt(1 - y))

# test
#print yikes(5) # prints 1.0303150673

def rand_divis_3():
    #a number between 0 - 100
    my_number = random.randint(0,100)
    if (my_number % 3) == 0:
        print my_number
        return True
    else:
        print my_number
        return False
#print rand_divis_3()

def roll_dice (sides_num,dice_num):
    for i in range(dice_num):
        print random.randrange(1, sides_num+1 )
        
    print "That`s all !"
    
roll_dice(6,4)
    
