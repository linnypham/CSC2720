from collections import deque
class TreeNode:
    def __init__(self,left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val

    def biSearchTree(self,root,data):
        pass

    def insert(self,root,data):
        pass

    def validate(self,node,lower,upper):
        if node == None:
            return True
        if not (node.val>lower and node.val<upper):
            return False
        return (validate(node.left,lower,node.val)
                and validate(node.right,node.val,right))

validate(root,float("-inf"),float("inf"))
