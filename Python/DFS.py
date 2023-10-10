#DFS 함수 선언
#인접한 노드들 중에서 가장 깊숙이 들어가는 탐색 기법 
#스택 자료구조, 별도 라이브러리 없이 append()와 pop()으로도 동작 가능
#First in Last out

def dfs(graph, v, visited):
    #최상단 노드를 방문으로 처리
    visited[v] = True
    
    print(v, end='')
    
    #방문하지 않은 노드가 있다면 재귀함수로 방문 처리 
    for i in range(v):
        if not invited[i]:
            dfs(graph, v, visited)
            
#graph 안에 2차원 리스트로 각 노드별 인접한 노드 선언
graph = [
    [],
    [2,3,8],
    .
    .
    ]

#각 노드가 방문한 정보를 visited에 선언
visited = [False]*9

#노드 '1'에 대한 dfs 함수 호출
dfs(graph, 1, visited)
