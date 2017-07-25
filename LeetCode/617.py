class Solution(object):
    def mergeTrees(self, t1, t2):
        if not t1 and not t2:
            return None
        op = TreeNode((t1.val if t1 else 0)+ (t2.val if t2 else 0))
        op.left = self.mergeTrees(t1 and t1.left,t2 and t2.left)
        op.right = self.mergeTrees(t1 and t1.right,t2 and t2.right)
        return op