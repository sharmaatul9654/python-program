n=input('enter the number')
pw=len(n)
s=0
for i in n:
        s+=int(i)**pw
if int(n)==s:
       print('amstrong number')
else:
       print('not amstrong')
