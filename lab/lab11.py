from collections import deque
class Graph:
    def __init__(self,V): # Constructor
        self.V = V # No. of vertices
        self.adj = [[] for i in range(V)] # adjacency lists
    def addEdge(self,v, w): # to add an edge to graph
        self.adj[v].append(w) # Add w to the list of v.

    def DFS_recursive(self,source, visited=None,DFS=None):
        if visited is None: #create set to check for visited nodes
            visited = set()
        if DFS is None:
            DFS = [source]
        visited.add(source) #source at the beginning
        for j in self.adj[source]:
            if j not in visited: #if the node is not visited yet, visit it
                DFS.append(j)
                self.DFS_recursive(j, visited,DFS)
        return DFS

    def DFS(self,source):
        DFS = []
        stack = deque()
        visited = set()
        stack.append(source) #source at the beginning
        visited.add(source) #visit stack first
        while stack:
            item = stack.pop()
            DFS.append(item)
            for j in self.adj[item]:
                if j not in visited: #if note is not visited, visit it
                    stack.append(j)
                    visited.add(j)
        return DFS
g = Graph(6)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(4, 5)
g.addEdge(1, 3)
g.addEdge(3, 5)
source = 0

print(f'Recursion: {g.DFS_recursive(source)}')
print(f'Stack: {g.DFS(source)}')
'''
# Test 1: Source is None
g = Graph(None)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(4, 5)
g.addEdge(1, 3)
g.addEdge(3, 5)
source = None
print(f'Recursion: {g.DFS_recursive(source)}')
print(f'Stack: {g.DFS(source)}')

# Test 2: Vertices are string
g = Graph(6)
g.addEdge('A', 'B')
g.addEdge('A', 2)
g.addEdge(2, 'C')
g.addEdge(2, 'D')
g.addEdge('D', 'E')
g.addEdge('B', 'C')
g.addEdge('C', 'E')
source = 'A'
print(f'Recursion: {g.DFS_recursive(source)}')
print(f'Stack: {g.DFS(source)}')

# Test 3: Only root
g = Graph(1)
g.addEdge(0, None)
print(f'Recursion: {g.DFS_recursive(0)}')
print(f'Stack: {g.DFS(0)}')

# Test 4: Vertices are zero
g = Graph(6)
g.addEdge(0, 0)
g.addEdge(0, 0)
g.addEdge(0, 0)
g.addEdge(0, 0)
g.addEdge(0, 0)
g.addEdge(0, 0)
g.addEdge(0, 0)
source = 0
print(f'Recursion: {g.DFS_recursive(source)}')
print(f'Stack: {g.DFS(source)}')
'''