def traverse_level_order(root):
    if root is None:
        return []
    res = []
    nodes = [root]
    while nodes:
        res.append([node.data for node in nodes])
        nextnodes = []
        for node in nodes:
            if node.left:
                nextnodes.append(node.left)
            if node.right:
                nextnodes.append(node.right)
        nodes = nextnodes
    for i in res:
        print (*i,end=' ')