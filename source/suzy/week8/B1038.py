from collections import deque
N = int(input())
q = deque(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
total = 9
if N <= 9 : 
  print(q[N])
  exit(0)
  
while q:
  c = q.popleft()
  for i in range(0, 10):
    if int(c[-1]) <= i : # 감소하는 수가 아닌 경우
        break
    q.append(c+str(i))
    total += 1
    if total == N: 
      print(q[-1])
      exit(0)

print(-1)