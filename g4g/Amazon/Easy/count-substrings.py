from collections import Counter
t = int(input())
for p in range(t):
	n = (input())
	nums = Counter(n)
	i = nums['1']
	print (int((i)*(i-1)/2))