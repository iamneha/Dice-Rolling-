#!/usr/bin/python
import random
guess = 0
print "I am thinking number between 1 to 6"
a =random.randint(1,6)

while (guess < 3):
	print "You have only three chances to guess the number"
	b = input("Take a guess");
  	guess = guess + 1

	if b > a:
	 print 'The no is too high'
	elif b < a:
	 print 'The no is too low'
	elif b == a:
	 break

if guess == a:
	print "you take right guess"

