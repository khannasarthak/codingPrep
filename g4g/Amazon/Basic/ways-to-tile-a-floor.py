t = int(input())
for p in range(t):
	n = int(input())
	fibo=[0,1]
	for i in range (n):
		fibo.append(fibo[-1]+fibo[-2])
	print (fibo[-1])