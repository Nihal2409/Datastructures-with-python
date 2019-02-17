class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		
class LinkedList:
	
	def __init__(self):
		self.head = None
		self.length = 0
	def print_list(self):
		curr_node = self.head
		while curr_node:
			print(curr_node.data)
			curr_node = curr_node.next
			
	def append(self,data):
		new_node = Node(data)
		#looking for null value if it is encountered, then insert the node
		if self.head is None:
			self.head = new_node
			self.length +=1
			return
		#traversing through the linkedlist to find the null node
		last_node = self.head
		while last_node.next is not None:
			last_node = last_node.next
		last_node.next = new_node
		self.length +=1
		
	def delete_node(self,data):
		curr_node = self.head
		# when we are deleting the head itself
		if curr_node.data == data:
			self.head = curr_node.next
			curr_node == None
			self.length -=1
			return
		# When we are deleting which is not the head
		prev_node = None
		while curr_node.data != data:
			prev_node = curr_node
			curr_node = curr_node.next
		prev_node.next = curr_node.next
		curr_node = None
		self.length -=1
		
	def delete_node_at_pos(self,pos):
		curr_node = self.head
		if pos == 0:
			self.head = curr_node.next
			curr_node = None
			self.length -=1
			return
		
		prev_node = None
		count = 0
		while curr_node and count != pos:
			prev_node = curr_node
			curr_node = curr_node.next
			count += 1
		if curr_node is None:
			print("Position exceeds the number of elements in the list")
		
		prev_node.next = curr_node.next
		curr_node = None
		self.length -=1
		
	def prepend(self,data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
		self.length +=1
		
	def insert_after_node(self,prev_node,data):
		new_node = Node(data)
		curr_node = self.head
		while curr_node.data != prev_node:
			curr_node = curr_node.next
		new_node.next = curr_node.next
		curr_node.next = new_node
		self.length +=1
		
	def swap_nodes(self,key_1,key_2):
		if key_1 == key_2:
			return
		prev_1 = None
		curr_1 = self.head
		while curr_1 and curr_1.data != key_1:
			prev_1 = curr_1
			curr_1 = curr_1.next
		prev_2 = None
		curr_2 = self.head
		while curr_2 and curr_2.data != key_2:
			prev_2 = curr_2
			curr_2 = curr_2.next
		
		if not curr_1 or not curr_2:
			return
			
		if prev_1:
			prev_1.next = curr_2
		else:
			self.head = curr_2
		if prev_2:
			prev_2.next = curr_1
		else:
			self.head = curr_1
		
		curr_1.next, curr_2.next = curr_2.next, curr_1.next
		
	def reverse_iterative(self):
		prev_node = None
		curr_node = self.head
		while curr_node is not None:
			temp_node = curr_node.next	
			curr_node.next = prev_node				
			prev_node = curr_node
			curr_node = temp_node
		self.head = prev_node

	#original list:
	# 1-> 6 ->1 ->7
	#remove duplicates
	# 1->6->7
	def remove_duplicates(self):
		curr_node = self.head
		prev_node = None
		dup_values = dict()
		while curr_node:
			if curr_node.data in dup_values.keys():
				#Remove the duplicates
				prev_node.next = curr_node.next
				curr_node = None
				self.length -=1
			else:
				dup_values[curr_node.data] = 1
				prev_node = curr_node
			curr_node = prev_node.next

	# Print the Nth node from the last node
	def print_nth_from_last(self,n):
		#Method 1
		"""
		curr_node = self.head
		count = self.length
		while curr_node and count != n:
			count -=1
			curr_node = curr_node.next
		print(f"The node which is at nth position from the last is {curr_node.data}")"""
		
		#Method 2
		p = self.head
		q = self.head
		count = 0
		while q and count < n:
			q=q.next
			count+=1
		if not q:
			print(str(n)+ " is greater than the number of nodes in the list")
			return
		while p and q:
			p = p.next
			q = q.next
		print( str(p.data) + " is the value at the nth position from last" )
		
	#Rotate the list at kth position
	#1->2->3->4->5->6 k = 4
	#new list
	#5->6->1->2->3->4->NULL
	def rotate(self,k):
		p = self.head
		q = self.head
		prev_node = None
		count = 0
		while p and count<k:
			prev_node = p
			p = p.next
			q = q.next
			count +=1
		p = prev_node
		while q:
			prev_node = q
			q = q.next
		q = prev_node
		
		q.next = self.head
		self.head = p.next
		p.next = None
	
	def is_palindrome(self):
		# Method 1:
		curr_node = self.head
		word=''
		while curr_node:
			word += curr_node.data
			curr_node = curr_node.next
		return word == word[::-1]
		
	def sum_two_list(self,llist):
		p = self.head
		q = llist.head
		sum_list = LinkedList()
		carry = 0
		while p or q:
			if not p:
				i = 0
			else:
				i = p.data
			if not q:
				j = 0
			else:
				j = q.data
			s = i+j+carry
			if s>=10:
				carry = 1
				remainder = s%10
				sum_list.append(remainder)
			else:
				carry = 0
				sum_list.append(s)
			if p:
				p = p.next
			if q:
				q = q.next
		
	
llist = LinkedList()
"""
llist.append(12)
llist.append(24)
llist.append(31)
llist.prepend(6)
llist.prepend(3)
llist.insert_after_node(12,18)
llist.delete_node(3)
llist.delete_node(18)
llist.delete_node_at_pos(1)
llist.delete_node_at_pos(2)
llist.append(32)
llist.swap_nodes(6,24)
llist.swap_nodes(6,24)
llist.print_list()
print("\n")
llist.reverse_iterative()
llist.append(32)
llist.append(64)
llist.append(96)
llist.remove_duplicates()
llist.print_nth_from_last(2)
#llist.print_nth_from_last(3)
"""

#for rotating inputs
"""
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6) """

#for palindrome check
"""
llist.append('R')
llist.append('A')
llist.append('D')
llist.append('A')
llist.append('R')
print(llist.is_palindrome())"""



llist.print_list()
#llist.rotate(3)
print("\n")
#llist.print_list()
print(f"Length of the list is: {llist.length}")
	