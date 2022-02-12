## 5주차 공통문제
### [백준 2230 수 고르기](https://www.acmicpc.net/problem/2230)
- 문제 유형: 정렬, 투포인터
- 시간 복잡도: O(NlogN + N)
- 공간 복잡도: O(1)
- 접근 방법
    - 두 수의 가장 작은 차이를 찾아야 하므로 투포인터를 사용하면 되는 것은 쉽게 파악했다.
    - 처음엔 l = 0, r = n-1로 두고 탐색을 했는데 틀렸다고 나왔다. 이 때, 뭔가 이상하다는 것을 깨달았다. 생각해보니 이건 이분탐색인 것 같다.
    - l = 0, r = 1로 고치고 왼쪽부터 탐색하도록 바꾸었더니 해결되었다.
<br/><br/>
- 풀이
    1. 입력받은 수(a)를 오름차순 정렬한다.
    2. 투 포인터를 l = 0, r = 1로 초기화한다.
    3. 가장 작은 수의 차이를 찾는다.
        - diff가 m보다 작다면 차이를 더 크게 만들어줘야 하므로 r += 1
        - diff가 m보다 크거나 같다면 차이를 더 작게 만들어줘야 하므로 l += 1
        - 이 때, 수의 차이가 m과 같다면 더 이상 볼 필요가 없으므로 break
    4. 결과를 출력한다.
<br/><br/>
- 코드
```python
n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()

l, r = 0, 1
ans = a[n-1] - a[0]

while l < n and r < n:
    diff = a[r] - a[l] # 수의 차이

    if diff < m:
        r += 1
    else:
        ans = min(ans, diff)
        if diff == m: break
        l += 1

print(ans)
```

### [백준 2096 내려가기](https://www.acmicpc.net/problem/2096)
- 문제 유형: DP, 슬라이딩 윈도우
- 시간 복잡도: O(N * 6)
- 공간 복잡도: O(3 * 5)
- 접근 방법
    - 문제는 어렵지 않았으나 메모리 초과를 해결하는 것이 어려웠던 문제였다.
    - 평소 DP 풀던대로 2차원 리스트를 만들어서 했더니 메모리 초과
    - 이 때, 2차원 리스트를 사용하면 안된다는 것을 깨닫고 1차원 리스트를 사용했지만... 메모리 초과
    - 더 이상 줄일게 없어서 다른 사람 풀이를 보니 입력받는 부분도 메모리를 줄여야했다.
    - 입력을 다 받은 다음 DP를 구현했었는데 입력받는 부분과 DP를 합쳐야 메모리 초과를 해결할 수 있었다.
<br/><br/>
- 풀이
    1. 최대점수와 최소점수를 저장할 1차원 리스트를 생성한다.
    2. n번째 행의 숫자를 입력받는다.
    3. n번째 행의 최대 점수와 최소 점수를 구한 후, dp에 저장한다.
    4. 결과를 출력한다.
<br/><br/>
- 코드
```python
n = int(input())
max_dp = [0] * 3
min_dp = [0] * 3
max_tmp = [0] * 3
min_tmp = [0] * 3

for _ in range(n):
    nums = list(map(int, input().split()))
    
    for j in range(3):
        if j == 0: # 가장 왼쪽일 때
            max_tmp[j] = nums[j] + max(max_dp[j], max_dp[j+1])
            min_tmp[j] = nums[j] + min(min_dp[j], min_dp[j+1])
        elif j == 1: # 가운데일 때
            max_tmp[j] = nums[j] + max(max_dp[j-1], max_dp[j], max_dp[j+1])
            min_tmp[j] = nums[j] + min(min_dp[j-1], min_dp[j], min_dp[j+1])
        else: # 가장 오른쪽일 때
            max_tmp[j] = nums[j] + max(max_dp[j-1], max_dp[j])
            min_tmp[j] = nums[j] + min(min_dp[j-1], min_dp[j])
    
    # 구한 점수를 저장
    for i in range(3):
        max_dp[i] = max_tmp[i]
        min_dp[i] = min_tmp[i]

print(max(max_dp), min(min_dp))
```

### [백준 1806 부분합](https://www.acmicpc.net/problem/1806)
- 문제 유형: 투포인터
- 시간 복잡도: O(N)
- 공간 복잡도: O(N)
- 접근 방법
    - 생각보다 어렵지 않은 투포인터 문제여서 자신있게 제출했지만 시간초과가 났다..^^
    - 이유는 sum()을 사용한 것 때문이었다.
    - sum()을 사용하지 않고 문제를 해결할 방법이 생각나지 않아 다른 사람 풀이를 참고했다.
    - 부분합 리스트를 사용하면 해결할 수 있었고, 이 방법도 알아둬야갰다고 생각했다.
<br/><br/>
- 풀이
    1. 투 포인터 변수와 부분합 리스트를 생성한다.
    2. 부분합 리스트를 구한다.
    3. 투 포인터가 범위를 벗어나지 않을 때까지 최소길이를 구한다.
    4. 먼저 l부터 r까지의 합인 result를 구한다.
    5. result가 s이상이면 최소갱신하고 l을 이동시킨다.
    6. result가 s미만이면 r을 이동시킨다.
    7. 문제 조건에 따른 결과를 출력한다.
<br/><br/>
- 코드
```python
n, s = map(int, input().split())
nums = list(map(int, input().split()))
l, r = 0, 1 # 투 포인터
ans = 1e9 # 최소 길이
sum_n = [0] * (n+1) # 부분합 리스트

for i in range(1, n+1):
    sum_n[i] = sum_n[i-1] + nums[i-1]

while l < n+1 and r < n+1:
    result = sum_n[r] - sum_n[l] # l부터 r까지의 합

    if result >= s: # 합이 s이상이면 최소길이를 갱신 왼쪽 포인터 이동
        ans = min(ans, r-l)
        l += 1
    else: # 합이 s미만이면 오른쪽 포인터 이동
        r += 1

print(0) if ans == 1e9 else print(ans)
```