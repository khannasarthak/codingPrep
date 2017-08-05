t = int(input())
for p in (range(t)):
	l,r = (map(int, input().split()))
	op=0
	for i in range(l,r+1):
		if str(i)[0]==str(i)[-1]:
			op+=1
	print (op)
		