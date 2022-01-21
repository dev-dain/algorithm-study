# 세로 R 가로 C
R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(input().strip())

# 방향벡터
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    ans = 1
    q = set([(x, y, graph[x][y])])
    
    while q:
        x, y, g = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<R and 0<=ny<C and graph[nx][ny] not in g:
                q.add((nx, ny, g + graph[nx][ny]))
                ans = max(ans, len(g)+1)
    return ans

print(bfs(0,0))