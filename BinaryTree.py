class Stack(object):
	def __init__(self):
		self.items=[]
	def is_empty(self):
		return len(self.items) ==0
	def push(self,item):
		self.items.append(item)
	def pop(self):
		if not self.is_empty():
			return self.items.pop()
	def peek(self):
		if not self.is_empty():
			return self.items[-1].value
	def __len__(self):
		return self.size()
	def size(self):
		return len(self.items)

class Queue(object):
	def __init__(self):
		self.items = []
	def is_empty(self):
		return len(self.items) == 0
	def enqueue(self,item):
		self.items.insert(0, item)
	def dequeue(self):
		if not self.is_empty():
			return self.items.pop()
	def peek(self):
		if not self.is_empty():
			return self.items[-1].value
	def __len__(self):
		return self.size()
	def size(self):
		return len(self.items)
		

class Node(object):
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None
		
class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)
	
	#print the tree depending on the type of traversal
	def print_tree(self,traversal_type):
		if traversal_type == 'preorder':
			return self.preorder_print(tree.root,'')
		elif traversal_type == 'inorder':
			return self.inorder_print(tree.root,'')
		elif traversal_type == 'postorder':
			return self.postorder_print(tree.root,'')
		elif traversal_type == 'levelorder':
			return self.levelorder_print(tree.root)
		elif traversal_type == 'reverselevelorder':
			return self.reverse_levelorder_print(tree.root)
			
	#Pre-order traversal method
	def preorder_print(self, start, traversal):
		#root ->left -> right
		if start:
			traversal += (str(start.value)+ '-')
			traversal = self.preorder_print(start.left,traversal)
			traversal = self.preorder_print(start.right,traversal)
		return traversal
	
	#In-order traversal method
	def inorder_print(self,start,traversal):
		#left->root->right
		if start:
			traversal = self.inorder_print(start.left,traversal)
			traversal += (str(start.value) + '-')
			traversal = self.inorder_print(start.right,traversal)
		return traversal
		
	#Post-order traversal method
	def postorder_print(self,start,traversal):
		#left -> right -> root
		if start:
			traversal = self.postorder_print(start.left,traversal)
			traversal = self.postorder_print(start.right,traversal)
			traversal += (str(start.value) + '-')
		return traversal
	
	#level-order traversal method
	def levelorder_print(self,start):
		#makes use of the queue data structure
		if start is None:
			return
		queue = Queue()
		queue.enqueue(start)
		traversal = ''
		while  len(queue) > 0:
			traversal += str(queue.peek()) + '-'
			node = queue.dequeue()
				
			if node.left:
				queue.enqueue(node.left)
			if node.right:
				queue.enqueue(node.right)
		return traversal
	
	#Reverse level-order traversal method
	def reverse_levelorder_print(self,start):
		if start is None:
			return
		queue = Queue()
		stack = Stack()
		traversal = ''
		queue.enqueue(start)
		while len(queue) > 0:
			node = queue.dequeue()
			stack.push(node)
			
			if node.right:
				queue.enqueue(node.right)
			if node.left:
				queue.enqueue(node.left)
		while len(stack) != 0:
			node = stack.pop()
			traversal += str(node.value) + '-'
		return traversal
		
	#Height of the tree - It is the longest edge path to the last leave in the tree
	def height(self, start):
		if start is None:
			return -1
		left_height = self.height(start.left)
		right_height = self.height(start.right)
		
		return 1 + max(left_height,right_height)
		
	# calculating the size of the tree which is the total number of nodes in the tree
	def size_tree(self):
		if self.root is None:
			return 0
		stack = Stack()
		stack.push(self.root)
		count = 1
		while stack:
			node = stack.pop()
			if node.left:
				stack.push(node.left)
				count+=1
			if node.right:
				stack.push(node.right)
				count+=1
		return count
		
	# size using recursion method
	def size_recurse(self, start):
		count = 0
		if start is None:
			return 0
		return 1 + self.size_recurse(start.left) + self.size_recurse(start.right)
			
		
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(f'Pre-Order: {tree.print_tree("preorder")}')
print(f'In-Order: {tree.print_tree("inorder")}')
print(f'Post-Order: {tree.print_tree("postorder")}')
print(f'Level-Order: {tree.print_tree("levelorder")}')
print(f'Reverse-Level-Order: {tree.print_tree("reverselevelorder")}')
print(f'Height of the tree: {tree.height(tree.root)}')
print(tree.size_tree())
print(tree.size_recurse(tree.root))