# Name: Romeo Ekirapa
# Section:
# homework_3.py

##### Template for Homework 3, exercises 5.1 - 5.5 ######

# **********  Exercise 5.1 **********
'''
def negate(num):
    return -num
def large_num(num):
    res = (num > 10000)
    
negate(b)
neg_b = num
print 'b:', b, 'neg_b:', neg_b

big = large_num(b)
print 'b is big:', big
'''

# Bugs
##### BUG 1 #####

# negate(b)
# variable b is not defined

##### BUG 2 #####

# neg_b = num
# variable num is not defined and hence cannot be assigned to another variable

##### BUG 3 #####

# def large_num(num):
   # res = (num > 10000)
# function requires a return statement

# **********  Exercise 5.2 ********** 

# Define "Mutable" and list what data structures have this characteristic

# Data can be changed.
# examples : List, Dictionaries

# Define "Immutable" and list what data structures have this characteristic

# Data cannot be changed.
# examples : String, Integers, Floats, Tuples



# **********  Exercise 5.3 **********

import math

def ball_collide(ball1, ball2):
    '''
    Computes whether or not two balls are colliding
    
    ball1: a tuple of (x-coord, y-coord, radius) nums (ints or floats);
        represents first ball
    ball2: a tuple of (x-coord, y-coord, radius) nums (ints or floats); 
        represents second ball

    returns: True if the balls collide and False if they do not collide
    '''
    x1, y1, r1 = ball1
    x2, y2, r2 = ball2
    
    change_in_x = (x2 - x1)
    change_in_y = (y2 -y1)
    pyt = (change_in_x)**2 + (change_in_y)**2
    distance = math.sqrt(pyt)

    rad = r1 + r2

    if (distance <= rad):
        return True
    return False
    

# Test Cases for Exercise 5.3
print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True

################ Results ###############

False
True
True

# **********  Exercise 5.4 **********

def add_class(class_num, desc, class_dict):
    '''
    Adds a class number/class name pair to a dictionary
    
    class_num: a string; the MIT number associated with the class
    desc: a string; the English name of the class
    class_dict: a dictionary with the keys being class numbers
     and the values being class names

    returns: nothing; only modifies class_dict
    '''
    class_dict[class_num] = desc
    print class_num, ":", desc, "Class Added"
    

def print_classes(course, class_dict):
    '''
    Prints out all the classes you've taken in a given Course.
     If no classes were taken in the Course, print out that none were taken
    
    course: a string; the Course for which we would like to
     print out classes taken
    class_dict: a dictionary with the keys being class numbers
     and the values being class names

    returns: nothing; simply prints out relevant information
    '''
    printed = False
    
    class_keys = class_dict.keys()
    
    for class_key in class_keys:
        
        if class_key[:class_key.index(".")] == course:
            print class_key, "-", class_dict[class_key]
            printed = True

    if not printed:
        print "No classes taken in course " + course

# Test Cases for Exercise 5.4

classes = { "1.202" : "Introduction to Programming",
            "2.303" : "Special Topics",
            "3.404" : "Database Administration",
            "4.101" : "Communication Skills",
            "1.201" : "Business Studies" }

add_class("1.103", "Marketing", classes)
add_class("2.301", "Anthropology", classes)
add_class("3.102", "Internet Technologies", classes)

print_classes("1", classes)
print_classes("2", classes)
print_classes("5", classes)

################ Results ###############

1.103 : Marketing Class Added
2.301 : Anthropology Class Added
3.102 : Internet Technologies Class Added
1.201 - Business Studies
1.202 - Introduction to Programming
1.103 - Marketing
2.303 - Special Topics
2.301 - Anthropology
No classes taken in course 5


# **********  Exercise 5.5 **********

def buildAddrBook(fileName):
    '''
    Builds an address book from a file.
    
    fileName: a string, the name of the file to read in
     File must be in the format specified in Exercise 5.5.

    returns: a dictionary with keys and values generated
      from the file, as specified in Exercise 5.5.
    '''
    addrBook = {}
    input_file = open(fileName)
    for line in input_file:
        split_line = line.split(',')
        name = split_line[0] + ', ' + split_line[1]
        phoneNumber = split_line[2]
        emailAddress = [x.rstrip("\r\n") for x in split_line[3:]]
        addrBook[name] = [phoneNumber] + emailAddress
    input_file.close()
    return addrBook

def changeEntry(addrBook, entry, field, newValue):
    '''
    Changes one entry in the specified address book.

    addrBook: a dictionary in the address book format
      returned by buildAddrBook.
    entry: a string; the pre-existing entry to change
    field: a string; the field to change (one of: "name",
      "phoneNumber", "emailAddress")
    newValue: the new value for the specified field

    returns: nothing; only modifies addrBook
    '''
    addrBook_keys = addrBook.keys()

    if not entry in addrBook_keys:
        print 'invalid entry: ', entry
    elif field == 'name':
        value = addrBook[entry]
        del addrBook[entry]
        addrBook[newValue] = value
    elif field == 'phoneNumber':
        addrBook[entry][0] = newValue
    elif field == 'emailAddress':
        addrBook[entry].append(newValue)
    else:
        print 'Incorrect field: ', field
    
addrBook = buildAddrBook('rawAddresses.csv')

# Test Cases for Exercise 5.5

changeEntry(addrBook, 'Lemon, Liz', 'emailAddress', 'lizzing@starwars.net')
print addrBook['Lemon, Liz'] == \
                ['(202) 555-8130', 'lizlemon@nbc.com', 'lizzing@starwars.net'] # should print True

changeEntry(addrBook, 'Lemon, Liz', 'name', 'Mark, Okumu')
print addrBook['Mark, Okumu'] == \
                ['(202) 555-8130', 'lizlemon@nbc.com', 'lizzing@starwars.net'] # should print True

changeEntry(addrBook, 'Bitddiddle, Ben', 'emailAddress', 'bitddiddly@bu.edu')  

changeEntry(addrBook, 'Beaver, Tim', 'homeAddress', 'Baltimore, MD')

################ Results ###############

True
True
invalid entry:  Bitddiddle, Ben
Incorrect field:  homeAddress


