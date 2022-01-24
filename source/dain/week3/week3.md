## 3주 공통 문제 1
* 🥇❓ [백준 1987 알파벳](https://www.acmicpc.net/problem/1987)

* 접근 방법
	* R, C가 최대 20 * 20이므로 최대 400칸이 될 수 있음. 그래서 시간복잡도가 만약 O(N^2)라면 좀 슬플 문제
  * 처음 단순한 BFS + DP라고 생각해서 덱을 사용해 풀었지만 1시간을 풀어봐도 틀리는 테스트 케이스가 생김
  * alphabet이라는 배열을 r*c만큼 만들어 칸별로 만들어질 수 있는 최대 길이를 누적해서 구해야겠다고 생각해서 풀이했음
  * 그런데도 틀려서 결국 검색  
   
* 정리된 풀이
	* DFS로 푼 풀이와 set을 이용해서 푼 풀이가 있었음. set을 큐처럼 사용해서 풀이. 
  * set은 pop했을 때 임의의 요소가 나오는데, 시간복잡도는 O(1)임
  * 가능한 경우들을 전부 시도해보되 백트랙킹하는 방법을 사용
  * 다음에 볼 것이 아직 알파벳 모음에 없다면 알파벳을 추가하고, 셋에 넣은 다음 길이를 비교해 더 긴 길이를 최대값으로 넣음
  * 즉, 어떤 알파벳이 어떤 순서로 들어가는지는 상관없고 최대값이 얼마인지가 중요하기 때문에 길이는 따로 관리하는 것이 더 효율적인 문제 

---
* 오답 코드
```python
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(a, b):
  qu = deque([[a, b]])
  alphabet[a][b] += board[a][b]
  
  while qu:
    x, y = qu.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= r or ny >= c:
        continue
      if len(alphabet[nx][ny]) > len(alphabet[x][y]):
        continue
      if board[nx][ny] in alphabet[x][y]:
        continue
      qu.append([nx, ny])
      alphabet[nx][ny] = alphabet[x][y] + board[nx][ny]

  print(alphabet)
  return 


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
alphabet = [['' for _ in range(c)] for _ in range(r)]
print(alphabet)
print(bfs(0, 0))
```

* 정답 코드
```python
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def solution():
  dp = 1  # 최대값
  # x, y, visited
  qu = set([(0, 0, board[0][0])])
  
  while qu:
    # 가능한 경우들을 시도해보되 백트랙킹하기
    # set에서 pop하면 임의의 요소가 나옴
    x, y, visited = qu.pop()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= r or ny >= c:
        continue
      # 다음에 볼 것이 아직 알파벳 모음에 없다면
      if board[nx][ny] not in visited:
        next = visited + board[nx][ny]  # 다음 알파벳 추가
        qu.add((nx, ny, next))  # 큐로 이동
        dp = max(dp, len(next)) # 어떤 것이 더 큰지 비교해 최대값 넣기
  return dp

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
print(solution())
```
- 시간복잡도 : ? (O(n) 같은데.. 잘 모르겠네요)
- 공간복잡도 : O(n)
- 문제 유형 : BFS/DFS, DP, 백트랙킹
---
---
## 3주 공통 문제 2
* 🥇 [백준 1504 특정한 최단 경로](https://www.acmicpc.net/problem/1504)
* 접근 방법
	* 한 점에서 다른 한 점으로 이동할 때 최단 거리를 구한다는 설명에서 다익스트라를 사용해 풀 수 있다는 힌트를 얻음.
  * 문제는 임의의 두 정점을 반드시 지나면서 최단 경로일 것이라는 조건
  * 임의의 두 정점을 어떻게 지날까?
    * 바로 시작부터 다른 두 정점으로 가는 최단 경로를 구해 합해주면 된다. 간단한 아이디어
  
* 문제
  * 비용을 다익스트라 함수에서 자체로 관리하거나(즉, 함수를 호출할 때마다 새로운 비용 리스트가 생겨야 함) 매번 초기화해줘야 한다는 점을 알아야 함
  * 그런데 계속 시간 초과가 나고 코드가 통과하지 못함. 분명히 정답은 맞는데..
  * 알고 보니, 힙에 넣는 [비용, 노드]를 리스트 형태로 넣었기 때문에 나는 것. 설마 하고 (비용, 노드)처럼 튜플 형태로 넣어보니 어이없게도 시간 초과가 나지 않고 통과한다. 
  * 괜히 시간 초과가 난다면, 그리고 변경해야 하는 것이 아니라면 튜플로 넣기.
---
* 정답 코드
```python
import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

# 경유해야 할 노드가 있다면 거기까지 가는 노드의 최단경로를 구해서 합하면 된다
# 비용은 함수를 호출할 때마다 관리한다.
def dijkstra(start, end):
  qu = []
  # 여기를 [0, start]로 넣으면 시간초과가 남
  heapq.heappush(qu, (0, start))
  dist = [INF for _ in range(n+1)]
  dist[start] = 0

  while qu:
    cur_cost, node = qu.pop()
    # if cur_cost > dist[node]:
    #   continue
    for adj_cost, adj_node in graph[node]:
      cost = cur_cost + adj_cost
      if cost < dist[adj_node]:
        dist[adj_node] = cost
        heapq.heappush(qu, (cost, adj_node))
  
  return dist[end]

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((c, b))
  graph[b].append((c, a))
v1, v2 = map(int, input().split())
# 비용은 바깥에서 관리하면 다익스트라 함수를 호출할 때마다 매번 초기화해야 한다
# 귀찮으므로 그냥 없애버린다
# dist = [sys.maxsize for _ in range(n+1)]

p1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
p2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)
res = min(p1, p2)
print(res if res < INF else -1)
```
- 시간복잡도 : O(ElogE), E는 간선 개수
- 공간복잡도 : O(N)
- 문제 유형 : 최단 경로, 다익스트라 알고리즘

## 3주 공통 문제 3
* 3️⃣❓ [프로그래머스 49191 순위](https://programmers.co.kr/learn/courses/30/lessons/49191)
  
* 접근 방법
	* 딱 봤을 때 플로이드 워셜인 걸 알아보기 힘듦. 뭔가 그래프처럼 풀거나 아니면 set을 쓰면 좋겠다는 생각은 드는데 탐색의 방법을 정하기 어려움. 문제 독해에 힘써야겠다는 생각이 절실해짐
  * 플로이드 워셜이라는 힌트를 보고 왜 플로이드 워셜인지 생각해봄
  * 이 문제는 특이하게 비용을 물어보는 문제가 아니라 연결 관계를 간접적으로 묻는 문제
  * 규칙을 살펴보면 A가 B를 이겼을 때, C가 A를 이기면 C는 당연히 B를 이긴다. 
    * 즉, C-A-B 순으로 간접 연결 관계가 형성되어 있다는 것을 의미함
  * 그래서 어떤 선수(노드)가 자기 외의 다른 모든 선수(노드)들과 직간접적인 승부 결과(연결 관계)가 있다면 그의 순위를 알 수 있는 것이므로 이 선수를 result에 포함시킬 수 있는 것임
  * 정리하자면, 이 문제는 주어진 모든 노드에서 다른 모든 노드와 직간접적으로 연결되어 있는지 묻는 문제이기 때문에 플로이드 워셜로 풀 수 있는 문제임
   
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