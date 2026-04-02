class Node:
	def __init__(self, data, prev = None, next_ = None):
		self.data = data
		self.prev = prev
		self.next = next_

head = None

def append(value):
	node = Node(value)
	global head
	if head is None:
		head = node
	else:
		p = head
		while p.next is not None:
			p = p.next
		node.prev = p
		p.next = node

def insert(ptr, value):
	global head
	if ptr is None:
		append(value)
	else:
		p = ptr.prev
		node = Node(value, p, ptr)
		ptr.prev = node
		if ptr == head:
			head = node
		else:
			p.next = node

def delete(ptr):
	global head
	if ptr is None:
		return
	if ptr == head:  # 刪除head節點
		head = head.next
		head.prev = None
	else:
		p = ptr.prev
		p.next = ptr.next
		if ptr.next is not None:
			p.next.prev = p

def find(value):
	p = head
	while p is not None:
		if p.data == value:
			return p
		p = p.next
	return p

def traverse_next():
	print("[", end="")
	p = head
	while p is not None:
		if p == head:
			print(p.data, end="")
		else:
			print(",", p.data, sep="", end="")
		p = p.next
	print("]")

def traverse_prev():
	print("[", end="")
	if head is not None:
		p = head
		while p.next is not None:
			p = p.next
		print(p.data, end="")
		while p.prev is not None:
			p = p.prev
			print(",", p.data, sep="", end="")
	print("]")

def size():
	count = 0
	p = head
	while p is not None:
		count += 1
		p = p.next
	return count

traverse_next()
traverse_prev()
append(54)
append(12)
append(30)
append(25)
ptr_ = find(30)
insert(ptr_, 67)
traverse_next()
traverse_prev()
print("Have", size(), "nodes")
ptr_ = find(30)
delete(ptr_)
traverse_next()
traverse_prev()
print("Have", size(), "nodes")
