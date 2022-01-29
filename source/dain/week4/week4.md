## 4주 공통 문제 1
* 🥇❓ [백준 14500 테트로미노](https://www.acmicpc.net/problem/14500)

* 접근 방법
	* 직관적으로 생각해 보면 가능한 경우의 수를 모두 시도해서 구하면 될 것 같았음
  * 결국 완전탐색 문제의 대표격 되는 것이라고 생각해서 진짜 하나하나 다 구하기 시작(...)
  * 그래서 나온 경우의 수는 총 19가지. 
  * 이것을 종이 위에 올려보면서 테스트하기로 함
  * 일단 냅다 tetromino 경우의 수를 리스트에 담아준다. x, y 좌표값을 담아 만듦
  * 뭔가 더 좋은 방법이 있을 것 같아서 검색도 해봤는데 다른 풀이는 쉽게 이해되지는 않아서 이 방법을 채택
  * 이걸 적고 백트랙킹으로 푸신 분이 있는지 이제 코드를 볼 예정입니다 

---
* 정답 코드
```python
N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
# 가로, 세로 좌표를 그냥 다 찍어버림
# 뭔가 이렇게 살면 안 될 것 같지만..
tetromino = [
  [(0, 0), (0, 1), (1, 0), (1, 1)],
  [(0, 0), (0, 1), (0, 2), (0, 3)],
  [(0, 0), (1, 0), (2, 0), (3, 0)],
  [(0, 0), (0, 1), (0, 2), (1, 0)],
  [(0, 0), (0, 1), (0, 2), (-1, 2)],
  [(0, 0), (1, 0), (1, 1), (1, 2)],
  [(0, 0), (0, 1), (0, 2), (1, 2)],
  [(0, 0), (1, 0), (2, 0), (2, 1)],
  [(0, 0), (0, 1), (1, 1), (2, 1)],
  [(0, 0), (0, 1), (1, 0), (2, 0)],
  [(0, 0), (1, 0), (2, 0), (2, -1)],
  [(0, 0), (1, 0), (1, 1), (2, 1)],
  [(0, 0), (0, 1), (1, 0), (-1, 1)],
  [(0, 0), (0, 1), (1, 0), (1, -1)],
  [(0, 0), (0, 1), (1, 1), (1, 2)],
  [(0, 0), (0, 1), (0, 2), (1, 1)],
  [(0, 0), (1, 0), (1, 1), (1, -1)],
  [(0, 0), (1, 0), (2, 0), (1, -1)],
  [(0, 0), (1, 0), (1, 1), (2, 0)]
]

res = []
for i in range(N):
  for j in range(M):
    for t in tetromino:
      tmp = 0
      for x, y in t:
        try:
          tmp += paper[i + x][j + y]
        except:
          break
      else:
        res.append(tmp)
print(max(res))
```
- 시간복잡도 : O(N x M). 최대 250,000 * 19
- 공간복잡도 : O(N)
- 문제 유형 : 백트랙킹, 구현, 시뮬레이션
---
---
## 4주 공통 문제 2
* 🥇 [백준 16234 인구 이동](https://www.acmicpc.net/problem/16234)
* 접근 방법
	* 개인적으로 공통 문제들 중에서 가장 까다로운 문제였다고 느껴지는 문제
  * BFS로 풀 수 있을 것 같았는데, 백트래킹 연습을 하려면 DFS로 푸는 연습을 해야 할 것 같아서 DFS로 풀어봄
    * 재귀가 깊지 않아서인지 재귀 깊이를 따로 설정해주지 않아도 에러가 나지는 않았음
  * 같은 연합이라는 것을 어떻게 정하고, 하루에 여러 연합이 있을 때 어떻게 묶어서 계산해야 할지 생각하는 게 까다로웠음

* 풀이
  * 바깥에서 무한루프를 돌리되 연합이 없으면 프로그램을 종료하는 식으로 구현
  * 무한루프 1회에서는 2중 for문으로 전체 나라를 돌음. 이 때, visited 처리가 안 된 방문 안 한 나라라면 dfs를 함
  * dfs의 결과를 연합을 이루는 나라의 개수 cnt와 연합국의 위치 좌표를 담은 리스트 country를 받음. 연합국이 만들어지지 않았다면 넘어감
  * 만약 연합국이 만들어졌다면 나라의 개수는 cnt_list에, 연합국 좌표 리스트는 하루의 연합국 리스트인 country_list에 추가함. 왜 추가하냐면 전체 땅을 다 돌아서 연합국의 위치와 개수를 전부 파악한 다음 마지막에 한꺼번에 처리해줘야 섞이는 오류 등이 생기지 않기 때문임
  * country_list에서 연합국들을 하나씩 빼내서 연합국 내의 인구 수를 더하고, 연합국 수로 나눠서 연합국 리스트에 배정한다
  * while 루프 1번에서 country_list 루프가 다 돌고 나면 하루에 일어날 인구 이동이 다 일어난 것이므로 day += 1을 해주고 끝
  * 이것을 연합국이 만들어지지 않을 때까지 반복
  
* 문제
  * 시간 초과 문제가 있었음. visited를 제대로 활용하지 못했기 때문에 일어난 문제였음
  * 시간 초과 코드에서는 while 루프 내에서 visited 표시를 했는데, 바꾼 코드에서는 dfs 내에서 연합국이 될 수 있는지 체크할 때 visited를 표시함. 그러고 나니까 시간 초과가 없어짐
  * while 루프 내에서 visited 표시를 하면 이미 연합국으로 속했을지라도 또 검사하게 되어 비효율적임
---
* 정답 코드
```python
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]
day = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, visited, country, num, cnt):
  # 시간 초과를 없애준 코드
  visited[x][y] = 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
      continue
    if [nx, ny] in country:
      continue
    if L <= abs(land[x][y] - land[nx][ny]) <= R:
      country.append([nx, ny])
      cnt, country = dfs(nx, ny, visited, country, num, cnt + 1)
  return cnt, country

while True:
  visited = [[0 for _ in range(N)] for _ in range(N)]
  num = 1
  cnt = 0
  cnt_list = []
  country_list = []
  for i in range(N):
    for j in range(N):
#       시간 초과의 원인
#       visited[i][j] = 1
      if not visited[i][j]:
        visited[i][j] = 1
        cnt, country = dfs(i, j, visited, [[i, j]], num, 1)
        if cnt == 1:
          continue
        cnt_list.append(cnt)
        country_list.append(country)
        num += 1
  if num == 1:
    break
  for i in range(len(cnt_list)):
    people = 0
    for x, y in country_list[i]:
      people += land[x][y]
    people = people // cnt_list[i]
    for x, y in country_list[i]:
      land[x][y] = people
  day += 1
print(day)
```
- 시간복잡도 : O(N^2)
- 공간복잡도 : O(N^2)
- 문제 유형 : DFS, 시뮬레이션

## 4주 공통 문제 3
* 🥇 [백준 17144 미세먼지 안녕!](https://www.acmicpc.net/problem/17144)
  
* 접근 방법
	* 사실 이 문제가 세 문제 중 가장 무난하다는 생각이 들었음. 요구 조건이 그리 어렵지 않다
  * 단, 미세먼지가 확산할 때 확산량을 합쳐주면 에러가 나므로 확산한 후에 자기 위치에 남은 먼지와 확산되는 위치와 확산량을 따로 구분해주는 것이 포인트
  * 또, 공기청정기가 2칸인데 위쪽은 반시계, 아래쪽은 시계방향이므로 방향벡터를 거꾸로 잘 써먹는 것이 중요했음
   
* 정리된 풀이
	* 비용이 아니라 다른 모든 노드로 이동하는 길이 있는지를 묻는 문제라서 플로이드 워셜이 모든 노드에서 모든 노드로 가는 비용'만'을 계산하는 알고리즘이라는 고정 관념을 가지면 힘든 문제..
  * 의외로 구현은 간단하고 이해하기 쉬움
  
---
* 정답 코드
```python
def solution(n, results):
  score = [[None for _ in range(n)] for _ in range(n)]
  # 승패를 True/False로 지정
  for a, b in results:
    score[a-1][b-1] = True
    score[b-1][a-1] = False

  for i in range(n):
    for j in range(n):
      for k in range(n):
        # 만약 j-i 사이 경기 정보가 없다면 패스
        if not score[j][i]:
          continue
        
        # 만약 j가 i를 이겼고, i가 k를 이겼다면 j가 k를 이긴 것
        # 반대의 경우도 마찬가지임
        if score[j][i] == score[i][k]:
          score[j][k] = score[i][k]
          score[k][j] = not score[i][k]

  res = 0
  for x in range(n):
    # 만약 승부 결정이 나지 않은 짝이 있다면
    # 순위를 알 수 없으므로 넘김
    if None in score[x][:x] + score[x][x+1:]:
      continue
    res += 1
  
  return res
```
```
처음 score  
[[None, True, None, None, None],  
[False, None, False, False, True],   
[None, True, None, False, None],   
[None, True, True, None, None],   
[None, False, None, None, None]]    
처음에는 2번 선수만 그 순위를 알 수 있음  
  
플로이드 워셜 이후의 score  
[[None, True, None, None, True],   
[False, None, False, False, True],   
[None, True, None, False, True],   
[None, True, True, None, True],   
[False, False, False, False, None]]  
이제 5번 선수도 순위를 알 수 있으므로, 결과적으로 2명의 순위를 낼 수 있음
```
- 시간복잡도 : O(n^3)
- 공간복잡도 : O(n^2)
- 문제 유형 : set, 플로이드 워셜, 경로-경로 간 연결 관계 찾기