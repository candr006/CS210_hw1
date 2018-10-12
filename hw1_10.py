#!/usr/bin/python  
import math
print ''
print '*************************************************************************'
print "INPUT NOTE: To enter a number of the form '6*10^154', please type '6e154'"
print '*************************************************************************'
a=raw_input("Enter value for a: ")
a=float(a)
b=raw_input("Enter value for b: ")
b=float(b)
c=raw_input("Enter value for c: ")
c=float(c)
print("")
print("******* Solutions *********")
if b>=0:
	num1=((-1*b)-(math.sqrt(math.pow(b,2)-4*a*c)))
	denom1=(2*a)
	if denom1!=0:
		root1=num1/denom1
		print('Root 1: '+repr(root1))
	else:
		print("Root 1- ERROR: can't divide by 0")

	num2=(2*c)
	denom2= ((-1*b)+(math.sqrt((math.pow(b,2))-4*a*c)))
	
	if denom2!=0:
		root2=num2/denom2
		print('Root 2: '+repr(root2))
	else:
		print("Root 2- ERROR: can't divide by 0")

if b<0:
	num3=(2*c)
	denom3=((-1*b)-(math.sqrt(math.pow(b,2)-4*a*c)))
	if denom!=0:
		root1=num3/denom3
		print('Root 1: '+repr(root1))

	num4=((-1*b)+(math.sqrt(math.pow(b,2)-4*a*c)))
	denom4=(2*a)
	if denom4!=0:
		root2=num4/denom4
		print('Root 2: '+repr(root2))
	
	else:
		print("Root 2- ERROR: can't divide by 0")
