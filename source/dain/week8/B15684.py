def check():
  for i in range(N):
    line = i
    for j in range(H):
      if visited[j][line]:
        line += 1
      elif line > 0 and visited[j][line-1]:
        line -= 1
    if i != line:
      return False
  return True

def dfs(x, y, cnt):
  global res
  if check():
    res = min(res, cnt)
    return
  elif cnt == 3 or res <= cnt:
    return
  for i in range(x, H):
    k = y if i == x else 0
    for j in range(k, N-1):
      if not visited[i][j] and not visited[i][j+1]:
        if j > 0 and visited[i][j-1]:
          continue
        visited[i][j] = 1 # 가로선 놔보기
        dfs(x, y+2, cnt+1)
        visited[i][j] = 0 # 가로선 다시 회수

N, M, H = map(int, input().split())
visited = [[0 for _ in range(N)] for _ in range(H)]
if not M:
  print(0)
  exit(0)
for _ in range(M):
  x, y = map(int, input().split())
  visited[x-1][y-1] = 1
res = 4
dfs(0, 0, 0)
print(res if res < 4 else -1)