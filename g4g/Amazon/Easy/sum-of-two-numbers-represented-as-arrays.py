def sums(a,b,m,n):
	p='0'
	s = str(int(''.join(a))+int(''.join(b)))
	i = max(m,n)-len(s)
	print (*list(p*i+s))
	

t = int(input())
for p in (range(t)):
	m,n = map(int,(input().split()))
	a =	input().split()
	b =	input().split()
	
	(sums(a,b,m,n))