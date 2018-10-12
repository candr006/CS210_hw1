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

#check for complex roots
sqrtval=(math.pow(b,2)-(4*a*c))
i_val='';
if sqrtval<0:
	print('here1')
	i_val='i'
	sqrtval=-1*(sqrtval)

if b>=0:
	print('here2')
	num1=((-1*b)-(math.sqrt(sqrtval)))
	denom1=(2*a)
	if denom1!=0:
		print('here3')
		root1=num1/denom1
		print('Root 1: '+repr(root1)+i_val)
	else:
		print('here4')
		print("Root 1- ERROR: can't divide by 0")

	num2=(2*c)
	denom2= ((-1*b)+(math.sqrt(sqrtval)))
	
	if denom2!=0:
		print('here5')
		root2=num2/denom2
		print('Root 2: '+repr(root2)+i_val)
	else:
		print("Root 2- ERROR: can't divide by 0")

if b<0:
	print('here6')
	num3=(2*c)
	denom3=((-1*b)-(math.sqrt(sqrtval)))
	if denom3!=0:
		root1=num3/denom3
		print('Root 1: '+repr(root1)+i_val)

	num4=((-1*b)+(math.sqrt(sqrtval)))
	denom4=(2*a)
	if denom4!=0:
		root2=num4/denom4
		print('here7')
		print('Root 2: '+repr(root2)+i_val)
	
	else:
		print("Root 2- ERROR: can't divide by 0")
