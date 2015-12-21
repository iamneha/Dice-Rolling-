#!/usr/bin/python
import random 
print "Rolling the dice......."
print (random.randint(1,6))

def dice():
 str = raw_input("yes or no \n")
 if str == "yes" :
   print (random.randint(1,6))
 else :
   print "no"
dice()
