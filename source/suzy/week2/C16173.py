from collections import deque

n = int(input())
graph = []
for _ in range(n): 
    graph.append(list(map(int, input().split())))

visited = [[0]*n for _ in range(n)]
# 오른쪽 아래 방향벡터
dx = [1,0]
dy = [0,1]

# bfs
def bfs():
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    
    while q:
        x, y = q.popleft()
        
        if graph[x][y] == -1:
            print("HaruHaru")
            return
        
        add = graph[x][y]
        
        for i in range(2):
            nx = x + dx[i] * add
            ny = y + dy[i] * add
            
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
    print("Hing")

bfs()