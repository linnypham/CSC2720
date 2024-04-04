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
'''
def DFS_recursive(source, graph, visited=None):
    if visited is None:
        visited = set()
    visited.add(source)
    for neighbor in graph.get(source, []):
        if neighbor not in visited:
            DFS_recursive(neighbor, graph, visited)
    return visited'''
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
source = 1
output1 = DFS(source,graph)
output2 = BFS(source,graph)
print('DFS:')
print(output1)
print('BFS:')
print(output2)
