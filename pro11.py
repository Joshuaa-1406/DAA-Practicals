def find(p, i):
    while p[i] != i: i = p[i]
    return i

def kruskal(n, edges):
    p = list(range(n))
    mst = []
    for u, v, w in sorted(edges, key=lambda x: x[2]):
        a, b = find(p, u), find(p, v)
        if a != b:
            p[a] = b
            mst.append((u, v, w))
    return mst

edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
print("edges : weight")
for u, v, w in kruskal(4, edges):
    print(f"{u} - {v} : {w}")