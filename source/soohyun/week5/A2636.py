# 백준 2636 치즈
# https://www.acmicpc.net/problem/2636

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북동남서
ans = [] # 각 시간에 녹은 치즈 개수

def bfs(i, j):
    queue = deque([[i, j]])
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    cnt = 0 # 녹은 치즈 개수

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]: # 이동 가능한 범위이며 아직 방문하지 않은 경우
                if graph[nx][ny] == 1: # 가장 자리 치즈인 경우 녹은 상태로 변경
                    graph[nx][ny] = 0
                    cnt += 1
                else: # 공기인 경우 큐에 추가
                    queue.append([nx, ny])
                visited[nx][ny] = 1

    return cnt

while True:
    cnt = bfs(0, 0)
    
    if cnt == 0: # 녹은 치즈 개수가 0개인 경우 = 더 이상 녹을 치즈가 없는 경우
        break

    ans.append(cnt)

print(len(ans))
print(ans[-1])