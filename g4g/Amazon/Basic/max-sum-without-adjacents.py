def maxsum(k):
	incl = 0
	excl = 0
	for i in (k):
		kexcl = max(incl,excl)
		incl = excl + i
		excl = kexcl
	print (max(incl, kexcl))
t = int(input())
for p in (range(t)):
	n = int(input())
	k = list(map(int,input().split()))
	maxsum(k)


# IMPORTANT Question, learn aboiut dynamic programming
# http://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
# https://stackoverflow.com/questions/1065433/what-is-dynamic-programming
# https://stackoverflow.com/questions/4487438/maximum-sum-of-non-consecutive-elements