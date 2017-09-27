# HASH SET SOLUTION VERY SLOW

# from collections import Counter
# class Solution(object):
#     def distributeCandies(self, candies):
#         if len(set(candies))==len(candies):
# 	        return (len(candies)/2)
	
#         c = Counter(candies)
#         sis = 0
#         check = 0
#         for i in c:
#             if check<len(candies)/2:
#                 sis+=1
#                 check+=1
#         return (sis)

# ALTERNATIVE USING LOGIC

class Solution(object):
    def distributeCandies(self, candies):
        return min((len(candies)/2),len(set(candies)))