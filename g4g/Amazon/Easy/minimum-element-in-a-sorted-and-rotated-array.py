def find(a,l,r):
	mid = int((l+r)/2)
	if r<l:
		return a[0]
	if r==l:
		return a[l]
	if mid < r and a[mid+1] < a[mid]:
		return a[mid+1]
	if mid > l and a[mid] < a[mid-1]:
		return a[mid]
	if a[r] > a[mid]:
		return find(a, l, mid-1)
	return find(a, mid+1, r)

t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int, input().split()))
	l = 0
	r = n-1
	print (find(a,l,r))
	