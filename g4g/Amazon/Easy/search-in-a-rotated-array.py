def bin(l,h,a,k):
	# print (a[l:h+1])
	if h<l:
		return -1
	mid = int((l+h)/2)
	# print ('l',l,' h',h,' mid',mid,' a[mid]',a[mid])
	if a[mid]==k:
		return mid
	if a[l]<=a[mid]:
		if k>=a[l] and k<=a[mid]:
			return bin(l,mid-1,a,k)
		else:
			return bin(mid+1,h,a,k)
	else :
		if k>=a[mid] and k<=a[h]:
			return bin(mid+1,h,a,k)
		else:
			return bin(l,mid-1,a,k)

			
		

t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int,input().split()))
	k = int(input())
	print (bin(0,n-1,a,k))