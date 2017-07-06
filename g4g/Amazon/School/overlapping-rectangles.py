t = int(input())
while (t!=0):
	t -= 1
	r1x1,r1y1,r1x2,r1y2 = (input().split())
	r2x1,r2y1,r2x2,r2y2 = (input().split())
	if (int(r1x1)>int(r2x2) or int(r2x1)>int(r1x2) or int(r2y2)>int(r1y1) or int(r1y2)>int(r2y1)):
		print (0)
	else:
		print (1)

# BASED ON criteria given here https://stackoverflow.com/questions/13390333/two-rectangles-intersection 
# and https://stackoverflow.com/questions/306316/determine-if-two-rectangles-overlap-each-other