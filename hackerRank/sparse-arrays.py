#Link : http://hr.gs/eh1
n = int(input())
s = []
for i in range(n):
	s.append(str(input()))
q = int(input())
query = []
for i in range(q):
	query.append(str(input()))
res = []
for qu in query:
	res.append(s.count(qu))
for i in res:
    print (i)
