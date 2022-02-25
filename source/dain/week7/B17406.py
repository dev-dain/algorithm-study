from itertools import permutations
from copy import deepcopy

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
RCS = [list(map(int, input().split())) for _ in range(K)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
res = 1e9

for perm in permutations(RCS,K):
  temp = deepcopy(A)
  for r, c, s in perm:
    for i in range(0, s):
      top = [r-s+i-1, c-s+i-1]
      bottom = [r+s-i-1, c+s-i-1]
      nx, ny = top
      tmp = temp[nx][ny]

      for i in range(4):
        while True:
          nx = nx + dx[i]
          ny = ny + dy[i]
          if not (nx >= top[0] and nx <= bottom[0] and ny >= top[1] and ny <= bottom[1]):
            nx = nx - dx[i]
            ny = ny - dy[i]
            break
          tmp, temp[nx][ny] = temp[nx][ny], tmp

  for row in temp:
    res = min(res, sum(row))
print(res)