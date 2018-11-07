class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self):
		self.head = None


	def push(self, data):
		newNode = Node(data)		
		oldHead = self.head
		newNode.next = oldHead
		self.head = newNode

	def peek(self):
		print (self.head.data)

	def pop(self):
		e
		if self.head==None:
			print (-1)
			return
		print ("Popped:", self.head.data)
		self.head = self.head.next



	def disp(self):
		c = 0
		while self.head:
			print (self.head.data,sep=' ')
			self.head = self.head.next
			c+=1
		print ("Size:", c) 



s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(7)
s.pop()
# s.push(9)
# s.pop()





s.disp()
