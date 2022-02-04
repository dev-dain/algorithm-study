from collections import deque
import sys
input = sys.stdin.readline
# 세로 가로
n, m = map(int, input().split())

graph = [ list(map(int, input().split())) for _ in range(n)]

# 동서남북
dx = [1,-1,0,0]
dy = [0,0,-1,1]

day = 0
check = False

# bfs
def bfs(i,j):
    q = deque()
    q.append((i,j))
    
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] !=0 and visited[nx][ny] == False:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                elif graph[nx][ny] == 0:
                    count[x][y] += 1
    return 1

# 빙산이 분리될 때까지 반복
while True:
    visited = [[False]*m for _ in range(n)]
    count = [[0]*m for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == False:
                result.append(bfs(i,j))
                
    # 빙산 깎기
    for i in range(n):
        for j in range(m):
            graph[i][j] -= count[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
    
    # 다 녹을때까지 분리되지 않으면
    if len(result) == 0:
        break
    # 빙산이 분리되면
    if len(result) >=2:
        check = True
        break
    day += 1
    
if check:
    print(day)
else:
    print(0)