from collections import Counter
t= int(input())
for p in (range(t)):
	n = int(input())
	bst = list(map(int,input().split()))
	f = 0
	if len(bst)==1:
		print ('1')
	else:
		for i in range(0,len(bst)-1):
			
			if bst[i]<bst[i+1]:
				f = 1 
			else:
				f = 0
				break
		bstunique = Counter(bst)
		k = 1
		for i in bstunique:
			if (bstunique[i])!=1:
				k = 0
		if f ==1 and k==1:
			print ('1')
		else:
			print ('0')