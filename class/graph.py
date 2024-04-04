#time: O(|v|+|E|)
#space: O(|v|)
from collections import deque
#depth-first search
def DFS(source,graph):
   DFS = []
   stack = deque()
   visited = set()
   stack.append(source)
   visited.add(source)
   while stack:
      item =stack.pop()
      DFS.append(item)
      for j in graph.get(item,[]):
         if j not in visited:
            stack.append(j)
            visited.add(j)
   return DFS

#Breadth-First Search
def BFS(source,graph):
   BFS = []
   q = deque()
   visited = set()
   q.append(source)
   visited.add(source)
   while q:
      item =q.popleft()
      BFS.append(item)
      for j in graph.get(item,[]):
         if j not in visited:
            q.append(j)
            visited.add(j)
   return BFS
graph = {1: [2,3],
         2: [4],
         3: [4,5],
         4: [2,6],
         5: [6],
         6: []}
output1 = DFS(1,graph)
output2 = BFS(1,graph)
print('DFS:')
print(output1)

