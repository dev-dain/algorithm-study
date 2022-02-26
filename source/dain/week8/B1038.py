from collections import deque
N = int(input())
qu = deque(list('0123456789'))
cnt = 9
if N < 10:
  print(qu[N])
  exit(0)

while qu:
  n = qu.popleft()
  for i in range(0, 10):
    if int(n[-1]) <= i:
      break
    qu.append(n+str(i))
    cnt += 1
    if cnt == N:
      print(qu[-1])
      exit(0)

print(-1)