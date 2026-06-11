import sys

def prims(graph):
    v = len(graph)
    visited = [False] * v
    visited[0] = True
    print("Edge : Weight")
    for _ in range(v - 1):
        min_w,x,y = sys.maxsize,0,0
        for i in range(v):
            if visited[i]:
                for j in range(v):
                    if not visited[j] and graph[i][j] != 0:
                        if graph[i][j] < min_w:
                            min_w,x,y = graph[i][j],i,j
        visited[y] = True
        print(f"{x} - {y} : {graph[x][y]}")
    print("ETC: O(V^2)")

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],    
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]   
prims(graph)