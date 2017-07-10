t = int(input())
for p in range(t):
	n = int(input())
	a = list(map(int,input().split()))
	l,r = map(int,input().split())
	newl = l-1
	newr = r-1
	suba = a[newl:newr+1]
	op =  (a[:newl]+suba[::-1]+a[newr+1:])
	print (*op)