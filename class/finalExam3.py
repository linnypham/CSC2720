from collections import deque
class Node:
# A function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def smallestK(root, k):
    if root == None:
        return
    stack = deque()
    i = 0 #counter
    current = root
    while current or len(stack) > 0:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            i += 1 #increment
            if i == k:#return if counter is met
                return current.data
            current = current.right
    return False

def smallestKrecursive(root, k):
    def inorder(node):
        if node is None or count >= k:
            return
        inorder(node.left)
        count += 1
        if count == k:
            result = node.data
            return root.data
        inorder(node.right)


root = Node(400)
root.left = Node(200)
root.right = Node(600)
root.left.left = Node(100)
root.left.right = Node(300)
root.right.left = Node(500)
root.right.right = Node(700)
print(smallestK(root,3))
print(smallestKrecursive(root,3))