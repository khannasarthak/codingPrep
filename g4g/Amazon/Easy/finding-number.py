def find(a,l,r,x):
	mid = int((l+r)/2)
	if l>r:
	    return 'OOPS! NOT FOUND'
	if a[mid] ==x:
		return mid
	if a[l]<=a[mid]:
		if (x>=a[l] and x<=a[mid]):
			return find(a,l,mid-1,x)
		return find(a,mid+1,r,x)
	elif x>=a[mid] and x<=a[r]:
		return find(a,mid+1,r,x)
	return find(a,l,mid-1,x)
	
t = int(input())
for p in (range(t)):
	n,x = map(int,(input()).split())
	a = list(map(int,input().split()))
	
	print (find(a,0,n-1,x))
