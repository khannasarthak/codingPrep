# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K, M):
    # write your code in Python 3.6
    
    day = 0 
    status = ['0']*len(A)
    opDay = []
    
    for i in A:
        day +=1
        status[i-1]='1'
        # print (status)
        groups = ((''.join(status)).split('0'))
        for group in groups:
            if group == '':
                groups.pop(groups.index(''))
        # print ('Grp',groups)
        tmpLong = 0
        for group in groups:
            # print ('t',group,len(group))
            if len(group)>=K:
                # print ('Long Group:', group, 'Day', day)
                tmpLong +=1
        if tmpLong==M:
            # print ('DAY OP',day)
            opDay.append(day)
    if len(opDay)==0:
        return -1
    return max(opDay)