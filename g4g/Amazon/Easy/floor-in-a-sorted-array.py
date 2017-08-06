def search(a,l,r,x):
	if l>r:
		return -1
	mid = int(int(l+r)/2)
	
	if a[r]<=x:
		return r
	if a[mid]==x:
		return mid
	if mid>0 and a[mid-1]<=x and x<a[mid]:
		return mid-1
	elif a[mid]>x:
		return search(a,l,mid-1,x)
	elif a[mid]<x:
		return search(a,mid+1,r,x)
	

t = int(input())
for p in (range(t)):
	n,x = map(int,input().split())
	a = list(map(int,input().split()))
	print (search(a,0,n-1,x))