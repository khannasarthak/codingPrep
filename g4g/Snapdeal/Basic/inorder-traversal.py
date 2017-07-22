def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print (root.data,end=' ')
        inorderTraversal(root.right)