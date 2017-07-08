import math
t = int(input())
for p in (range(t)):
	h,m  = (map(float,input().split()))
	hangle = h*30+ m*0.5
	if m==60:
		mangle = 0
	else:
		mangle = m*6
	k =  abs(mangle-hangle)
	if k >180:
		print (math.floor(360-k))
	else:
		print (math.floor(k))