import re
t = int(input())
for p in (range(t)):
	s = (input())
	matches = (re.findall(r"(\d+)", s))
	matches = list(map(int,matches))
	print (max(matches))