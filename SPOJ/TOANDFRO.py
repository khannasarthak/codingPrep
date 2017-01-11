import textwrap
def func(c,s):
    for k in range(len(c)):
        split = textwrap.wrap(s[k],c[k])
        rev = []

        for i in range(len(split)):
            if i%2==1:
                rev.append((split[i])[::-1])
            else:
                rev.append(split[i])
        # print (rev)
        op=[]
        for i in range(c[k]):
            op.append([word[i] for word in rev])
        chars = ''
        for i in op:
            for j in i:
                chars+=j
        print (chars)
w = -1
column = []
string = []
while True:
    w = int(input())
    if w == 0:
        break
    else:
        column.append(w)
        string.append(input())

func(column,string)
