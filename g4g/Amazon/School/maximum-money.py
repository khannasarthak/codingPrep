t = int(input())
while (t!=0):
	t -= 1
	n,m = map(int,(input().split(' ')))
	if n%2==1:
		print ((int(n/2)+1)*m)
	else:
		print ((int(n/2))*m)