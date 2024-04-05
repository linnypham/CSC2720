# Class to represent Tree node
class Node:
# A function to create a new node
def __init__(self, key):
    self.val = key
    self.left = None
    self.right = None
def validate(root):
    if root == None:
        return True
    stack = deque()
    stack.append((root,float('-inf'),float('inf')))
    while stack:
        node, lb, ub = stack.pop()
        if not (node.val > lb and node.val < ub):
            return False
        if node.left:
            stack.append((node.left,lb,node.val))
        if node.right:
            stack.append((node.right,node.val,ub))
    return True
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)