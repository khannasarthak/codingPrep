from collections import Counter
t = int(input())
for p in range(t):
	n,x = map(int,input().split())
	c = list(map(int,input().split()))
	# print (x,c)
	if x not in c:
		print (-1)
	else:
		count = Counter(c)
		for key in count:
			if key == x:
				print (count[key])