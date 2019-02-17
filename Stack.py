class Stack():
	def __init__(self):
		self.items=[]
	def is_empty(self):
		return len(self.items) == 0
	def push(self,item):
		self.items.append(item)
	def pop(self):
			return self.items.pop()
	def peek(self):
		if not self.is_empty:
			return self.items[-1]
	def size(self):
		return len(self.items)
	def __len__(self):
		return self.size()
	def get_stack(self):
		return self.items
		
def reverse(str):
	result = ''
	for char in str:
		stack.push(char)
	while not stack.is_empty():
		result += stack.pop()
	return result

def int_to_bin(value):
	result =''
	while value !=0:
		rem = value%2
		stack.push(rem)
		value = value//2
	while not stack.is_empty():
		result += str(stack.pop())
	return result
	
def balance_check(param):
	balance = True
	index = 0
	while index < len(param) and balance:
		par = param[index]
		if par in '([{':
			stack.push(par)
		else:
			if stack.is_empty():
				balance = False
			else:
				top = stack.pop()
				if not is_match(top,par):
					balance = False
		index+=1
	if stack.is_empty() and balance:
		return True
	else:
		return False
def is_match(p1,p2):
	if p1== '{' and  p2 =='}':
		return True
	elif p1== '[' and  p2 ==']':
		return True
	elif p1== '(' and  p2 ==')':
		return True
	else:
		return False
stack = Stack()
print(reverse("Hello"))
print(int_to_bin(242))
print(balance_check("{[}"))