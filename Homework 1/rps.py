# conditionals
# Exercise 2.1 Rock, Paper, Scissors

def newLine():
    print


print ('Select one of the following: Rock, Paper or Scissors')
newLine()
player_1 = raw_input('Player 1 Type your selection: ')
player_2 = raw_input('Player 2 Type your selection: ')
newLine()

if player_1 == 'Rock' or player_1 == 'Paper' or player_1 == 'Scissors':
    if player_2 == 'Rock' or player_2 == 'Paper' or player_2 == 'Scissors':
        
        if player_1 == 'Rock' and player_2 == 'Scissors':
            print 'Player 1 wins.'
        elif player_1 == 'Rock' and player_2 == 'Paper':
            print 'Player 2 wins.'
        elif player_1 == 'Rock' and player_2 == 'Rock':
            print 'Result is a draw.'
            
        elif player_1 == 'Paper' and player_2 == 'Scissors':
            print 'Player 2 wins.'
        elif player_1 == 'Paper' and player_2 == 'Rock':
            print 'Player 1 wins.'
        elif player_1 == 'Paper' and player_2 == 'Paper':
            print 'Result is a draw.'

        elif player_1 == 'Scissors' and player_2 == 'Paper':
            print 'Player 1 wins.'
        elif player_1 == 'Scissors' and player_2 == 'Rock':
            print 'Player 2 wins.'
        else:
            print 'Result is a draw.'
        
else:
    print 'This is not a valid object selection'



####################  Results ###########################

Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Select one of the following: Rock, Paper or Scissors

Player 1 Type your selection: Rock
Player 2 Type your selection: Paper

Player 2 wins.

################## Results ####################

Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Select one of the following: Rock, Paper or Scissors

Player 1 Type your selection: Paper
Player 2 Type your selection: Paper

Result is a draw.
>>> 

