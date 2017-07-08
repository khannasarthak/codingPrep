t = int(input())
for p in (range(t)):
	n = int(input())
	k = list(map(int,input().split()))
	o = int(input())
	if o not in k:
		print (-1)
	else:
		indices = [i for i, x in enumerate(k) if x == o]	# good way to find all occurances
		print (min(indices),max(indices))

# Read about enumerate properly
# without enumerate , we use binary search.
# https://stackoverflow.com/questions/13478974/how-to-find-all-occurrences-of-an-element-in-a-list