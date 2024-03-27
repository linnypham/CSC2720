from collections import deque
class TreeNode:
    def __init__(self,left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val

'''
def inOrder(root):#recursive
    list = []
    if root == None:
        return
    else:
        inOrder(root.left)
        list.append(root.val)
        inOrder(root.right)
    inOrder(root)
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