## 8주차 공통문제
### [백준 1038 감소하는 수](https://www.acmicpc.net/problem/1038)
- 문제 유형: 완전탐색, 백트랙킹
- 시간 복잡도: O(N)
- 공간 복잡도: O(1)
- 접근 방법
    - 만약 현재 숫자가 감소하는 숫자라면 다음 숫자로 넘어가고,
    - 감소하지 않는 숫자라면 감소하는 숫자를 찾을 때까지 숫자를 증가시키면 된다고 생각했다.
    - 근데 무한루프에 빠져버려서... 모르겠어서 풀이를 참고했다.
    - 재귀함수 쓰는 문제는 넘 어려운 것 같다..
<br/><br/>
- 풀이
    1. 수의 범위에 따른 처리를 해준다.
        - n = 0 이면 0을 출력, n > 1022면 -1을 출력, 나머지 경우는 재귀함수의 결과를 출력
    2. 반복문을 통해 감소하는 수인지 체크한다.
    3. 숫자의 길이가 1이면 무조건 감소하는 수이므로 아무것도 하지 않는다.
    4. 숫자의 길이가 2이상 이라면 감소하는 수인지 체크한다.
        - 감소하는 수가 아닌 경우 감소하는 수로 만들어준다. (ex. 655 -> 660)
    5. 감소하는 수라면 다음 숫자로 넘어가는데, 이 때 n번째 감소하는 수라면 리턴한다.
<br/><br/>
- 코드
```python
n = int(input())

def solve(n):
    cnt = 0 # 몇번째 수인지
    num = 1 # 현재 수

    while True:
        str_num = str(num)
        flag = True # 감소하는 수인지 체크

        if len(str_num) == 1:  # 길이가 1이면 무조건 감수하는 수
            pass
        else:
            for i in range(1, len(str_num)):
                if int(str_num[i-1]) > int(str_num[i]):
                    continue
                else: # 감소하는 수가 아닌 경우 감소하는 수로 만들어준다
                    start = str_num[:i - 1]
                    mid = str(int(str_num[i - 1]) + 1)
                    end = '0' + str_num[i + 1:]
                    num = int(start + mid + end)
                    flag = False
                    break
        if flag:
            cnt += 1
            if cnt == n:  # n번째 감소하는 수라면 리턴
                return num
            num += 1

if n > 1022: # n번째 감소하는 수가 없는 경우
    print(-1)
elif n == 0: # 0번째 숫자인 경우
    print(0)
else:
    print(solve(n))
```

### [백준 15684 사다리 조작](https://www.acmicpc.net/problem/15684)
- 문제 유형: 구현, 완전탐색, 백트랙킹
- 시간 복잡도: O(NH)
- 공간 복잡도: O(NH)
- 접근 방법
    - 다 해보면 되는 완전탐색이었고, 놓을 수 있는 가로선 개수가 있어서 재귀함수를 탈출할 조건은 쉽게 알 수 있었다.
    - 열심히 풀어보았으나 수많은 틀렸습니다의 반복으로 풀이를 볼 수 밖에 없었다...
    - 풀이도 이해가 잘 안가서 이해하는데 오래걸렸다. 나중에 다시 꼭 풀어봐야될 것 같다
<br/><br/>
- 풀이
    1. m개의 가로선은 연결 처리해준다.
    2. (0, 0)부터 가로선을 놓을 수 있는지 확인한다.
    3. 현재 가로선이 없으면서 왼쪽과 오른쪽에 가로선이 없는 경우에 가로선을 놓는다.
    4. 모든 i번 세로선의 결과가 i번이 나온다면 더 이상 가로선을 놓을 필요가 없으므로 답을 구하고 리턴한다.
    5. 조건에 따른 결과를 출력한다.
<br/><br/>
- 코드
```python
import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
board = [[0] * n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1 # 가로선 연결

# i번 세로선의 결과가 i번이 나오는지 확인
def check():
    for start in range(n): # 세로선(열) 체크
        j = start # 이동하는 가로선
        for i in range(h): # 가로선(행) 체크
            if board[i][j]: # 가로선이 오른쪽에 있다면 오른쪽으로 이동
                j += 1
            elif j > 0 and board[i][j-1]: # 가로선이 왼쪽에 있다면 왼쪽으로 이동
                j -= 1
        if j != start: # 도착한 세로선이 출발한 세로선과 같지 않으면 return False
            return False
    return True # i번 세로선의 결과가 i번이 나오면 return True

# 가로선 놓기
def solve(cnt, x, y):
    global ans

    # 모든 i번 세로선의 결과가 i번이 나온다면 답을 구하고 리턴
    if check():
        ans = min(ans, cnt)
        return
    # 더 이상 가로선을 놓을 수 없거나 (최대 가로선 수는 3) 가로선이 답보다 많다면 더 이상 볼 필요가 없으므로 리턴
    elif cnt == 3 or ans <= cnt:
        return

    for i in range(x, h):
        k = y if i == x else 0 # 행이 변경되면 0부터, 변경되지 않으면 현재 가로선을 탐색
        for j in range(k, n-1):
            # 현재 가로선이 없으며 왼쪽과 오른쪽에 가로선이 없는 경우 가로선을 놓는다
            if not board[i][j] and not board[i][j+1] and not board[i][j-1]:
                board[i][j] = 1
                solve(cnt+1, i, j+2)
                board[i][j] = 0

ans = 4
solve(0, 0, 0)
print(ans) if ans < 4 else print(-1)
```

### [백준 1062 가르침](https://www.acmicpc.net/problem/1062)
- 문제 유형: 완전탐색, 백트랙킹, 비트마스크
- 시간 복잡도: O(N * (K-5))
- 공간 복잡도: O(N)
- 접근 방법
    - 단어에서 공통적으로 들어가는 알파벳이 'a, c, i, n, t' 이다.
    - k < 5인 경우 읽을 수 있는 단어가 없다.
    - k >= 5인 경우 공통 알파벳 빼고 나머지 알파벳의 조합을 구해서 읽을 수 있는 단어 개수를 셌다.
    - 하지만, 역시 시간초과..^^ 역시 골드 쉽지 않네 
    - 'if w not in alphabet' 으로 글자를 읽을 수 있는지 확인한 부분 때문에 시간초과가 난 것 같다.
    - 다른 풀이를 참고해보니 글자를 읽을 수 있는지 확인할 수 있는 리스트를 통해 해결할 수 있었다.
<br/><br/>
- 풀이
    1. 알파벳을 읽을 수 있는지 확인할 수 있는 리스트 learn을 생성한다.
    2. 공통 알파벳은 읽을 수 있으므로 읽기 처리한다.
    3. k < 5인 경우 읽을 수 있는 단어가 없으므로 0을 출력한다.
    4. k >= 5인 경우 읽을 수 있는 단어 최대 개수를 구한다.
    5. 읽을 수 있는 글자를 k개 만드는 모든 경우를 탐색한다.
    6. 읽을 수 있는 글자가 k개 만들어졌다면 읽을 수 있는 단어 개수를 센 후, 최대 개수를 갱신한다.
    7. 모든 경우의 탐색이 끝나면 최대 개수를 출력한다.
<br/><br/>
- 코드
```python
n, k = map(int, input().split())
words = [input() for _ in range(n)]
learn = [0] * 26 # 읽을 수 있는 알파벳
ans = 0 # 읽을 수 있는 단어 최대 개수

# 공통 알파벳은 읽기 처리
for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1

def dfs(cnt, idx):
    global ans

    # 읽을 수 있는 글자가 k개인 경우 읽을 수 있는 단어 개수 세기
    if cnt == k-5:
        read = 0
        for word in words:
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    break
            else:
                read += 1
        ans = max(ans, read)

    # 글자 배우기
    for i in range(idx+1, 26):
        if not learn[i]:
            learn[i] = 1
            dfs(cnt+1, i)
            learn[i] = 0

if k < 5:
    print(0)
else:
    dfs(0, 0)
    print(ans)
```