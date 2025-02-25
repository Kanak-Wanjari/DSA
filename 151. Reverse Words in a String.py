class Stack:
	def __init__(self):
		self.stack = []

	def push(self,item):
		self.stack.append(item)

	def pop(self):
		if not self.is_empty():
			return self.stack.pop()
		return "Stack is Empty"

	def peek(self):
		if not self.is_empty():
			return self.stack[-1]
		return "Stack is Empty"

	def is_empty(self):
		return len(self.stack) == 0

	def size(self):
		return len(self.stack)

new_stack = Stack()	
w = "Sky is Blue"

for i in range(len(uw)):
	print(w[i], end = "")
	
print()