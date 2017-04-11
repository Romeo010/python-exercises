# Name: Romeo Ekirapa
# Section:
# strings_and_lists.py

# **********  Exercise 4.1 **********

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

# Test cases
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])

################# Results #################

sum_all of [4, 3, 6] is: 13
sum_all of [1, 2, 3, 4] is: 10


def cumulative_sum(number_list):
    # number_list is a list of numbers
    cumulative = []
    total = 0
    for num in number_list:
        total = total + num
        cumulative.append(total)

    return cumulative


# Test Cases

print "cumulative_sum of [4, 3, 6] is:", cumulative_sum([4, 3, 6])
print "cumulative_sum of [1, 2, 3, 4] is:", cumulative_sum([1, 2, 3, 4])

################# Results #################

cumulative_sum of [4, 3, 6] is: [4, 7, 13]
cumulative_sum of [1, 2, 3, 4] is: [1, 3, 6, 10]

# **********  Exercise 4.2 **********

import sys

sentence = raw_input("Please enter a sentence: ")
vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
words =  sentence.split()

count = 0

def pig_latin(word):
    for i in range(len(word)):
       if word[i] in vowels:
         return i
    return -1

for word in words:
  vowel = pig_latin(word)

  sys.stdout.write(word[vowel:] + word[:vowel] + "ay" + " ")
  
################# Results #################

Please enter a sentence: mike is a boy
ikemay isay aay oybay 



# **********  HW 2 complete! *********
