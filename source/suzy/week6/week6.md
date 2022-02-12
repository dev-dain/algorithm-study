## 6주차 공통문제
### [백준 2230](https://www.acmicpc.net/problem/2230)
- 문제 유형: 정렬, 투포인터
- 시간 복잡도: O(NlogN + N)
- 공간 복잡도: O(1)
- 접근 방법
    - 두 수를 골랐을때 그 차이가 M일 경우가 가장 작은 경우
    - 차이를 비교하기 위해 정렬
<br/><br/>
- 풀이
    - 전체를 비교하기 위해 index left 와 right 를 각 0과 1로 두고 갱신
    - 차이가 M 이상일 경우 중 가장 작은 값은 M 이므로 차이가 M과 같다면 M 을 출력하고 종료
<br/><br/>
- 코드
import sys
input = sys.stdin.readline
# 입력
n, m = map(int, input().split())
a = [0] * n
for i in range(n):
    a[i] = int(input().strip())

a = sorted(a)
ans = sys.maxsize
# 투포인터
left, right = 0, 1
while left < n and right < n:
    tmp = a[right] - a[left]
    if tmp == m:
        print(m)
        exit(0)
    if tmp < m:
        right += 1
        continue
    left += 1
    ans = min(tmp, ans)
print(ans)
```

### [백준 2096](https://www.acmicpc.net/problem/2096)
- 문제 유형: DP, 슬라이딩 윈도우
- 시간 복잡도: O(N)
- 공간 복잡도: O(N)
- 접근 방법
    - 메모리 초과로 배열 선언을 최소화 .. 해야했기 때문에 기존 dp 방식과 달라 다른 풀이를 참고했습니다
    - 왼쪽, 가운데, 오른쪽 큰 곳으로 작은 곳으로 조건에 맞춰 배열을 갱신하도록 구현하면 되는 문제였습니다
<br/><br/>
- 풀이
    - 최대 점수와 최소 점수를 1차원 배열!로 입력 받고 최대점수와 최소점수를 구하여 dp에 저장합니다
    - 최대 점수와 최소 점수를 출력합니다
<br/><br/>
- 코드
```python
import sys

input = sys.stdin.readline

n = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

max_tmp = [0] * 3
min_tmp = [0] * 3

for i in range(n):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            max_tmp[j] = a + max(max_dp[j], max_dp[j + 1])
            min_tmp[j] = a + min(min_dp[j], min_dp[j + 1])
        elif j == 1:
            max_tmp[j] = b + max(max_dp[j - 1], max_dp[j], max_dp[j + 1])
            min_tmp[j] = b + min(min_dp[j - 1], min_dp[j], min_dp[j + 1])
        else:
            max_tmp[j] = c + max(max_dp[j], max_dp[j - 1])
            min_tmp[j] = c + min(min_dp[j], min_dp[j - 1])

    for j in range(3):
        max_dp[j] = max_tmp[j]
        min_dp[j] = min_tmp[j]

print(max(max_dp), min(min_dp))
```

### [백준 1806 부분합](https://www.acmicpc.net/problem/1806)
- 문제 유형: 투포인터
- 시간 복잡도: O(N)
- 공간 복잡도: O(N)
- 접근 방법
    - 예전에 조합인가 .. 하고 사용했던 생각이 나서 모든 합의 조합을 다 구해서 비교하는 요상한 방법에 빠져서 망할뻔 했다 ㅎㅎ .. ^^ 헤헤 ..
    - 그런 문제가 아니고 정상적으로 투포인터로 구현하는 문제였다
<br/><br/>
- 풀이
    - left 부터 right 까지 부분합을 구하고 길이를 ans 저장한다
    - 합이 s 이상이라면 left 포인터를 이동하여 최소길이를 갱신합니다
<br/><br/>
- 코드
```python
n, s = map(int, input().split())

arr = list(map(int, input().split()))

end = 0
# 초기의 합을 arr[0]
result = arr[0]
ans = float('inf')

# 투포인터
for start in range(n):
    while result < s and end < n:
        end += 1
        if end == n:
            break
        result += arr[end]
    
    if result >= s:
        ans = min(ans, end-start+1)
    result -= arr[start]

if ans == float('inf'):
    print(0)
else:
    print(ans)
```
