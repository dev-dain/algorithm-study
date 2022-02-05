from collections import deque

N, M = map(int, input().split())
arctic = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
# 결국 굴복하고 melt도 N*M 크기로 만들어서 BFS에서 한 번에 돌기로..
# 하...
melt = [[0 for _ in range(M)] for _ in range(N)]
year = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
  qu = deque([[x, y]])
  visited[x][y] = 1

  while qu:
    x, y = qu.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      if arctic[nx][ny] and not visited[nx][ny]:
        visited[nx][ny] = 1
        qu.append([nx, ny])
      elif not arctic[nx][ny]:
        melt[x][y] += 1

while True:
  visited = [[0 for _ in range(M)] for _ in range(N)]
  melt = [[0 for _ in range(M)] for _ in range(N)]
  cnt = 0
  for x in range(N):
    for y in range(M):
      if arctic[x][y] and not visited[x][y]:
        bfs(x, y)
        cnt += 1

  for x in range(N):
    for y in range(M):
      arctic[x][y] -= melt[x][y]
      if arctic[x][y] < 0:
        arctic[x][y] = 0

  if not cnt:
    year = 0
    break
  if cnt > 1:
    break
  year += 1
print(year)