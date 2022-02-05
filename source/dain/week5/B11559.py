# 겹치는 것인지 아닌지는 어떻게 알까?
# 전체적인 좌표를 하나 둬야할까
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
location = []
visited = [[0 for _ in range(6)] for _ in range(12)]
def bfs(color, x, y):
  qu = deque([[x, y]])
  delete = [[x, y]]

  while qu:
    x, y = qu.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:
        continue
      if field[nx][ny] != color or visited[nx][ny]:
        continue
      visited[nx][ny] = 1
      qu.append([nx, ny])
      if [nx, ny] not in delete:
        delete.append([nx, ny])
  return [] if len(delete) < 4 else delete

field = [list(input()) for _ in range(12)]
d_row = 0
combo = 0
while True:
  d = []
  location = []
  visited = [[0 for _ in range(6)] for _ in range(12)]
  add = 0
  for i in range(d_row, 12):
    if field[i] == ['.', '.', '.', '.', '.', '.',]:
      d_row += 1
      visited[i] = [1, 1, 1, 1, 1, 1]
      continue

    for j in range(6):
      if field[i][j] == '.' or visited[i][j] or [i, j] in location:
        continue
      color = field[i][j]
      visited[i][j] = 1
      delete = bfs(color, i, j)
      if not delete:
        continue
      d.append(delete)
      location += delete
  
  if not d:
    break
  
  for delete in d:
    for x, y in delete:
      if x == 0:
        field[x][y] = '.'
        continue
      while field[x][y] != '.' and x > 0:
        field[x][y] = field[x-1][y]
        x -= 1
      field[0][y] = '.'
  
  combo += 1
print(combo)