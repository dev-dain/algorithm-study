# 백준 1261 알고스팟
# https://www.acmicpc.net/problem/1261

from collections import deque

m, n = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)] # 각 위치의 벽을 부시는 횟수
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북

def bfs():
    queue = deque([[0, 0]])
    dist[0][0] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1: # 이동 가능한 범위이며 아직 방문하지 않은 경우
                # 해당 위치가 벽이면 벽을 부시고 큐의 뒤에 삽입
                if board[nx][ny]:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append([nx, ny])
                # 해당 위치가 빈 방이면 바로 이동하고 큐의 앞에 삽입
                else:
                    dist[nx][ny] = dist[x][y]
                    queue.appendleft([nx, ny])

bfs()
print(dist[-1][-1])