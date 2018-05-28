s = ''
print (chr(92))
n = 26 # multiples of 26 are causing problem
while (n!=0):
	print (s)
	if n <=26:
		print ('N---',n)
		print ('S---',s)
		if n%26==0:
			s = s + chr(65)
		else:
			s = s + chr(64+n)
		# print (s)
	else:


		s = s + chr(64+(n%26))
		print ('Else S---',s,n%26)
	n = int(n/26)

print (s[::-1])
