#List with 3 nodes

class Node:
    def  __init__(self,data): # initialises the node object
        self.data = data
        self.next = None # point to next
class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self): # Linked list traversal
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next

    def pushNew(self,newData): # push new data in the beginning
        newNode = Node(newData)
        newNode.next = self.head  # make new
        self.head = newNode

    def insertAfter(self,prevNode,newData): # insert after a given node
        if prevNode is None:
            print ('Not in linked list')
            return
        newNode = Node(newData) 
        newNode.next = prevNode.next
        prevNode.next = newNode

    def append(self,newData): # insert at end
        newNode = Node(newData)
        if self.head is None: # check is List is empty
            self.head = newNode
            return
        last = self.head
        while(last.next): # go to last node
            last = last.next
        last.next = newNode # change next of last node


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third
llist.printList()
