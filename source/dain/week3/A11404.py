import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
cost = [[sys.maxsize for _ in range(n)] for _ in range(n)]

for _ in range(m):
  a, b, c = map(int, input().split())
  cost[a-1][b-1] = min(cost[a-1][b-1], c)
for x in range(n):
  cost[x][x] = 0

for i in range(n):
  for j in range(n):
    for k in range(n):
      cost[j][k] = min(cost[j][k], cost[j][i] + cost[i][k])
for co in cost:
  for x in co:
    print(x, end=' ') if x is not sys.maxsize else print(0, end=' ')
  print()