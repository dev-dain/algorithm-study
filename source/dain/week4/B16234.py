import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]
day = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, visited, country, num, cnt):
  visited[x][y] = 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
      continue
    if [nx, ny] in country:
      continue
    if L <= abs(land[x][y] - land[nx][ny]) <= R:
      country.append([nx, ny])
      cnt, country = dfs(nx, ny, visited, country, num, cnt + 1)
  return cnt, country

while True:
  visited = [[0 for _ in range(N)] for _ in range(N)]
  num = 1
  cnt = 0
  cnt_list = []
  country_list = []
  for i in range(N):
    for j in range(N):
      if not visited[i][j]:
        visited[i][j] = 1
        cnt, country = dfs(i, j, visited, [[i, j]], num, 1)
        if cnt == 1:
          continue
        cnt_list.append(cnt)
        country_list.append(country)
        num += 1
  if num == 1:
    break
  for i in range(len(cnt_list)):
    people = 0
    for x, y in country_list[i]:
      people += land[x][y]
    people = people // cnt_list[i]
    for x, y in country_list[i]:
      land[x][y] = people
  day += 1
print(day)