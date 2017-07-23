class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0       
        ldepth = self.maxDepth(root.left)
        rdepth = self.maxDepth(root.right)        
        return (max(ldepth+1,rdepth+1))
                