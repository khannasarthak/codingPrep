def isSparse(n):
	b = bin(n)[2:]
	if b.find('11')==-1:
		return True
	else:
		return False
		
t = int(input())
for p in (range(t)):
	n = int(input())
	
	while(True):
		if (isSparse(n)):
			print (n)
			break
		else:
			n += 1