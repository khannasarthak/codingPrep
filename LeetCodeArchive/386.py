class Solution(object):
    def lexicalOrder(self, n):
        k = [str(x) for x in range(1,n+1)]
        return (list(map(int,sorted(k))))