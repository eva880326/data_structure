class Node:
	def __init__(self, data, next_ = None):
		self.data = data
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
		p.next = node

def insert(ptr, value):
	global head
	if ptr is None:
		append(value)
	else:
		node = Node(value, ptr)
		node.next = ptr
		if ptr == head:
			head = node
		else:
			p = head
			while p.next != ptr:
				p = p.next
			p.next = node

def delete(ptr):
	global head
	if ptr is None:
		return
	if ptr == head:  # 第一種情況: 刪除第一個節點
		head = head.next
	else:
		p = head
		while p.next != ptr:  # 找節點ptr的前節點
			p = p.next
		p.next = ptr.next

def find(value):
	p = head
	while p is not None:
		if p.data == value:
			return p
		p = p.next
	return p

def traverse():
	print("[", end="")
	p = head
	while p is not None:
		if p != head:
			print(",", end="")
		print(p.data, end="")
		p = p.next
	print("]")

def size():
	count = 0
	p = head
	while p is not None:
		count += 1
		p = p.next
	return count

traverse()
append(54)
append(12)
append(30)
append(25)
ptr_ = find(30)
insert(ptr_, 67)
traverse()
print("Have", size(), "nodes")
ptr_ = find(30)
delete(ptr_)
traverse()
print("Have", size(), "nodes")
