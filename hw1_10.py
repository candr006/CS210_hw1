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
try:
	sqrtval=(math.pow(b,2)-(4*a*c))
	i_val='';
except OverflowError, e:
	print('ERROR: Your number(s) are too large')
	exit()
if sqrtval<0:
	i_val='i'
	sqrtval=-1*(sqrtval)

if a!=0:
	num1=((-1*b)-(math.sqrt(sqrtval)))
	denom1=(2*a)
	if denom1!=0:
		root1=num1/denom1
		print('Root 1: '+repr(root1)+i_val)
	else:
		print("Root 1: NONE")

	num2=((-1*b)+(math.sqrt(sqrtval)))
	denom2= (2*a)
	
	if denom2!=0:
		try:
			root2=num2/denom2
			print('Root 2: '+repr(root2)+i_val)
		except OverflowError, e:
			print("Result too large")
			exit()

	else:
		print("Root 2: NONE")
else:
	num3=(2*c)
	denom3=((-1*b)-(math.sqrt(sqrtval)))
	if denom3!=0:
		root1=num3/denom3
		print('Root 1: '+repr(root1)+i_val)
	else:
		print("Root 1: NONE")

	num4=(2*c)
	denom4=((-1*b)+(math.sqrt(sqrtval)))
	if denom4!=0:
		root2=num4/denom4
		print('here7')
		print('Root 2: '+repr(root2)+i_val)

	else:
		print("Root 2: NONE")
