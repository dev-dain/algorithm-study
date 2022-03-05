import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
    
# 초기 구름 위치
clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
for _ in range(m):
    d,s = map(int, input().split())
    
    move = []
    for idx in range(len(clouds)):
        x, y = clouds[idx]
        nx = (n + x + (dx[d-1]*s)) % n
        ny = (n + y + (dy[d-1]*s)) % n
        
        move.append((nx,ny)) #구름이 이동한 좌표
    
    # 구름의 위치를 확인하고 물 추가
    cloud_loc = [[False]*n for _ in range(n)]
    for i,j in move:
        graph[i][j] += 1
        cloud_loc[i][j] = True
        
    # 대각선의 위치를 탐색하기 위한 idx
    find = [1,3,5,7]
    for i,j in move:
        cnt = 0
        for f in find:
            fx, fy = i + dx[f], j + dy[f]
            
            if not 0<=fx<n or not 0<=fy<n: # 범위 밖인 경우
                continue
            if graph[fx][fy] == 0 : # 물이 없는 경우
                continue
            
            cnt += 1
        graph[i][j] += cnt
        
    clouds = [] # 새 구름 생성
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= 1: # 물 양이 1이면 제외
                continue
            if not cloud_loc[i][j]:
                clouds.append((i,j))
                graph[i][j] -= 2
print(sum(sum(graph, [])))


# 8개의 이동방향 중 s칸의 크기만큼 이동
# 물이 증가한 칸에서 대각서의 방향으로 거리가 1인칸의
# 0이 아닌 칸을 세서 더해주면된다

# 이후 2 이상인 모든 칸을 구하고 -2 해준다
# 이때 앞선 구름이 없던 칸이어야한다 
