def add(x,y):
	return(x+y)
def sub(x,y):
	return(x-y)
def multiply(x,y):
	return(x*y)
def divide(x,y):
	return(x/y)
def squareroot(x,y):
	import math
	a=math.sqrt(x)
	b=math.sqrt(y)
	return(a,b)
print("choose your operation /1/2/3/4/5")
print("1.addition \t 2.substraction \t 3.multipication \t 4.division \t 5.squareroot\n")

choice=raw_input("enter your choice 1/2/3/4/5:-")
x=input("enter a number")
y=input("enter another number")
if (choice=='1'):
	print add(x,y)
elif(choice=='2'):
     print sub(x,y)
elif(choice=='3'):
     print multiply(x,y)
elif(choice=='4'):
     print divide(x,y)
elif(choice=='5'):
    print squareroot(x,y)
else:
    print INVALID



