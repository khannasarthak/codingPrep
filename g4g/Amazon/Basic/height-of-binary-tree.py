def height(root):
    if root is None:
        return (0)
    else:
        ldepth = height(root.left)
        rdepth = height(root.right)
        return (max(ldepth+1,rdepth+1))