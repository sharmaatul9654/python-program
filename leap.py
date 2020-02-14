year=int(input("entre year:"))
if year%4==0:
	if year%100==0:
		if year%400==0:
			print("{} is leap year".format(year))
		else:
			print("{} is not leap year".format(year))
	else:
		print("{} is a leap year".format (year))
else:
	prinrt("{} is not a leap year".format(year))	
