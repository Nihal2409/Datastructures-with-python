class Node():
	def __init__(self,data):
		self.data = data
		self.next = None

class CircularLinkedList():
	def __init__(self):
		self.head = None
	def append(self,data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			new_node.next = new_node
		else:
			curr_node = self.head
			while curr_node.next != self.head:
				curr_node = curr_node.next
			curr_node.next = new_node
			new_node.next = self.head
	def prepend(self,data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			new_node.next = new_node
		else:
			last_node = self.head
			while last_node.next != self.head:
				last_node = last_node.next
			new_node.next = self.head
			last_node.next = new_node
			self.head = new_node
			
	def remove(self,data):
		if self.head.data == data:
			curr_node = self.head
			while curr_node.next != self.head:
				curr_node = curr_node.next
			curr_node.next = self.head.next
			self.head = self.head.next
		else:
			prev_node = None
			curr_node = self.head
			while curr_node.next !=self.head:
				prev_node = curr_node
				curr_node = curr_node.next
				if curr_node.data == data:
					prev_node.next = curr_node.next
					curr_node = curr_node.next
		
	def print_list(self):
		curr_node = self.head
		while curr_node:
			print(curr_node.data)
			if curr_node.next == self.head:
				break
			curr_node= curr_node.next

	def __len__(self):
		curr_node = self.head
		count = 0
		while curr_node:
			count+=1
			if curr_node.next == self.head:
				return count
				break
			curr_node = curr_node.next
	def split_list(self):
		size = len(self)
		if size ==0:
			return None
		if size == 1:
			return self.head
		
		mid = size//2
		count = 0
		prev_node = None
		curr_node = self.head
		while curr_node and count < mid:
			count+=1
			prev_node = curr_node
			curr_node = curr_node.next
		prev_node.next = self.head
		
		split_clist = CircularLinkedList()
		while curr_node.next != self.head:
			split_clist.append(curr_node.data)
			curr_node = curr_node.next
		split_clist.append(curr_node.data)
		
		self.print_list()
		print("\n")
		split_clist.print_list()
	
	def josephus_circle(self, step):
		curr_node = self.head
		
		while len(self) > 1:
			count = 1
			while count != step:
				curr_node = curr_node.next
				count +=1
			print("REMOVED: "+ str(curr_node.data))
			self.remove(curr_node.data)
			curr_node = curr_node.next
			
	def is_circular_linked_list(self, input_list):
		p = input_list.head
		q = p.next
		while p != q:
			if p is not None and q is not None:
				p = p.next
				q = q.next.next
			else:
				return False
		return True	
		
				
clist = CircularLinkedList()
clist.append(1)
clist.append(2)
clist.append(3)
clist.append(4)
clist.prepend(0)
clist.prepend(-1)
clist.remove(2)
clist.remove(4)
print(f"Length: {len(clist)}")

clist.print_list()
print("\n")
print(clist.is_circular_linked_list(clist))
#clist.josephus_circle(2)
#clist.split_list()
#print(clist.head.next.next.next.next.next.next.data)
print("\n")
#clist.print_list()