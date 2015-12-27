#!/usr/bin/python
import random
guess = 0
a =random.randint(1,6)

while (guess < 3):
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

