# Name: Romeo Ekirapa
# Section:
# nims.py

##    '''
##    An interactive two-person game; also known as Stones.
##    @param pile: the number of stones in the pile to start
##    @param max_stones: the maximum number of stones you can take on one turn
##    '''

def play_nims(pile, max_stones):

    def move(x):
        return (x > 0) and (x <= max_stones) and (x <= pile)

    while pile > 0:
        print "There are", pile, " stones in the pile."
        p1 = 0
        while not move(p1):
            p1 = int(raw_input("Player 1's move: "))
            if not move(p1):
                print "pick stones between 1-5, pick stones contained in the pile"

        pile = pile - p1

        if pile == 0:
            print "Player 1 wins!!"
            break
        
        print "There are", pile, " stones in the pile."
        p2 = 0
        while not move(p2):
            p2 = int(raw_input("Player 2's move: "))
            if not move(p2):
                print "pick stones between 1-5, pick stones contained in the pile"

        pile = pile -p2

        if pile == 0:
            print "Player 2 wins!!"
            break
    print "Game over"
        

play_nims(20, 4)

############### Results ##############

Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
There are 20  stones in the pile.
Player 1's move: 6
pick stones between 1-5, pick stones contained in the pile
Player 1's move: 0
pick stones between 1-5, pick stones contained in the pile
Player 1's move: 5
There are 15  stones in the pile.
Player 2's move: 3
There are 12  stones in the pile.
Player 1's move: 5
There are 7  stones in the pile.
Player 2's move: 5
There are 2  stones in the pile.
Player 1's move: 5
pick stones between 1-5, pick stones contained in the pile
Player 1's move: 3
pick stones between 1-5, pick stones contained in the pile
Player 1's move: 2
Player 1 wins!!
Game over
>>> 
