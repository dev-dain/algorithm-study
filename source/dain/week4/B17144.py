from collections import deque

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
machine = []

for _ in range(T):
  dust = []
  diffuse = []
  # 먼지 위치 확보
  for i in range(R):
    for j in range(C):
      if not room[i][j]:
        continue
      if room[i][j] == -1:
        machine.append([i, j])
        continue
      dust.append([i, j])

  # 먼지 확산과 남은 양 측정
  for x, y in dust:
    if room[x][y] < 5:
      continue
    cnt = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= R or ny < 0 or ny >= C:
        continue
      # 공기청정기 쪽으로는 확산 X
      if room[nx][ny] == -1:
        continue
      diffuse.append([nx, ny, room[x][y] // 5])
      cnt += 1
    room[x][y] = room[x][y] - ((room[x][y] // 5) * cnt)
  for x, y, diff in diffuse:
    room[x][y] += diff

  for i in range(2):
    x, y = machine[i]
    y += 1
    tmp = room[x][y]
    room[x][y] = 0
    for v in range(4):
      nx, ny = x, y
      while True:
        if not i:
          nx = nx + dx[v]
          ny = ny + dy[v]
        else:
          nx = nx + dx[-v]
          ny = ny + dy[-v]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
          break
        if room[nx][ny] == -1:
          break
        tmp, room[nx][ny] = room[nx][ny], tmp
        x, y = nx, ny

print(sum([sum(x) for x in room]) + 2)