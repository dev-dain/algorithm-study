from collections import deque

N = int(input())
big_dp = [0, 0, 0]
small_dp = [0, 0, 0]
arr = list(map(int, input().split()))
big_dp = [x for x in arr]
small_dp = [x for x in arr]
for i in range(1, N):
  arr = list(map(int, input().split()))
  b_tmp = [x for x in big_dp]
  s_tmp = [x for x in small_dp]

  big_dp[0] = max(b_tmp[0], b_tmp[1]) + arr[0]
  small_dp[0] = min(s_tmp[0], s_tmp[1]) + arr[0]

  big_dp[1] = max(b_tmp) + arr[1]
  small_dp[1] = min(s_tmp) + arr[1]

  big_dp[2] = max(b_tmp[1], b_tmp[2]) + arr[2]
  small_dp[2] = min(s_tmp[1], s_tmp[2]) + arr[2]
print(max(big_dp), min(small_dp))
# arr = deque(list(map(int, input().split())))
# small, big = min(arr), max(arr)
# small_i = arr.index(min(arr))
# big_i = arr.index(max(arr))
# for _ in range(1, N):
#   if len(arr) >= 2:
#     arr.popleft()
#   a, b, c = map(int, input().split())
  