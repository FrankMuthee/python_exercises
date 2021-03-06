# Muthee Francis
# hw2
# nims.py
# Oct 18, 2015

import random
from random import randint
from time import sleep
import os

#globals
picked_stones = 0
pile = 0

#This function initialises the playing
def player(pil,max_stones,player):
   global picked_stones, pile    
   while True:
       stones = int(raw_input('\n '+player+' please enter the number of stones you want to pick : '))
       picked_stones = stones
       if picked_stones < 0:
           print '\nNegative numbers not allowed'
       elif picked_stones > max_stones:
           print '\n You can`t collect more stones than allowed'
       elif picked_stones > 0 and picked_stones <=max_stones:
           pile -=picked_stones
           print '\n picked stones : '+str(picked_stones)
           print '\n remaining stones : '+str(pile)
           return pile, picked_stones
           break
       else:
           break

#function to define the game 
def start_game(pile, max_stones):
    player_1_name = raw_input('\n Please Enter Player One`s Name : ')
    player_2_name = raw_input('\n Please Enter Player Two`s Name : ')
    start_player = random.choice([player_1_name,player_2_name])
    print '\n Player ' +start_player+ ' will start the game .......... Loading ........'
    sleep(0.8)
    while True:
        if start_player == player_1_name:
            print '\n Its '+player_1_name+ ' turn to play !'
            player(pile, max_stones, player_1_name)
            pile -=picked_stones
            
            if pile > max_stones and pile > 0:
                player(pile, max_stones, player_2_name)
            elif pile > 0 and pile <= max_stones: 
                print '\n '+player_2_name + ' wins !!'
                break
             
        elif start_player == player_2_name:
            print '\n Its '+player_2_name + ' turn to play !'
            player(pile, max_stones, player_2_name)
            pile -=picked_stones
            if  pile > max_stones and pile > 0:
                player(pile, max_stones, player_1_name)
                pile -=picked_stones
            elif pile > 0 and pile <= max_stones:
                print '\n '+player_1_name + ' wins'
                break

#initialise
while True:
    print '\n               ---&&&& WELCOME TO THE GAME OF STONES [NIMS] &&&&--- \n'
    
    print '''
    This game involves two players who agree on number of stones to make up the pile
    and the maximum stones one is allowed to collect during his/her turn of playing
    The players take turn to player until the size of the pile is equal to or less than
    the maximum number of of stones that can be collected which is the condition to check
    the winner
    '''
    print '\n                 Game is loading .......................  '
    sleep(2)
    os.system('clear')
    pile = raw_input('\n Enter the number of stones that make up the pile: ')
    max_stones = raw_input('\n Enter the maximum stones you can pick from the pile: ')
    pile, max_stones = int(pile), int(max_stones)
    if max_stones > pile:
        print '\n Max stones cannot be greater than the pile'
    elif max_stones < pile:
        start_game(pile,max_stones)
        break
