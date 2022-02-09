# 백준 2573 빙산
# https://www.acmicpc.net/problem/2573

from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
ans = 0 # 빙산이 분리되는 시간
flag = False # 빙산이 분리되는지 체크

# 빙산 녹이기
def melt():
    height = [[0] * M for _ in range(N)] # 빙산의 녹은 높이

    # 빙산의 녹은 높이 구하기
    for x in range(N):
        for y in range(M):
            if graph[x][y] != 0:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                        height[x][y] -= 1

    # 녹은 높이만큼 빙산 높이 변경
    for x in range(N):
        for y in range(M):
            if graph[x][y] + height[x][y] < 0: # 높이는 0보다 더 줄어들 수 없다
                graph[x][y] = 0
            else:
                graph[x][y] += height[x][y]

# 빙산 덩어리 구하기
def bfs(i, j):
    queue = deque([[i, j]])
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] != 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1

while True:
    melt() # 빙산 녹이기

    cnt = 0
    visited = [[0] * M for _ in range(N)]

    # 빙산 덩어리 구하기
    for x in range(N):
        for y in range(M):
            if not visited[x][y] and graph[x][y] != 0:
                bfs(x, y)
                cnt += 1

    ans += 1

    if cnt == 0: # 빙산이 다 녹을 때까지 분리되지 않는 경우
        flag = True
        break

    if cnt >= 2: # 빙산의 덩어리가 2이상인 경우
        break

print(0) if flag else print(ans)