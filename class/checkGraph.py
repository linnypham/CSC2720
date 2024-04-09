def createGraph(edges,n):
    if n == None:
        return True
    visited = set()
    al = {i: [] for i in range(n)}
    for n1, n2 in edges:
        al[n1].append(n2)
        al[n2].append(n1)
        return al
def DFS(node,prev):
    if node in visited:
        return False
    visited.add(node)
    for i in al[node]:
        if i in visited:
            return False
        if i == prev:
            continue
        if not DFS(i,node):
            return False
    return True
    return(DFS(0,float("-inf") and (n==len(visited))))

n = 5
edges = [[0,1],
         [0,2],
         [0,3],
         [1,4]]
print(createGraph(edges,n))