t = int(input())
for p in (range(t)):
	n = int(input())
	a = input().split()
	d = {}
	w = []
	for word in a:
		key = "".join(sorted(word))
		w.append(key)
		d[key]=(w.count(key))
	
	op= sorted(list(d.values()))
	print (*op)