#!/usr/bin/python
import random
a = 5
b = raw_input("Guess any number between 1 to 6")

def guess():
	if b > a:
	 print 'The no is too high'
	elif b < a:
	 print 'The no is too low'
	elif b == a:
	 print 'You guess correct number'
	else :
	 print 'Number not exist'
guess()
