def find(parent, i):
    if parent[i]!=i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1    

def kruskal(v, edges):
    edges.sort(key=lambda x: x[2])
    parent,rank = [i for i in range(v)], [0] * v
    print("Edge : Weight")
    for u,v,w in edges:
        x,y = find(parent, u), find(parent, v)
        if x != y:
            union(parent, rank, x, y)
            print(f"{u} - {v} : {w}")
    print("ETC: O(E log E)")

edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5)
]
kruskal(5, edges)