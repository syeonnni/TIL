#음료수 얼려먹기
n, m = map(int, input().split())

#2차원 리스트로 정보 받기 
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#DFS함수 선언
def dfs(x,y):
    #입력받은 틀보다 넘어선다면 종료 
    if x <= -1 or x >= n or y <= 1 or y >= m:
        return False

    #현재 노드를 방문하지 않았다면, 방문 처리
    if graph[x][y] == 0:
        graph[x][y] = 1

        #DFS = 재귀 함수로 표현 
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            return += 1

print(result)

