# Muthee Francis
# rps.py
# Oct 18, 2015

# rock-paper-lizard game

# Truth table
'''
PLAYER 1    PLAYER 2    RESULT

Rock        Paper       Player 2
Rock        Scissors    Player 1
Rock        Rock        Tie

Paper       Rock        Player 1
Paper       Scissors    Player 2
Paper       Paper       Tie

Scissors    Scissors    Tie
Scissors    Rock        Player 2
Scissors    Paper       Player 1

'''
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
playerChoice()
