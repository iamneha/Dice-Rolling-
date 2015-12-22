#!/usr/bin/python
import random 
print "Rolling the dice......."
print (random.randint(1,6))

def dice():
 str = raw_input("Wnat to roll the dice again \n")
 if str == "yes" or str == "y":
   print "Rolling the dice...."
   print (random.randint(1,6))
 else:
   print "stop"
dice()
