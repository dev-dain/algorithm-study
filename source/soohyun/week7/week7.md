## 7주차 공통문제
### [백준 16637 괄호 추가하기](https://www.acmicpc.net/problem/16637)
- 문제 유형: 완전탐색
- 시간 복잡도: O(N)
- 공간 복잡도: O(N^2)
- 접근 방법
    - 문제는 간단하지만 어떻게 풀어야 할지 모르겠어서 풀이를 봤는데... 너무 길었다
    - 긴 코드는 뭐라는지 모르겠어서 최대한 간결한 코드를 찾아 이해해보려고 노력했다..^^
<br/><br/>
- 아이디어
    - 괄호가 묶이는 경우를 잘 생각해보면, 괄호 이전의 수식은 이미 다 계산된 상태에서 괄호가 연산된다.
    - 연산된 괄호와 이미 계산된 숫자들이 그 사이의 연산자로 계산되는 과정이 반복된다.
    - 첫번째로, 자신 차례인 연산자에 괄호를 묶을 수 있다. 
    - ex) (3+8)×7-9×2 --> 자신 차례인 연산자는 +이며 자신 차례에 괄호를 묶었다
    - 두번재로, 자신 차례의 다음 연산자에 괄호를 묶어 계산한 후, 자신 차례의 숫자와 연산된 괄호값을 그 사이 연산자로 계산한다.
    - 3+(8x7)-9×2 --> 자신 차례의 다음 연산자는 x이며 다음 연산자에 괄호를 묶었다. 괄호를 계산하면 56이므로 '3+56'이 계산되게 된다.
    - 따라서 두가지 경우로 모든 케이스를 확인할 수가 있다.
    - 참고 - https://imucoding.tistory.com/516
<br/><br/>
- 풀이
    1. 입력받은 수식을 숫자와 연산자 리스트에 나눠 저장한다.
    2. DFS을 통해 괄호를 사용하여 만들 수 있는 최대값을 구한다.
        - 수식 계산이 끄타면 최대값을 구하고 리턴한다.
        - 현재 연산자를 괄호에 넣는 경우와 다음 연산자를 괄호에 넣는 경우를 각각 처리한다.
    3. 결과를 출력한다.
<br/><br/>
- 코드
```python
n = int(input())
exp = input()
num, op = [], [] # 수식의 숫자, 연산자 리스트
ans = -1e9 # 최대값

for e in exp:
    num.append(e) if e.isdigit() else op.append(e)

def dfs(idx, total):
    global ans

    # 수식 계산이 끝나면 최대값을 구하고 리턴
    if idx == len(op):
        ans = max(ans, int(total))
        return

    # 현재 연산자에서 괄호 넣기
    # (3+8)×7-9×2
    first = str(eval(total + op[idx] + num[idx+1]))
    dfs(idx+1, first)

    # 다음 연산자에서 괄호 넣기
    # 3+(8x7)-9×2
    if idx + 1 < len(op):
        next = str(eval(num[idx+1] + op[idx+1] + num[idx+2])) # 괄호 값 계산
        second = str(eval(total + op[idx] + next))
        dfs(idx+2, second)

dfs(0, num[0])
print(ans)
```

### [백준 17406 배열 돌리기 4](https://www.acmicpc.net/problem/17406)
- 문제 유형: 구현, 완전탐색
- 시간 복잡도: O(K! * NM)
- 공간 복잡도: O(NM)
- 접근 방법
    - 먼저 회전 연산의 순서에 따라 배열A의 최소값이 달라지므로 순서는 순열을 통해 구했다.
    - 로봇청소기 문제처럼 회전하면 될 것 같아서 방향을 바꿔가면서 회전하는 방법을 생각했다.
    - 로봇청소기와 다르게 안쪽도 회전을 해줘야되서 추가 조건이 더 필요했다.
<br/><br/>
- 풀이
    1. 모든 회전 연산의 순열을 구한다.
    2. 회전 순서에 따른 회전을 한다. (= rotate 함수) 
        - 이 때, 배열A는 복사해서 넘겨줘야 한다. 회전 연산의 순열에 따른 최소값을 각각 구해줘야 하므로!!
        - 더 이상 회전할게 없을 때까지 회전을 한다. ( = while lx < rx and ly < ry)
        - 방향에 따른 회전을 해주는데, 이동 범위를 벗어나면 방향을 바꾼다.
        - 현재 위치가 시작 위치(= 가장 왼쪽 위의 위치)와 같아지면 다음 안쪽 회전으로 넘어간다.
        - 모든 회전이 끝나면 최소값을 구한다.
    3. 결과를 출력한다.
<br/><br/>
- 코드
```python
# 회전하기
def rotate(pm, arr):
    result = 1e9 # 최소값

    for r, c, s in pm:
        r -= 1; c -= 1 # 인덱스가 0부터 시작
        lx, ly, rx, ry = r-s, c-s, r+s, c+s # 가장 왼쪽 위의 위치, 가장 오른쪽 아래의 위치

        # lx = rx and ly = ry( = 더 이상 회전할게 없다는 의미) 가 될 때까지 회전
        while lx < rx and ly < ry:
            x, y, before = lx, ly, arr[lx][ly] # 현재 위치, 값
            dir = 0 # 이동할 방향

            while True:
                nx = x + dx[dir]
                ny = y + dy[dir]

                if nx < lx or nx > rx or ny < ly or ny > ry: # 이동 범위를 벗어나면 방향을 바꾼다
                    dir += 1
                    continue

                arr[nx][ny], before = before, arr[nx][ny] # 값 이동
                x, y = nx, ny # 위치 이동

                if x == lx and y == ly: # 회전이 끝나면 다음 회전으로 넘어간다
                    lx += 1; ly += 1; rx -= 1; ry -= 1
                    break

    # 최소값 구하기
    for row in arr:
        result = min(result, sum(row))

    return result

# 모든 회전 순서 순열에 따른 회전하기
for pm in permutations(rot, k):
    result = rotate(pm, copy.deepcopy(a))
    ans = min(ans, result)

print(ans)
```

### [백준 1806 부분합](https://www.acmicpc.net/problem/1806)
- 문제 유형: 완전탐색, 백트랙킹
- 시간 복잡도: O(N^3)
- 공간 복잡도: O(6)
- 접근 방법
    - 모든 칸에서 모든 색종이를 확인하여 붙일 수 있는지 확인하면 되는 문제였다.
    - 완전탐색으로 모든 경우를 다 체크해주면 됐었다.
    - 근데 골드 문제 답게 백트래킹을 사용해서 조건에 따른 가지치기를 해주어야 하는게 중요했다.
<br/><br/>
- 풀이
    1. 재귀함수를 통해 해당 칸에 색종이를 붙일 수 있는지 확인한다.
    2. y >= 10 라면 끝까지 탐색한 것이므로 색종이의 최소 개수를 갱신한다.
    3. x >= 10 라면 해당 열은 끝까지 탐색한 것이므로 다음 열을 탐색한다.
    4. 색종이를 붙일 수 없는 경우에는 다음 칸을 탐색한다.
    5. 색종이를 붙일 수 있는 경우에는 모든 색종이를 붙일 수 있는지 확인한다.
        - 해당 색종이 사용 개수가 5인 경우 다음 색종이로 넘어간다. (색종이 최대 사용 개수 = 5)
        - 범위를 벗어나는 크기의 색종이라면 더 이상 볼 필요가 없으므로 탐색을 종료한다.
        - 해당 색종이를 붙일 수 있다면 색종이를 붙인 칸을 0으로 만들고 사용 개수에 +1 한다.
        - 그리고 색종이를 붙이지 않은 다음 칸을 탐색한다.
        - 모든 경우를 탐색해야하기 때문에 초기화를 꼭! 해준다
    6. 모든 탐색이 끝나면 조건에 따른 결과를 출력한다.
<br/><br/>
- 코드
```python
paper = [list(map(int, input().split())) for _ in range(10)]
paper_cnt = [0] * 6 # 종이별 사용 개수
ans = 1e9 # 색종이의 최소 개수

def solve(x, y, cnt):
    global ans

    if y >= 10: # 끝까지 탐색한 것이므로 최소 개수 갱신
        ans = min(ans, cnt)
        return

    if x >= 10: # y열은 탐색이 끝났으므로 다음 열로 넘어간다
        solve(0, y+1, cnt)
        return

    if paper[x][y] == 1: # 색종이를 붙일 수 있는 경우
        for k in range(1, 6): # k = 색종이의 크기
            if paper_cnt[k] == 5: # 해당 색종이 사용 개수가 5인 경우 다음 색종이로 넘어간다
                continue

            if x+k > 10 or y+k > 10: # 범위를 벗어나는 크기의 색종이라면 break
                break

            flag = True # 해당 색종이를 붙일 수 있는지 체크
            for i in range(x, x+k):
                for j in range(y, y+k):
                    if paper[i][j] == 0: # 해당 색종이를 붙일 수 없다먄 flag = False
                        flag = False
                        break
                if not flag: break

            if flag: # 해당 색종이를 붙일 수 있는 경우
                # 색종이를 붙이는 칸을 0으로 만들고 개수에 +1
                for i in range(x, x+k):
                    for j in range(y, y+k):
                        paper[i][j] = 0
                paper_cnt[k] += 1

                solve(x+k, y, cnt+1) # 다음 칸으로 넘어간다

                # 초기화
                for i in range(x, x+k):
                    for j in range(y, y+k):
                        paper[i][j] = 1
                paper_cnt[k] -= 1
    else: # 색종이를 붙일 수 없는 경우
        solve(x+1, y, cnt) # 다음 칸으로 넘어간다

solve(0, 0, 0)
print(-1) if ans == 1e9 else print(ans)
```