# Name: Romeo 
# Section:
# homework_2.py

##### Template for Homework 2, exercises 3.1-3.4  ######


# **********  Exercise 3.1 ********** 

# Define your rock paper scissors function here

def game(player_1, player_2):

    w1 = "player 1 wins"
    w2 = "player 2 wins"
    
    if player_1 == 'Rock' or player_1 == 'Paper' or player_1 == 'Scissors':
        if player_2 == 'Rock' or player_2 == 'Paper' or player_2 == 'Scissors':
        
            if player_1 == 'Rock' and player_2 == 'Scissors':
                return w1
            elif player_1 == 'Rock' and player_2 == 'Paper':
                return w2
            elif player_1 == 'Rock' and player_2 == 'Rock':
                return 'Player 1 and Player 2 draw.'
                
            elif player_1 == 'Paper' and player_2 == 'Scissors':
                return w2
            elif player_1 == 'Paper' and player_2 == 'Rock':
                return w1
            elif player_1 == 'Paper' and player_2 == 'Paper':
                return 'Player 1 and Player 2 draw.'

            elif player_1 == 'Scissors' and player_2 == 'Paper':
                return w1
            elif player_1 == 'Scissors' and player_2 == 'Rock':
                return w2
            else:
                return 'Player 1 and Player 2 draw.'
        
    else:
        return 'This is not a valid object selection'
    

# Test Cases for Exercise 3.1

result = game('Rock', 'Paper')
print "Result of game 1 is " + result

result = game('Paper', 'Rock')
print "Result of game 2 is " + result

result = game('Scissors', 'Scissors')
print "Result of game 3 is " + result

######### Results for Exercise 3.1  ##############

Result of game 1 is player 2 wins
Result of game 2 is player 1 wins
Result of game 3 is Player 1 and Player 2 draw.

# *********** Exercise 3.2 ***********
## 1 - multadd function

def multadd(a, b, c):
    return a * b + c

print "Result of multadd function is:  " + str(multadd(1, 2, 3))
print "Result of multadd function is:  " + str(multadd(3, 4, 5))
print "Result of multadd function is:  " + str(multadd(6, 7, 8))

######### Results for multadd function ##############

Result of multadd function is:  5
Result of multadd function is:  17
Result of multadd function is:  50


## 2 - Equations

import math
import random

a = 1
b = math.sin(math.pi/4)
c = math.cos(math.pi/4)/2

angle_test = multadd(a, b, c)

print "sin(pi/4) + cos(pi/4)/2 is: "
print angle_test

a = 1
b = math.ceil(279.0/19.0)
c = 2 * math.log(12, 7)

ceiling_test = multadd(a, b, c)

print "ceiling(276/19) + 2 log_7(12) is:"
print ceiling_test

######### Results for equations ##############

sin(pi/4) + cos(pi/4)/2 is: 
1.06066017178
ceiling(276/19) + 2 log_7(12) is:
17.5539788165

## 3 - yikes function

def yikes(x):
    a = 1
    b = x * math.exp(-x)
    c = math.sqrt(1 - math.exp(-x))
    return multadd(a, b, c)

# Test Cases

x = 5
print "yikes(5) =", yikes(x)

######### Results for yikes function ##############

yikes(5) = 1.0303150673

# ********** Exercise 3.3 **********

## 1 - rand_divis_3 function

def rand_divis_3():
    rand = random.randint(0, 100)
    if rand % 3 == 0:
        return "True"
    else:
        return "False"

# Test Cases

print rand_divis_3()
print rand_divis_3()
print rand_divis_3()

######### Results for rand_divis_3 function ##############

False
True
True

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has

def roll_dice(side, roll):
    for x in range(roll):
        rng = random.randint(1, side)
        print str(rng)
        x+1
    print "That's all!"

# Test Cases

roll_dice(6, 5)
roll_dice(6, 2)
roll_dice(6, 10)

######### Results for roll_dice function ##############

4
5
5
3
5
That's all!
1
3
That's all!
3
6
1
4
4
1
5
2
1
1
That's all!


