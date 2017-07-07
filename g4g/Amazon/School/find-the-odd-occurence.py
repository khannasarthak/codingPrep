# This solution is basically hashing
from collections import Counter
t = int(input())
for p in (range(t)):
	n = int(input())
	k = list(map(int,input().split()))
	c = (Counter(k))
	for key in c:
	    value = c[key]
	    if value%2==1:
	    	print (key)


# talk about itereating over the counter dict
# Faster solution without using pythonic tools : http://www.geeksforgeeks.org/find-the-number-occurring-odd-number-of-times/

# best solution do BITWISE XOR