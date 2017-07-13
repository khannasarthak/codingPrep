t = int(input())
for p in range(t):
	n = int(input())
	a = ''
	for i in range(1,n+1):
		a = a+ (bin(i)[2:])
	print (sum(list(map(int,list(a)))))

# Try without inbuilt bin