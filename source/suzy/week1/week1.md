## 1주차 개별문제
### 1) [프로그래머스 43165](https://programmers.co.kr/learn/courses/30/lessons/43165)
- 문제 유형: 그래프(bfs), 완전탐색
- 시간 복잡도: O(N²)  |  공간 복잡도: O(N)
- 접근 방법
    - n개의 수를 적절히 더하거나 빼서 타겟의 넘버를 만든다
    - 더하거나 빼는 모든 경우를 구해야한다 ( 다음 노드 : 각 단계마다 앞선 노드의 더하고 뺀값 )
    - 모든 경우의 수 중 target 과 같은 경우 방법의 수를 세어준다
<br/><br/>
* 풀이
  * 수를 더하거나 빼는 모든 경우를 탐색한다.
  * 모든 경우를 탐색하기 위해 tmp 를 초기화한다
  * 더한 값과 뺀 값 모두 check 리스트에 저장된다
  * 모든 경우의 수 중 target과 비교하여 같다면 +1 한 결과를 출력한다
<br/><br/>
- 코드
```python
def solution(numbers, target):
    answer = 0
    check = [0]
    
    for num in numbers:
        tmp = []
        for number in check:
            tmp.append(number + num)
            tmp.append(number - num)
        check = tmp
        
    for i in check:
        if i == target:
            answer += 1
    return answer
```
---

### 2) [프로그래머스 43162](https://programmers.co.kr/learn/courses/30/lessons/43162)
- 문제 유형: 그래프 (dfs)
- 시간 복잡도: O(N+M)  |  공간 복잡도: O(N²)
- 접근 방법
    - 주어진 컴퓨터의 개수는 노드를 의미하고 2차원배열 computers 간선을 의미
    - 구해야할 네트워크의 개수는 트리의 개수를 의미
<br/><br/>
* 풀이
  * dfs 재귀적 방법을 사용하여 구현
  * dfs 로 방문하고 빠져나오게 된다면 하나의 네트워크
  * 컴퓨터의 수만큼 반복 확인하여 네트워크 개수를 세어준다
<br/><br/>
- 코드
```python
# DFS
def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]

    def dfs(i):
        visited[i] = 1
        for j in range(n):
            if computers[i][j] and not visited[j]:
                dfs(j)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer
```
