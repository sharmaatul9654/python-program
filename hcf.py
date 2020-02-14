a=int(input('entre the no'))
b=int(input('entre the other no'))
if a>b:
	m=b
else:
	m=a
for i in range(1,m+1):
	if (a%i==0 and b%i==0):
		r=i
print(r)
