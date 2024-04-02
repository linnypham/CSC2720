from collections import deque
class Node:
# A function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
def smallestK(root,k):
    if root == None:
        return
    stack = deque()
    i = 0
    current = root
    while current or len(stack)>0:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            i += 1
            if i == k:
                return current.val
            current = current.right
    return False
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
print(smallestK(root,3))