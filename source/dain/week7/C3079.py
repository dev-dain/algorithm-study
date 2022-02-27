# https://viyoung.tistory.com/77
N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]
times.sort()
# 가장 짧은 시간과 가장 길게 걸릴 수 있는 시간 l, r로 잡기
l, r = 0, M*times[-1] + 1
while l < r:
  m = (l + r) // 2
  cnt = 0
  for i in range(N):
    cnt += m // times[i]
  if cnt < M:
    l = m + 1
  else:
    r = m
print(r)