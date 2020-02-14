import math
a=int(input())
b=int(input())
c=int(input())
D=b**2-4*a*c
if D<0:
	print("roots does not exist or imaginary roots")
else:
	x=(-b-math.sqrt(D))/2*a
	y=(-b+math.sqrt(D))/2*a
	print("roots are:",x,y)
