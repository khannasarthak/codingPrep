# find parity

n = '11101'
k = 0 
for i in n:
	k = k^int(i)
print (k)

# Use XOR, if odd number then it gives back the same numbers else gives 0 if even