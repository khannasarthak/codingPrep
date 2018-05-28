class Solution(object):
    def maxDepth(self, root):
        if root:
            ldepth = self.maxDepth(root.left)
            rdepth = self.maxDepth(root.right)
            
            return max(ldepth,rdepth)+1
        else:
            return 0