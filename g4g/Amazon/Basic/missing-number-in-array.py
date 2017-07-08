t = int(input())
for p in (range(t)):
	n = int(input())
	c = list(map(int, input().split()))
	d = [x for x in range(min(c),max(c)+1)]
	k = set(d)- set(c)
	if list(set(k))!=[]:
		print (int(list(set(k))[0]))
	else:
	    print (1)   # handles when both are []