def prims(g):
    n = len(g)
    sel = [False] * n
    sel[0] = True
    for _ in range(n - 1):
        mn, x, y = float('inf'), 0, 0
        for i in range(n):
            if sel[i]:
                for j in range(n):
                    if not sel[j] and 0 < g[i][j] < mn:
                        mn, x, y = g[i][j], i, j
        print(f"{x} - {y} : {mn}")
        sel[y] = True

graph = [[0,2,0,6,0],[2,0,3,8,5],[0,3,0,0,7],[6,8,0,0,9],[0,5,7,9,0]]
prims(graph)