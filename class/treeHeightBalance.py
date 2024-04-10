from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def checkBalance(self):
        def dfs(root):
            if root is None:
                return [True,0]
            lst = dfs(root.left)
            rst = dfs(root.right)
            balance = (lst[0] and rst[0]) and (abs(lst[1]-rst[1])<=1)
            return [balance,1+max(lst[1],rst[1])]
        return dfs(root)[0]
    def heightCheck(self):
        if root == None:
            return 0
        stack = deque()
        height = 0
        stack.append([root,1])
        while stack:
            node,currentDepth = stack.pop()
            height = max(height,currentDepth)
            if node.left:
                stack.append([node.left,1+currentDepth])
            if node.right:
                stack.append([node.right,1+currentDepth])
        return height

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.left.left.left = Node(5)
output = root.checkBalance()
print(output)
output2 = root.heightCheck()
print(output2)