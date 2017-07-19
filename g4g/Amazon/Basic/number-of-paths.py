def check(m,n):
	if m==1 or n==1:
		return 1
	return check(m-1,n)+check(m,n-1)

t = int(input())
for p in range(t):
	m,n = map(int,input().split())
	print (check(m,n))

# DO AGAIN!!!