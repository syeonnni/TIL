#최단경로_다익스트라 알고리즘
#빠르게 입력 받기 
import sys
input = sys.stdin.readline
#무한으로 10억 설정
INF = int(1e9)
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
#방문한 적이 있는지 체크하는 visited 리스트 초기화
visited = [False]*(n+1)
#최단거리 무한으로 초기화
distance = [INF]*(n+1)

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

    def smallest_node():
        min_value = INF
        index = 0
        for i in range(1, n+1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index

    def dijkstra(start):
        distance[start] = 0
        visited[start] = True
        for j in graph[start]:
            distance[j[0]] = j[1]

        for i in range(n-1):
            now = smallest_node()
            visited[now] = True

            for j in graph[now]:
                cost = distance[now]+j[1]

                if cost < distance[j[0]]:
                    distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
