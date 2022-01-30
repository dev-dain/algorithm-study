import sys
input = sys.stdin.readline

# 세로 n 가로 m
n, m  = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(n) ]
visited = [[False]*m for _ in range(n)]
answer = 0

# 상우하좌
move = ((-1, 0), (1, 0), (0, -1), (0, 1))

def dfs(x,y,value,length):
    global answer
    
    if length >= 4:
        answer  = max(answer, value)
        return 
    
    for d in move:
        nx = x + d[0]
        ny = y + d[1]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny] = True
            
            # 다음 지점 호출
            dfs(nx, ny, value + graph[nx][ny], length+1)
            visited[nx][ny] = False

def exception_shape(x, y, value):
    # ㅗㅜㅏㅓ 체크
    global answer
    # ㅗ
    if 0<=x+2<n and 0<= y+1<m:
        value = graph[x][y] + graph[x+1][y] + graph[x+1][y+1] + graph[x+2][y]
        answer = max(answer, value)
    # ㅜ
    if 0<=x-1 and x+1<n and 0<=y+1<m:
        value = graph[x-1][y+1] + graph[x][y+1] + graph[x][y] + graph[x+1][y+1]
        answer = max(answer, value)
    # ㅏ
    if 0<=x+1<n and 0<=y+2<m:
        value = graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x+1][y+1]
        answer = max(answer, value)
    # ㅓ
    if 0<=x-1 and x<n and 0<=y+2<m:
        value = graph[x][y] + graph[x-1][y+1] + graph[x][y+1] + graph[x][y+2]
        answer = max(answer, value)

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j, graph[i][j], 1)
        visited[i][j] = False
        
        exception_shape(i,j, graph[i][j])
print(answer)