# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        #convert ll -> array - > bst
        
        def arrToBST(arr):
            if len(arr)==0:
                return None
            mid = len(arr)//2
            # print (mid,arr[:mid],arr[mid+1:])
            root = TreeNode(arr[mid])
            root.left = arrToBST(arr[:mid])
            root.right = arrToBST(arr[mid+1:])
            return root
            
        arr = []
        while head!=None:
            arr.append(head.val)
            head = head.next
        # print (arr)
        
        return arrToBST(arr)
            