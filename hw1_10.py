#!/usr/bin/python  
import math
print "Quadratic Equation for equations of the form ax^2+bx+c=0"
a=input("Enter value for a: ")
b=input("Enter value for b: ")
c=input("Enter value for c: ")
print("")
print("******* Solutions *********")
if b>=0:
	root1=((-1*b)-(math.sqrt(math.pow(b,2)-4*a*c)))/(2*a)
	print('Root 1: '+repr(root1))

	root2=(2*c)/((-1*b)+(math.sqrt(math.pow(b,2)-4*a*c)))
	print('Root 2: '+repr(root2))

if b<0:
	root1=(2*c)/((-1*b)-(math.sqrt(math.pow(b,2)-4*a*c)))
	print('Root 1: '+repr(root1))

	root2=((-1*b)+(math.sqrt(math.pow(b,2)-4*a*c)))/(2*a)
	print('Root 2: '+repr(root2))
