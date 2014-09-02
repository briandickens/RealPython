__author__ = 'bdickens'

import pdb
import sys
from random import choice

random1 = [1,2,3,4,5,6,7,8,9,10,11,12]
random2 = [1,2,3,4,5,6,7,8,9,10,11,12]

while True:
    print "To exit the game type 'exit'"
    num1 = choice(random1)
    num2 = choice(random2)
    pdb.set_trace()
    answer  = raw_input("What is {} times {}? ".format(num1, num2))

    # exit
    if answer == "exit":
        print "Now exiting game!"
        sys.exit()
    
    #test = int(choice(random2)) * (choice(random1))
    #determine if number is correct
    elif answer == str(num1 * num2):
        print "Correct!"
    else:
        print "Wrong!"
