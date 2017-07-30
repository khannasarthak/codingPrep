def ab(a,k):
	if len(a)==len(set(a)):
		return (False)
	else:
		op = []
		for i in range(len(a)):
			if a[i] in op:
				return True
				
			op.append(a[i])
			if i>=k:
				op.remove(a[i-k])
				
		return (False)
				
	
		


from collections import Counter
t = int(input())
for p in (range(t)):
	k,n = map(int,(input().split()))
	a =	list(map(int,input().split()))
	print (ab(a,k))

			

			
		




