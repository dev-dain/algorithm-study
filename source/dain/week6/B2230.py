import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
l = 0
r = 1 # N-1이 아니라 1로 해야 다 둘러볼 수 있음
# 아 절댓값이 아니네!
# 문제 한 번 지독하네 ㅠㅠㅋㅋㅋ
diff = sys.maxsize
while l < N and r < N:
  new = arr[r] - arr[l]
  if new == M:
    diff = M
    break
  elif new < M:
    r += 1
  else:
    l += 1
    diff = min(diff, new)
print(diff)
