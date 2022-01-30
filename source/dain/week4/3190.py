from collections import deque

N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
K = int(input())
for _ in range(K):
  x, y = map(int, input().split())
  x, y = x-1, y-1 # (0, 0)을 시작점으로 할 수 있도록 좌표 줄여주기
  board[x][y] = 1 # 사과를 놓는다

# 방향
L = int(input())
rotate = deque([])
for _ in range(L):
  x, c = input().split()  # 초, 회전 방향 받기
  x = int(x)
  rotate.append((x, c))

# 동남서북 (0, 1, 2, 3) 순서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

snake = [(0, 0)] # 뱀은 길이가 늘어날 수 있으므로 리스트로 함
sec = 0 # 초
d = 0 # 방향

while True:
  # print(snake, sec)
  if rotate and sec == rotate[0][0]:
    if rotate[0][1] == 'D':
      d = (d + 1) % 4
    else:
      d = (d - 1) % 4
    rotate.popleft()

  x, y = snake[-1]
  x, y = x + dx[d], y + dy[d]

  if x < 0 or x >= N or y < 0 or y >= N:
    break
  if (x, y) in snake:
    break

  if board[x][y] == 1:
    snake.append((x, y))
    sec += 1
    board[x][y] = 0
    continue

  for i in range(len(snake)-1):
    snake[i] = snake[i+1][0], snake[i+1][1]

  snake[-1] = (x, y) 
  sec += 1

print(sec + 1)