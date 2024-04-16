#time: _(V+E)
#space: visiting, visited, call stack
def dfs(crs):
    if crs in visiting:
        return False
    if crs in visited:
        return True
    visiting.add(crs)
    for i in AL[crs]:
        if dfs(i)==False:
            return False
    visiting.remove(crs)
    visited.add(crs)
    TO.append(crs)
    return True
TO = [2,3,1,0,4,5]
PRL=[[0,1],[0,2],[1,3],[3,2],[4,0],[5,0]]
n = 6

AL = {i:[] for i in range(n)} # adjacency lists
for i,j in PRL:
    AL[i].append(j)
print(AL)
visiting = set()
visited = set()
TO = []

for c in range(n):
    if dfs(c)==False:
        print([])
print(TO)




