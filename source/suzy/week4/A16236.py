from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,-1,0,1]
dy = [1,0,-1,0]

# bfs
def bfs(x, y):
    shark = 2 # 현재 아기상어 크기
    eat = 0
    time = 0
    eat_flag = False  # 현재 상태에서 물고기를 먹은 경우
    
    ans = 0
    
    q = deque([(x, y)])
    visited = set([(x, y)])
    
    while q:
        size = len(q)
        
        # 위 그리고 왼쪽이 우선
        q = deque(sorted(q))
        
        for _ in range(size):
            x, y = q.popleft()
            
            # 현재 위치에 아기상어보다 작은 물고기 존재
            if graph[x][y] != 0 and graph[x][y] < shark:
                eat += 1
                graph[x][y] = 0
                
                # 아기상어 크기만큼 먹은 경우 : 초기화 후 상어 크기 + 1
                if shark == eat:
                    eat = 0
                    shark += 1
                
                # 현재 위치를 기준으로 다시 탐색
                # BFS queue visited 초기화
                q = deque()
                visited = set([(x,y)])
                eat_flag = True
                
                # 먹었을때 시간을 저장
                ans = time
                
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<n and (nx,ny) not in visited:
                    if graph[nx][ny] <= shark:
                        q.append((nx,ny))
                        visited.add((nx,ny))
            
            # 현재 위치에서 먹었다면 더이상 반복문 x
            if eat_flag:
                eat_flag = False
                break    
        time += 1
    return ans

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            sx, sy = i ,j
            graph[i][j] = 0

print(bfs(sx, sy))