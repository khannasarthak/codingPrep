class Solution(object):
    def levelOrder(self, root):
        
        if root is None:
            return []
        res = []
        nodes = [root]
        while nodes:
            res.append([node.val for node in nodes])
            nextnodes = []
            for node in nodes:
                if node.left:
                    nextnodes.append(node.left)
                if node.right:
                    nextnodes.append(node.right)
            nodes = nextnodes
        return (res)