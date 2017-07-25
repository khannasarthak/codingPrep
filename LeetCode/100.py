class Solution(object):
    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(q.left,p.left) and self.isSameTree(q.right,p.right)
        return (p==q)