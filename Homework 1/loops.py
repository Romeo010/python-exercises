# Execercise 2.2

# 1
print ("program that prints out decimals from a range")
for x in range(2, 11):
    print float(1.0/x)

# 2
print ("program to countdown to zero")
count = input("Please enter a number: ")

if count >= 0:
    while count >= 0:
        print count
        count = count - 1
else:
    print ("Please enter a number equal or greater than 0")

# 3
print ("program to calculate exponentials")

base = input("Enter the base number: ")
exp = input("Enter the exponent number: ")

answer = 1

for i in range(exp):
    answer = base**exp

print str(answer)

# 4
print ("program to check if a number is a multiple of 2")
number_dual = input("Enter a number that is divisible by two: ")

while number_dual % 2 !=0:
    print ("Sorry the number you have entered is not divisible by two")
    number_dual = input("Enter a number that is divisible by two: ")

print ("Correct")
    



###################### Results ######################


Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
program that prints out decimals from a range
0.5
0.333333333333
0.25
0.2
0.166666666667
0.142857142857
0.125
0.111111111111
0.1
program to countdown to zero
Please enter a number: 4
4
3
2
1
0
program to calculate exponentials
Enter the base number: 4
Enter the exponent number: 2
16
program to check if a number is a multiple of 2
Enter a number that is divisible by two: 2
Correct
>>> 
