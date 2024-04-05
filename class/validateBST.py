from collections import deque
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
    stack.append((root,float('-inf'),float('inf')))#append root, negative infinity for lower bound, infinity for upper bound
    while stack:
        node, lb, ub = stack.pop()
        if not (node.val > lb and node.val < ub):#if node violate BTS standard, return False
            return False
        if node.left:
            stack.append((node.left,lb,node.val))#set current node as new upper bound
        if node.right:
            stack.append((node.right,node.val,ub))#set current node as new lower bound
    return True
def inOrder(root): #In-order traversal
    IOT = [] #traversal list
    cs = deque() #call stack
    current = root
    while current or len(cs) > 0:
        if current:
            cs.append(current) #append data in call stack
            current = current.left # move left
        else:
            current = cs.pop() #pop data in call stack
            IOT.append(current.val) #append data in IOT list
            if sorted(IOT) != IOT:  # check if IOT list is in ascending order
                return False
            current = current.right # move right
    return True

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
print(f'Validate BTS: {validate(root)}')
print(f'IOT: {inOrder(root)}')
'''test1: Node is null
root = Node()
root.left = Node()
root.right = Node()
print(f'Validate BTS: {validate(root)}')
print(f'IOT list: {inOrder(root)}')

test2: Node is string
root = Node('a')
root.left = Node('b')
root.right = Node('c')
print(f'Validate BTS: {validate(root)}')
print(f'IOT list: {inOrder(root)}')

test3: Node is string and int
root = Node('a')
root.left = Node(3)
root.right = Node('c')
print(f'Validate BTS: {validate(root)}')
print(f'IOT list: {inOrder(root)}')

test4: Node is Null and String and Int
root = Node('a')
root.left = Node(3)
root.right = Node()
print(f'Validate BTS: {validate(root)}')
print(f'IOT list: {inOrder(root)}')'''