import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y, count):
  global answer, used

  if x >= 10:
    answer = min(answer, count)
    return

  if y >= 10:
    dfs(x+1, 0, count)
    return

  # 색종이 붙이기
  if paper[x][y] == 1:
    for k in range(5):
      if used[k] == 5:  # 다 썼으면 넘어가기
        continue
      if x + k >= 10 or y + k >= 10:
        continue

      flag = True
      # k 크기의 종이 대보기
      for i in range(x, x+k+1):
        for j in range(y, y+k+1):
          if paper[i][j] == 0:
            flag = False
            break
        if not flag:
          break

      if flag:
        for i in range(x, x+k+1):
          for j in range(y, y+k+1):
            paper[i][j] = 0
        used[k] += 1  # 종이 쓴 것
        dfs(x, y+k+1, count+1)

        used[k] -= 1  # 종이 안 쓴 채로 돌려놓기
        for i in range(x, x+k+1):
          for j in range(y, y+k+1):
            paper[i][j] = 1
    # 현재 좌표가 0이라면 넘어가기
  else:
    dfs(x, y+1, count)

paper = [list(map(int, input().split())) for _ in range(10)]
used = [0] * 5
answer = 26 # 아무리 커도 25장을 안 넘기 때문에
dfs(0, 0, 0)
print(answer if answer != 26 else -1)

# 어떻게 체크해야 할지 몰라서 더이상 진행을 못시킴
'''
from copy import deepcopy

def check(num, paper, i, j):
  for x in range(i, num):
    if x >= 10:
      return False
    for y in range(j, num):
      if y >= 10 or not paper[x][y]:
        return False
  return True
    
paper = [list(map(int, input().split())) for _ in range(10)]
available = [5, 5, 5, 5, 5]

tmp = deepcopy(paper)
for i in range(10):
  for j in range(10):
    if tmp[i][j]:
      tmp = deepcopy(tmp)
      # visited = [[0 for _ in range(10)] for _ in range(10)]
      if check(5, tmp, i, j):
        for x in range(i, i+5):
          paper[x] = tmp[:x] + [0, 0, 0, 0, 0] + paper[x+5:]
          available[-1] -= 1
      elif check(4, tmp, i, j):
        for 
'''