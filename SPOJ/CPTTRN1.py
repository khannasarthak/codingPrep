def design(a):
    for i in a:
        lines = i[0]
        chars = i[1]
        star =''
        dot = ''
        for j in range(chars):
            if j%2==0:
                star += '*'
            else:
                star += '.'

        for j in range(chars):
            if j%2==1:
                dot += '*'
            else:
                dot += '.'
        # print (star,dot)
        for j in range(lines):
            if j%2==0:
                print (star,sep='\n')
            else:
                print (dot,sep='\n')
        print ()

n = int(input())
a =[]
for i in range(n):
    a.append(list(map(int,input().split(' '))))
design(a)
