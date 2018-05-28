binary = bin(num)[2:]

comp = ''
for bit in binary:
	if bit=='0':
		comp=comp+ '1'
	elif bit=='1':
		comp=comp+'0'
dec = int(comp,2)
print (dec)
