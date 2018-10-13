#!/usr/bin/python  
import math
print ''
print '*************************************************************************'
print "INPUT NOTE: To enter a number of the form '6*10^154', please type '6e154'"
print '*************************************************************************'
a=raw_input("Enter value for a: ")
a_t=a
a=float(a)
if a_t!='0' and a==0:
	print('WARNING: Your number will cause an underflow. Exiting.')
	exit()
b=raw_input("Enter value for b: ")
b_t=b
b=float(b)
if b_t!='0' and b==0:
	print('WARNING: Your number will cause an underflow. Exiting.')
	exit()
c=raw_input("Enter value for c: ")
c_t=c
c=float(c)
if b_t!='0' and b==0:
	print('WARNING: Your number will cause an underflow. Exiting.')
	exit()
print("")
print("******* Solutions *********")

#check for complex roots
try:
	sqrtval=(math.pow(b,2)-(4*a*c))
	i_val='';
except OverflowError, e:
	print('WARNING: Your number(s) will cause an overflow. Exiting.')
	exit()
except ArithmeticError,e:
	print('WARNING: '+e+'. Exiting.')
	exit()

#use original formula when a!=o
if a!=0:
	denom1=(2*a)
	#handle complex solutions
	if sqrtval<0:
		sqrtval=-1*(sqrtval)
		print('Root 1: ('+repr(-1*b)+'+ sqrt('+repr(sqrtval)+') i)/'+'('+repr(denom1)+')')
		print('Root 2: ('+repr(-1*b)+'- sqrt('+repr(sqrtval)+') i)/'+'('+repr(denom1)+')')
		exit()

	num1=((-1*b)-(math.sqrt(sqrtval)))
	if denom1!=0:
		try:
			root1=num1/denom1
			print('Root 1: '+repr(root1)+i_val)
		except OverflowError, e:
			print('WARNING: Your number(s) will cause an overflow. Exiting.')
			exit()
		except ArithmeticError,e:
			print('WARNING: '+e+'. Exiting.')
			exit()		
	else:
		print("Root 1: NONE")

	num2=((-1*b)+(math.sqrt(sqrtval)))
	denom2= (2*a)
	
	if denom2!=0:
		try:
			root2=num2/denom2
			print('Root 2: '+repr(root2)+i_val)
		except OverflowError, e:
			print('WARNING: Your number(s) will cause an overflow. Exiting.')
			exit()
		except ArithmeticError,e:
			print('WARNING: '+e+'. Exiting.')
			exit()

	else:
		print("Root 2: NONE")
else:
	num3=(2*c)
	denom3=((-1*b)-(math.sqrt(sqrtval)))
	#handle complex solutions
	if sqrtval<0:
		sqrtval=-1*(sqrtval)
		print('Root 1: ('+repr(num3)+')/'+'('+repr(-1*b)+' + sqrt('+repr(sqrtval)+')i')
		print('Root 1: ('+repr(num3)+')/'+'('+repr(-1*b)+' - sqrt('+repr(sqrtval)+')i')
		exit()

	if denom3!=0:
		try:
			root1=num3/denom3
			print('Root 1: '+repr(root1)+i_val)
		except OverflowError, e:
			print('WARNING: Your number(s) will cause an overflow. Exiting.')
			exit()
		except ArithmeticError,e:
			print('WARNING: '+e+'. Exiting.')
			exit()
	else:
		print("Root 1: NONE")

	num4=(2*c)
	denom4=((-1*b)+(math.sqrt(sqrtval)))
	if denom4!=0:
		try:
			root2=num4/denom4
			print('Root 2: '+repr(root2)+i_val)
		except OverflowError, e:
			print('WARNING: Your number(s) will cause an overflow. Exiting.')
			exit()
		except ArithmeticError,e:
			print('WARNING: '+e+'. Exiting.')
			exit()			

	else:
		print("Root 2: NONE")
