# 플로이드 워셜 알고리즘
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    #a에서 b로 가는 비용은 c
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("infinity", end='')

        else:
            print(graph[a][b], end='')

    print()
