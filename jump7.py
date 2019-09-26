a = 0
while a<100:
	a+=1
	if a%7==0:
		continue
	elif str(a).find('7')>0:
		continue
	else:
		print(a)
