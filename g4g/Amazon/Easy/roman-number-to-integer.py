t = int(input())
for p in (range(t)):
	a = input()
	nums = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	exc = {'IX':2,'IV':2,'XL':20,'XC':20,'CD':200,'CM':200}
	s1 = 0 
	for i in a:
		if i in nums:
			s1+= nums[i]
	for i in exc.keys():
		if a.find(i)!=-1:
			s1 = s1 - exc[i]
	print (s1)