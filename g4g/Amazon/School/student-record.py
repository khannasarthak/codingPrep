t = int(input())
while (t!=0):
	t -= 1
	n = int(input())
	a  = (input().split())
	names  =  [x for x in a if x.isalpha()]	# creates a list out of a whichi just gives names
	scores = [x for x in a if x.isalpha()==False]
	k = [scores[i:i+3] for i in range(0, len(scores), 3)]
	avg = []

	for i in k:
		i = list(map(int,i))
		avg.append(int(sum(i)/3))
	m = max(avg)
	pos = avg.index(m)
	print (names[pos], m)