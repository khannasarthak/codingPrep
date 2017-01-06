a = int(input())
ans =[]
for i in range(a):
	c = (list(map(str,input().split(' '))))
	b = []

	for i in c:
		b.append(i[::-1])
	b = list(map(int,b))
	sum1 = sum(b)
	sum2 = str(sum1)
	sum2 =(sum2[::-1].strip('0'))
	ans.append(sum2)
print (*ans,sep = '\n')
