class Solution(object):
    def averageOfLevels(self, root):
        if root is None:
            return 0
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
        op = []
        for i in res:
            print (i)
            op.append((float(sum(i))/len(i)))
        return (op)