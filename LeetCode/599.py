from collections import Counter
class Solution(object):
    def findRestaurant(self, list1, list2):
        common = list(set(list1).intersection(set(list2)))
# print (common)

        op = {}
        for i in common:
            if i in list1 and i in list2:
                op[i]=list1.index(i)+list2.index(i)

        minIndex = 0
        # print (op)
        # for i in common:
        # 	if common[i]<minIndex:
        # 		minIndex=common[i]
        minIndex = min(op, key=op.get)
        # print (minIndex)
        # print ( [k for k,v in op.items() if v == op[minIndex] )
        ans = []
        for k,v in op.items():
            if v==op[minIndex]:
                ans.append(k)
        return (ans)