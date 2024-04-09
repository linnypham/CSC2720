def createGraph(edges, n):
    if n == None:
        return True

    al = {i: [] for i in range(n)}
    for n1, n2 in edges:
        al[n1].append(n2)
        al[n2].append(n1)
    return al

def DFS(node, prev, al):
    visited = set()
    if node in visited:
        return False
    visited.add(node)
    for i in al[node]:
        if i == prev:
            continue
        if not DFS(i, node, al):
            return False
    return True

n = 5
edges = [[0, 1],
         [0, 2],
         [0, 3],
         [1, 4]]

graph = createGraph(edges, n)

print(DFS(0, float("-inf"), graph))
