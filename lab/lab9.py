from collections import deque
class Node:
    def __init__(self, key): #initialize nodes
        self.data = key
        self.left = None
        self.right = None
def levelOrder(root):
    LOT = []    #create array for traversal
    q = deque() #create queue
    q.append(root)  #root as the first number
    while q:
        a_node = q.popleft() #pop the number in queue, put in a variable
        LOT.append(a_node.data) #put value of the variable into the LOT
        if a_node.left: #put value of left subtree, then right subtree in queue
            q.append(a_node.left)
        if a_node.right:
            q.append(a_node.right)
    return LOT

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

output = levelOrder(root)
print(output)

'''test1: Node is null
root = Node()
root.left = Node()
root.right = Node()
output = levelOrder(root)
print(output)

test2: Node is string
root = Node('a')
root.left = Node('b')
root.right = Node('c')
output = levelOrder(root)
print(output)

test3: Node is string and int
root = Node('a')
root.left = Node(3)
root.right = Node('c')
output = levelOrder(root)
print(output)

test4: Node is Null and String and Int
root = Node('a')
root.left = Node(3)
root.right = Node()
output = levelOrder(root)
print(output)'''