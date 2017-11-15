class Solution(object):
    
    def findTarget(self, root, k):
#         
        p = [root]
        op = set()
        for i in p:
            if k-i.val in op:
                return True
            op.add(i.val)
                
            if i.left:
                p.append(i.left)
            if i.right:
                p.append(i.right)
                
        return False