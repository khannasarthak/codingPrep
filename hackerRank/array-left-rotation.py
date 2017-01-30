from collections import deque
x,d = list(map(int,input().split(' ')))
n = list(map(int,input().split()))
a = deque(n)
a.rotate(-d)
a= (list(a))
print (*a)
