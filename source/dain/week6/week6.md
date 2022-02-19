## 6주 공통 문제 1
* 🥇 [백준 2230 수 고르기](https://www.acmicpc.net/problem/2230)

* 접근 방법
	* 차이가 M 이상이면서 제일 작은 경우를 구하는 문제라서 투포인터 방법으로 접근 가능  
  * 정렬해서 전체 배열을 보면 쉽게 풀리겠다고 생각했는데 계속 틀렸음  
  * 원인은 오른쪽 포인터를 N-1으로 잡은 것. 이렇게 하면 오히려 보지 못하는 구간이 생김 (L이 뒤로 이동하면서, L 이전의 구간을 못 보게 됨)  
  * 그래서 L을 0으로, R을 1로 고쳐서 다시 풀었더니 맞음  
   
---
* 오답 코드
```python
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
l = 0
r = N-1 # 이렇게 하면 전체를 볼 수 있을 거라고 생각했는데 착각이었음
diff = abs(arr[l] - arr[r]) # 게다가 이 차이도 절대값이 아니었음
while l < r:
  new = abs(arr[l] - arr[r])
  if new == M:
    diff = new
    break
  elif new > M:
    diff = min(diff, new)
    r -= 1
  else:
    l += 1
print(diff)
```

* 정답 코드
```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
l = 0
r = 1 # N-1이 아니라 1로 해야 다 둘러볼 수 있음
diff = sys.maxsize  # 일단 시스템상 최대값으로 하고 줄이는 것으로 함
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
```
- 시간복잡도 : O(n^2)
- 공간복잡도 : O(n)
- 문제 유형 : 투포인터
- Python3 제출, 35108KB / 204ms
---
---
## 6주 공통 문제 2
* 🥇❓ [백준 2096 내려가기](https://www.acmicpc.net/problem/2096)
* 접근 방법
	* 슬라이딩 윈도우보다 DP에 가까운 문제. *죄송합니다*  
  * 칸마다 다음 줄에 이동할 수 있는 구간이 달라서 어떻게 풀어야할지 접근 방법을 생각하는 데 오랜 시간이 걸렸고, 게다가 틀림...  
  * 처음 생각은 최대값과 최소값을 담는 변수를 만들고, 최대값/최소값을 담았던 인덱스를 매번 갱신해서 다음에 이용하는 것이었음
  * 그런데 그리디 문제가 아니기 때문에 이렇게 하면 조금 큰 값을 선택하고 다음에 작은 값을 선택해 결과를 작게 만드는 게 안됐음. 게다가 시간 초과를 유발할 수 있는 코드도 있었음  
  
* 검색 후 정리
  * small_dp, big_dp라는 배열을 새로 하나 만든다. 사이즈는 3으로 만들어서 0, 1, 2번 인덱스에서 가능한 최대/최소값으로 갱신함  
  * dp 원래 배열로 만드는 거 맞는데 왜 이 생각을 못 했는지 모르겠음  
---
* 생각해본 코드
```python
from collections import deque

arr = deque(list(map(int, input().split())))
small, big = min(arr), max(arr)
small_i = arr.index(min(arr))
big_i = arr.index(max(arr))
for _ in range(1, N):
  if len(arr) >= 2:
    arr.popleft()
  a, b, c = map(int, input().split())
  # 이 뒤는 생각을 못 함
```

* 정답 코드
```python
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
```
- 시간복잡도 : O(N)
- 공간복잡도 : O(N)
- 문제 유형 : DP
- Python3 제출, 30864KB / 4644ms

## 6주 공통 문제 3
* 🥇 [백준 1806 부분합](https://www.acmicpc.net/problem/1806)
  
* 접근 방법
	* 연속된 수들의 부분합 중 합이 S 이상이면서 가장 짧은 길이를 구하는 문제이기 때문에, 가장 앞에 포인터를 선언하고 for문 안에서 sum 함수를 써가면서 비교하면 되겠다고 생각  
  * 그래서 처음 코드를 짰는데 예제는 다 맞았으나 시간초과를 맞음
  * for문을 n 크기만큼 돌되, 이 안에서 만약 left:i까지의 합이 s를 넘는 동안 left 포인터를 1 증가시키는 방식으로 최소 길이를 구하려고 함  
  * 원인은 계속 sum 함수를 돌려서 최악의 경우 O(n^2) 연산이 되기 때문임  
  * 저번 주에 푼 문제에서 filter 함수를 매번 돌리지 않고 한 번에 O(n)으로 계산한 후 그 결과를 갖다쓰는 연습을 했기 때문에 이번에도 sum들을 먼저 구하고 풀음  
  * 근데 사실 결과적으로는 포인터를 1개 사용해서 풀음
   
* 정리된 풀이
	* sum_list라는 n 크기 배열을 만들어서 이번 인덱스까지의 합을 누적하는 값을 담도록 함  
  * 그리고 이 sum_list를 사용해 어떤 인덱스에서의 합의 값이 s보다 큰지 비교함  
  
---
* 시간 초과 코드
```python
n, s = map(int, input().split())
num = list(map(int, input().split()))
dp = 1e9
left = 0
for i in range(n+1):
  # 여기서 sum 함수를 최대 O(n^2)번
  while sum(num[left:i]) >= s:
    if sum(num[left+1:i]) < s:
      break
    left += 1
  if sum(num[left:i]) >= s:
    dp = min(dp, i-left)
print(dp)
```

* 정답 코드
```python
import sys
n, s = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))
left = 0
dp = 1e9
# 매번 합을 구해주는 것보다 합을 미리 구해놓는 게 현명한 방법이다. 
# O(n)으로 합 구하기
sum_list = [0] * (n+1)
for i in range(1, n+1):
  sum_list[i] = sum_list[i-1] + num[i-1]

for i in range(n+1):
  while (sum_list[i] - sum_list[left]) >= s:
    if (sum_list[i] - sum_list[left+1]) < s:
      break
    left += 1
  if (sum_list[i] - sum_list[left]) >= s:
    dp = min(dp, i-left)
    if dp == 1: break
print(dp) if dp != 1e9 else print(0)
```
- 시간복잡도 : O(n^2)
- 공간복잡도 : O(n)
- 문제 유형 : 투포인터, 그리디
- Pypy3 제출, 137764KB / 148ms