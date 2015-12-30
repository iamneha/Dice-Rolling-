#!/usr/bin/python
#In this game program run and roll the dice and randomly number came 
#Program ask again to roll the dice or not

import random 
print "Rolling the dice......."
print (random.randint(1,6))

def dice():
 str = raw_input("Want to roll the dice again \n")
 if str == "yes" or str == "y":
   print "Rolling the dice...."
   print (random.randint(1,6))
 else:
   print "stop"
dice()
