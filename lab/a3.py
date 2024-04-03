from collections import deque
class Node:
# A function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
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
            IOT.append(current.data) #append data in IOT list
            current = current.right # move right
    return IOT
def smallestNode(root): #find the node with lowest data
    current = root
    while current.left: #keep  going the the left of left subtree to find smallest data
        current = current.left
    return current
def deleteRoot(root):
    smallNode = smallestNode(root.right) #find the smallest data of right subtree of the root
    root.data = smallNode.data #replace root data with new data
    current = root.right
    while current.left.data != root.data: #delete smallNode
        current = current.left
    current.left = None

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
print(f'Before delete Root {root.data}:')
output = inOrder(root)
print(output)
print(f'After delete Root {root.data}:')
deleteRoot(root)
output = inOrder(root)
print(output)


'''test1: Node is null
root = Node()
root.left = Node()
root.right = Node()
deleteRoot(root)
output = levelOrder(root)
print(output)

test2: Node is string
root = Node('a')
root.left = Node('b')
root.right = Node('c')
deleteRoot(root)
output = levelOrder(root)
print(output)

test3: Node is string and int
root = Node('a')
root.left = Node(3)
root.right = Node('c')
deleteRoot(root)
output = levelOrder(root)
print(output)

test4: Node is Null and String and Int
root = Node('a')
root.left = Node(3)
root.right = Node()
deleteRoot(root)
output = levelOrder(root)
print(output)'''