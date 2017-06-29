class treeNode:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

root = treeNode(1)
root.left = treeNode(2)
root.right = treeNode(3)
root.left.left = treeNode(4)
