t = int(input())
for p in (range(t)):
	n,d = map(int,input().split())
	b = list(map(int,input().split()))
	k= (b[d:]+b[:d])
	print (*k)