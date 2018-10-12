#!/usr/bin/python  
import math
print "Quadratic Equation for equations of the form ax^2+bx+c=0"
a=input("Enter value for a: ")
b=input("Enter value for b: ")
c=input("Enter value for c: ")
print("")
print("******* Solutions *********")
if b>=0:
	num=((-1*b)-(math.sqrt(math.pow(b,2)-4*a*c)))
	denom=(2*a)
	if denom!=0:
		root1=num/denom
		print('Root 1: '+repr(root1))
	else:
		print("Root 1- ERROR: can't divide by 0")

	num=(2*c)
	denom= ((-1*b)+(math.sqrt((math.pow(b,2))-4*a*c)))
	
	if denom!=0:
		root2=num/denom
		print('Root 2: '+repr(root2))
	else:
		print("Root 2- ERROR: can't divide by 0")

if b<0:
	num=(2*c)
	denom=((-1*b)-(math.sqrt(math.pow(b,2)-4*a*c)))
	if denom!=0:
		root1=num/denom
		print('Root 1: '+repr(root1))

	num=((-1*b)+(math.sqrt(math.pow(b,2)-4*a*c)))
	denom=(2*a)
	if denom!=0:
		root2=num/denom
		print('Root 2: '+repr(root2))
	
	else:
		print("Root 2- ERROR: can't divide by 0")
