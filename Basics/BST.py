class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None
class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        if self.root==None:
            self.root = Node(value)
        else:
            # Private functions _, python doesn't have private functions inherently
            self._insert(value, self.root)
            
    def _insert(self, value, currentNode):
        # Case 1: vaue to insert is smaller than current node
        if value<currentNode.value:
            if currentNode.leftChild ==None:
                currentNode.leftChild = Node(value)
            else:
                self._insert(value, currentNode.leftChild)
        elif value>currentNode.value:
            if current.rightChild == None:
                currentNode.rightChild = Node(value)
            else:
                self._insert(value, currentNode.rightChild)
        else:
            # same value
            print ('Tree already has the value stored.')

    def print
            