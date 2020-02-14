a=int(input('entre the no'))
b=int(input('entre the other no'))
if a>b:
	max=a
else:
	max=b
for i in range(max,(a*b)+1):
	if max%a==0 and max%b==0:
		print(max)
		break
	max=max+1
