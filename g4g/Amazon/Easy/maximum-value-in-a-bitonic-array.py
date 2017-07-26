def findmax(a,l,h):
	mid = int((l+h)/2)
	if a[mid]>a[mid+1] and a[mid]>a[mid-1]:
		return (a[mid])
	if a[mid]>a[mid+1] and a[mid]<a[mid-1]:
		return findmax(a,l,mid-1)
	else:
		return findmax(a,mid+1,h)
	


t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int,input().split()))
	if n==1:
		print (a[0])
	elif n==2:
		print (max(a))
	else:
		print (findmax(a,0,n-1))
	