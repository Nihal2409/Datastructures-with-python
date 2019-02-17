class Node(object):
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

class BinarySearchTree(object):
	def __init__(self,root=None):
		self.root = root
	
	def insert(self,data):
		if self.root is None:
			self.root = Node(data)
		else:
			self._insert(data,self.root)
	def _insert(self,data,curr_node):
		if curr_node.value > data:
			if curr_node.left is None:
				curr_node.left = Node(data)
			else:
				self._insert(data,curr_node.left)
		elif curr_node.value < data:
			if curr_node.right is None:
				curr_node.right = Node(data)
			else:
				self._insert(data,curr_node.right)
		else:
			print("Value is already present")
			
	def find(self,data):
		if self.root:
			is_found = self._find(data,self.root)
			if is_found:
				return True
			return False
		else:
			return None
	def _find(self,data, curr_node):
		if data > curr_node.value and curr_node.right:
			return self._find(data,curr_node.right)
		if data < curr_node.value and curr_node.left:
			return self._find(data,curr_node.left)
		if data == curr_node.value:
			return True
			
	def is_bst_satisfied(self):
		if self.root:
			is_satisfied = self._is_bst_satisfied(self.root,self.root.data)
		
			if is_satisfied is None:
				return True
			return False
		return True
	
	def _is_bst_satisfied(self, curr_node, data):
		if curr_node.left:
			if data > curr_node.left.data:
				return self._is_bst_satisfied(curr_node.left,curr_node.left.data)
			else:
				return False
		if curr_node.right:
			if data < curr_node.right.data:
				return self._is_bst_satisfied(curr_node.right,curr_node.right.data)
			else:
				return False		
			
	def print_tree(self,traverse_type):
		if traverse_type == 'inorder':
			return self.inorder_print(bst.root,'')
		
	def inorder_print(self,start,traversal):
		if start:
			traversal = self.inorder_print(start.left,traversal)
			traversal += str(start.value) + '-'
			traversal = self.inorder_print(start.right,traversal)
		return traversal
		
	
bst = BinarySearchTree()
bst.insert(8)
bst.insert(10)
bst.insert(6)
bst.insert(5)
print(bst.find(7))
print(bst.print_tree('inorder'))
	