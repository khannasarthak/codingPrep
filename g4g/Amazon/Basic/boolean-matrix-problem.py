t = int(input())
for p in range(t):

	r,c = (map(int,input().split()))
	m = list(map(int,input().split()))
	op = []
	k = []
	while m!= []:
		k.append(m[:c])
		m = m[c:] 
	row = [0 for i in range(r)]
	col = [0 for i in range(c)]
	
	for i in range(0,r):
		for j in range(0,c):
			# print (i,j)
			if k[i][j]==1:
				row[i] =1
				col[j] = 1
				
	for i in range(0,r):
		for j in range(0,c):
			if row[i]==1 or col[j]==1:
				k[i][j]=1
	for i in k:
		for j in i:
			op.append(j)
	print (*op)