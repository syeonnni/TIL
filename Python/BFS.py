#BFS 함수 선언
#인접한 노드들 중에서 가까운 노드들부터 탐색하는 기법 
#큐 자료구조, collections&deque 라이브러리
#First in First out 

from collections import deque

def bfs(graph, start, visited):
    #큐 구현을 위해 deque 라이브러리 사용 
    queue = deque([start])

    #현재 노드를 방문 처리 
    visited[start]= True

    #큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end='')

        #방문하지 않은 노드가 있다면 큐에 삽입하고 방문 처리 
        for i in range(v):
            if not visited[v]:
                queue.append(i)
                visited[i] = True

#graph 안에 2차원 리스트로 각 노드별 인접한 노드 선언 
graph = [
    [],
    [2,3,8]
    .
    .
    ]

#각 노드가 방문한 정보를 visited에 선언
visited = [False]*9

#BFS 함수 호출
bsf(graph, 1, visited)
