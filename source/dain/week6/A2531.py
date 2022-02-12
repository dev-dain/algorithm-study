# 자력으로 못 풀었어요.. 어렵네요.. ^^
# 슬라이딩 윈도우라는 걸 알면서도,,,
import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]
l = r = 0
res = 0

while l < N:
  # 슬라이딩 윈도우 기법 사용. r은 N보다 커질 수 있음
  r = l + k
  sushi = set() # 중복을 막기 위해..
  add = True  # 쿠폰 초밥을 더할지 말지 확인
  for i in range(l, r):
    i %= N  # r이 N보다 커질 수도 있으므로 인덱스를 나눠주기
    sushi.add(belt[i])
    if belt[i] == c:
      add = False # 쿠폰 초밥이면 이미 더했기 때문에 플래그 내리기
  cnt = len(sushi)
  if add:
    cnt += 1
  res = max(res, cnt) # 가장 많이 먹을 수 있도록 세기
  l += 1
print(res)