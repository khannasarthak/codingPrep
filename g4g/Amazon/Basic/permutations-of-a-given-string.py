from itertools import permutations
t = int(input())
for p in (range(t)):
	a = input()
	k = [''.join(i) for i in permutations(a)]
	print (*sorted(k,key=str.lower))

# Another Solution without using itertools
# Try to do using backtracking http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/