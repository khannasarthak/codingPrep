t = int(input())
for p in range(t):
	n = int(input())
	a = list(map(int,input().split()))
	a.sort(reverse=True)
	print (a[0]*a[1])


# http://www.geeksforgeeks.org/return-a-pair-with-maximum-product-in-array-of-integers/