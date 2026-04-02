class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

root = None

def insert(value):
    global root
    node = Node(value, None, None)
    if root is None:
        root = node
    else:
        ptr = root
        prev = None
        while ptr is not None:
            prev = ptr
            ptr = ptr.left if value < ptr.data else ptr.right
        if value < prev.data:
            prev.left = node
        else:
            prev.right = node

def delete(value):
    global root
    if root is None:
        return
    ptr = root
    prev = None
    while ptr is not None and ptr.data != value:  # ptr指向要刪除的節點
        prev = ptr
        ptr = ptr.left if value < ptr.data else ptr.right

    if ptr is None:
        return
    if ptr.left is None and ptr.right is None:
        if value > prev.data:
            prev.right = None
        if value < prev.data:
            prev.left = None
    else:
        if ptr.left is None:
            p = ptr.right
        elif ptr.right is None:
            p = ptr.left
        else:  # 刪除節點有左右樹,將刪除節點右樹成為左樹最大值的右樹
            p = ptr.left
            lp = ptr.left
            rp = ptr.right
            while lp.right is not None:
                lp = lp.right
            lp.right = rp

        if ptr == root:  # 刪除節點為root
            root = p
        else:
            if value < prev.data:
                prev.left = p
            else:
                prev.right = p

def preorder(_root):
    if _root is not None:
        print(_root.data, end=" ")
        preorder(_root.left)
        preorder(_root.right)

def inorder(_root):
    if _root is not None:
        inorder(_root.left)
        print(_root.data, end=" ")
        inorder(_root.right)

def postorder(_root):
    if _root is not None:
        postorder(_root.left)
        postorder(_root.right)
        print(_root.data, end=" ")

arr = [41, 67, 34, 0, 69, 24, 78, 58, 62, 64, 5, 45, 81, 27, 61]
print("原始數列:", end=" ")
for i in range(len(arr)):
    insert(arr[i])
    print(arr[i], end=" ")

print("\n前序:", end=" ")
preorder(root)
print("\n中序:", end=" ")
inorder(root)
print("\n後序:", end=" ")
postorder(root)
delete(61)
print("\n刪除後中序:", end=" ")
inorder(root)
