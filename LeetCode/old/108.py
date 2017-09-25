class Solution(object):
    def sortedArrayToBST(self, nums):
        n = len(nums)
        if n == 0:
            return None
        if n ==1:
            root = TreeNode(nums[0])
            return root
        mid = int(n/2)
        root = TreeNode(nums[mid])	
        left = nums[0:mid]
        right = nums[mid+1:]
        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)
        return root