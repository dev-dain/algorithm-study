## 7주 공통 문제 1
* 🥇❓ [백준 16637 괄호 추가하기](https://www.acmicpc.net/problem/16637)

* 접근 방법
	* 진짜 괄호를 붙여가면서 계산하는 방식으로 답을 찾는 코드를 짬
  * 예를 들어 3+8x7-9x2 라면 (11)x7-9x2 이렇게 식이 변경되어 계산할 수 있도록 함
  * 처음에는 eval 함수 써도 되는 줄 알았는데 알고 보니 연산자 우선순위가 동일해서 왼쪽부터 계산되는 거라서 DFS가 맞긴 맞았음
  * 이렇게 코드를 1시간 30분 짜서 제출했는데.. 22%쯤에서 틀렸고 왜 틀렸는지도 모르겠음

* 정답 코드를 향한 길..
  * 새로 찾은 코드는 만약 인덱스가 0일 때(즉 처음일 때)는 +를 더하고(양수니까), 그렇지 않으면 앞의 인덱스인 연산자를 op로 정함
  * 솔직히 내 코드와 그렇게 다르지 않은 것 같은데 내 코드의 뭐가 문제인지? 알 수 없어서 답답한 문제였음
   
---
* 오답 코드
```python
from copy import deepcopy

N = int(input())
expression = list(input())
res = int(-1e9)

def calculate(exp):
  length = len(exp)
  if exp[2] == '(':
    res = eval(exp[0] + exp[1] + exp[3])
    idx = 5
  else:
    res = eval(''.join(exp[:3]))
    idx = 3
  while idx < length:
    op = exp[idx]
    if exp[idx+1] == '(':
      n = exp[idx+2]
      idx += 2
    else:
      n = exp[idx+1]
    res = eval(str(res) + op + n)
    idx += 2
  return res

def dfs(exp, index):
  global res
  if (index*2) >= N:
    return
  for i in range(index, N-1):
    new_exp = deepcopy(exp)
    try:
      val = eval(''.join(new_exp[i*2:i*2+3]))
    except:
      return
    new_exp[i*2:i*2+3] = ['(', str(val), ')']
    res = max(res, calculate(new_exp))  
    dfs(new_exp, index+2)
  return

for i in range(0, N//2):
  exp = deepcopy(expression)
  val = eval(''.join(exp[i*2:i*2+3]))
  exp[i*2:i*2+3] = ['(', str(val), ')']
  res = max(res, calculate(exp))
  dfs(exp, i+2)
if N == 1:
  res = ''.join(expression)
print(res)
```

* 정답 코드
```python
def calculate(x, y, op):
  return eval(x+op+y)

def dfs(index, val):
  global res
  if index >= N:
    res = max(res, val)
    return

  op = '+' if index == 0 else exp[index-1]
  if (index + 2 < N):
    tmp = calculate(exp[index], exp[index+2], exp[index+1])
    dfs(index + 4, calculate(str(val), str(tmp), op))
  dfs(index + 2, calculate(str(val), str(exp[index]), op))

N = int(input())
exp = list(input())
res = -1e9
dfs(0, 0)
print(res)
```
- 시간복잡도 : O(nlogn)
- 공간복잡도 : O(n)
- 문제 유형 : 완전탐색, 백트랙킹
---
---
## 7주 공통 문제 2
* 🥇❓ [백준 17136 내려가기](https://www.acmicpc.net/problem/17136)
* 접근 방법
	* 16637 문제는 풀기라도 했지 이건 손도 못 댈 지경이었으로 정말 어려운 문제였음. 일반적인 기업에서 나올 수 있는 난이도 중 최고 난이도 문제가 아닐까 생각이 듦
  * 이 문제는 그리디로 풀 수 없기 때문에 가능한 종이 모양을 전부 테스트해서 종이를 가장 조금 쓸 수 있도록 찾아야 하는 완전탐색을 써야 함
  * 나도 그 생각은 했는데 한 위치에서 k*k 색종이를 붙였다 뗐다 하는 것을 어떻게 구현해야 할지 몰라서 구현하다가 말고 찾음
  
* 검색 후 정리
  * 10*10만큼 루프를 돌되, 그 안에서 1이 발견되면 색종이 붙이기를 시도 (for k in range(5))
  * 이 때, used 배열에서 5를 넘었다면 그 크기 종이는 다 쓴 것이므로 다음으로 큰 것을 시도함
  * 만약 k*k 크기만큼의 종이가 남았다면 그 크기만큼 1이 있는지 루프를 돌음 (x+k, y+k)
  * 종이로 덮을 수 있다면 덮은 부분은 0으로 처리하고 used[k]에서 1을 더함. 그 다음 "이 상태의 종이로" y+k부터, 즉, 같은 가로줄인데 k만큼 이동한 곳부터 다시 DFS를 시작함
  * 한편 다른 케이스도 검사해야 하기 때문에 DFS를 다 돌고 나오면 used[k]에서 1을 빼 주고 색종이를 덮은 부분에서 다시 색종이를 가져감. (1으로 돌려놓음)
  * 만약 전체 루프를 다 돌았다면 거기서 answer를 더 작은 것으로 업데이트함  
  * 여기서 얻은 교훈은 반드시 deepcopy를 쓰지 않아도 되는 문제였다는 것이다. 나는 반드시 deepcopy를 써야 하는 줄.. 조금만 더 끈기있게 붙었다면 풀 수도 있었을 것 같은데, 아쉽다.
---
* 생각해본 코드
```python
from copy import deepcopy

def check(num, paper, i, j):
  for x in range(i, num):
    if x >= 10:
      return False
    for y in range(j, num):
      if y >= 10 or not paper[x][y]:
        return False
  return True
    
paper = [list(map(int, input().split())) for _ in range(10)]
available = [5, 5, 5, 5, 5]

tmp = deepcopy(paper)
for i in range(10):
  for j in range(10):
    if tmp[i][j]:
      tmp = deepcopy(tmp)
      # visited = [[0 for _ in range(10)] for _ in range(10)]
      if check(5, tmp, i, j):
        for x in range(i, i+5):
          paper[x] = tmp[:x] + [0, 0, 0, 0, 0] + paper[x+5:]
          available[-1] -= 1
      elif check(4, tmp, i, j):
        for 
        # 이 뒤는 생각을 못함
```

* 정답 코드
```python
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y, count):
  global answer, used

  if x >= 10:
    answer = min(answer, count)
    return

  if y >= 10:
    dfs(x+1, 0, count)
    return

  # 색종이 붙이기
  if paper[x][y] == 1:
    for k in range(5):
      if used[k] == 5:  # 다 썼으면 넘어가기
        continue
      if x + k >= 10 or y + k >= 10:
        continue

      flag = True
      # k 크기의 종이 대보기
      for i in range(x, x+k+1):
        for j in range(y, y+k+1):
          if paper[i][j] == 0:
            flag = False
            break
        if not flag:
          break

      if flag:
        for i in range(x, x+k+1):
          for j in range(y, y+k+1):
            paper[i][j] = 0
        used[k] += 1  # 종이 쓴 것
        dfs(x, y+k+1, count+1)

        used[k] -= 1  # 종이 안 쓴 채로 돌려놓기
        for i in range(x, x+k+1):
          for j in range(y, y+k+1):
            paper[i][j] = 1
    # 현재 좌표가 0이라면 넘어가기
  else:
    dfs(x, y+1, count)

paper = [list(map(int, input().split())) for _ in range(10)]
used = [0] * 5
answer = 26 # 아무리 커도 25장을 안 넘기 때문에
dfs(0, 0, 0)
print(answer if answer != 26 else -1)
```
- 시간복잡도 : O(1) (10*10이라서 아무리 많이 연산해도 어느 정도로 수렴되는데 O(1)이 아닌지 하는 생각이 듭니다.)
- 공간복잡도 : O(1)
- 문제 유형 : 완전탐색, 백트랙킹

## 7주 공통 문제 3
* 🥇 [백준 17406 배열 돌리기 4](https://www.acmicpc.net/problem/17406)
  
* 접근 방법
	* "미세먼지 안녕!" 문제와 비슷하게 배열을 사각형으로 돌리는 문제인데, 차이점은 테두리가 아니라 그 안쪽 사각형까지 돌려야 하는 문제였음
  * 회전 연산이 2개 이상일 때는 연산 수행 순서에 따라 최종 배열이 다르므로 모든 순열을 다 시험해봐야 하는 완전탐색 문제. permutations 사용하고, 매번 deepcopy로 배열을 복사 떠놔야 다음 순열에서 입력으로 들어온 순수한 배열을 시험할 수 있음
  * 회전 연산 변수 s개만큼의 테두리를 돌려주는 것을 알면 풀기 쉬워짐
  * 이 뒤로는 미세먼지 문제랑 비슷해서 딱히 설명할 건 없음. 그냥 tmp랑 temp[nx][ny]를 바꿔서 계속 tmp를 새 것으로 홀드하고 있으면 끝임
  
---
* 정답 코드
```python
from itertools import permutations
from copy import deepcopy

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
RCS = [list(map(int, input().split())) for _ in range(K)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
res = 1e9

for perm in permutations(RCS,K):
  temp = deepcopy(A)
  for r, c, s in perm:
    for i in range(0, s):
      top = [r-s+i-1, c-s+i-1]
      bottom = [r+s-i-1, c+s-i-1]
      nx, ny = top
      tmp = temp[nx][ny]

      for i in range(4):
        while True:
          nx = nx + dx[i]
          ny = ny + dy[i]
          if not (nx >= top[0] and nx <= bottom[0] and ny >= top[1] and ny <= bottom[1]):
            nx = nx - dx[i]
            ny = ny - dy[i]
            break
          tmp, temp[nx][ny] = temp[nx][ny], tmp

  for row in temp:
    res = min(res, sum(row))
print(res)
```
- 시간복잡도 : O(K!) (순열 테스트)
- 공간복잡도 : O(N*M)
- 문제 유형 : 완전탐색, 시뮬레이션
- Python3 제출, 31044KB / 3824ms