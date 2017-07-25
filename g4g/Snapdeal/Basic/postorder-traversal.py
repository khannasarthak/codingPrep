def postorderTraversal(root):
    if root is None:
        return
    s1 = []
    s2 = []
    s1.append(root)
    while (len(s1)>0):
        node = s1.pop()
        s2.append(node)
        if node.left is not None:
            s1.append(node.left)
        if node.right is not None:
            s1.append(node.right)
    op = []
    while (len(s2)>0):
        node = s2.pop()
        op.append(node.data)
    print (*op)
        