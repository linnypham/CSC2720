from collections import deque
class TreeNode:
# A function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

'''
def inOrder(root):#recursive
    list = []
    if root == None:
        return
    else:
        inOrder(root.left)
        list.append(root.val)
        inOrder(root.right)
    return list
'''
def inOrder(root):  #interative
    IOT = []
    cs = deque()
    current = root
    while current or len(cs) > 0:
        if current:
            cs.append(current)
            current = current.left
        else:
            current = cs.pop()
            IOT.append(current.val)
            current = current.right
    return IOT

def levelOrder(root):
    LOT = []
    q = deque()
    q.append(root)
    while q:
        a_node = q.popleft()
        LOT.append(a_node.val)
        if a_node.left:
            q.append(a_node.left)
        if a_node.right:
            q.append(a_node.right)
    return LOT

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(levelOrder(root))

