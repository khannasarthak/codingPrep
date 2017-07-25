class Solution(object):
    def levelOrderBottom(self, root):
        if root is None:
            return []
        nodes = [root]
        res = []
        while nodes:
            res.append([node.val for node in nodes])
            nextnodes= []
            for node in nodes:
                if node.left:
                    nextnodes.append(node.left)
                if node.right:
                    nextnodes.append(node.right)
            nodes = nextnodes
        return res[::-1]
        """