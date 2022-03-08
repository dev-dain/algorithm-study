import sys
input = sys.stdin.readline

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
move = [list(map(int, input().split())) for _ in range(M)]
cloud = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]

for d, s in move:
  d -= 1
  water = []
  for x, y in cloud:
    nx = (x + (dx[d] * s)) % N
    ny = (y + (dy[d] * s)) % N
    board[nx][ny] += 1
    water.append((nx, ny))

  for x, y in water:
    cnt = 0
    for i in range(1, 8, 2):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue
      if board[nx][ny] == 0:
        continue
      cnt += 1
    board[x][y] += cnt
  
  cloud = []
  for x in range(N):
    for y in range(N):
      if board[x][y] >= 2 and (x, y) not in water:
        cloud.append((x, y))
        board[x][y] -= 2

res = 0
for row in board:
  res += sum(row)
print(res)