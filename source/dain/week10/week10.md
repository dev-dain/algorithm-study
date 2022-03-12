## 10주 공통 문제 1
* 2️⃣ [프로그래머스 67257 수식 최대화](https://programmers.co.kr/learn/courses/30/lessons/67257)

* 접근 방법
	* 재귀로 모든 경우를 다 탐색하는 완전탐색 문제
  * 수식 우선순위 조합이 6가지밖에 되지 않기 때문에 6가지를 직접 다 시험해보는 것이 효율적
  * 굳이 수와 연산자를 하나하나 나눠줄 필요가 없는 방법이기 때문에 고정관념 탈피가 중요한 문제였음

* 풀이법
  * (1) 연산자 우선순위 조합 리스트를 만듦 (operators)
  * (2) 각 우선순위별로 cal 함수를 돌려서 그 결과를 answer와 비교해 절댓값이 더 큰 것으로 갱신함
    * (2)-(1) cal 함수에서 만약 2라면(즉, 3번째 연산자까지 왔다면) eval로 계산해서 값을 반환
    * (2)-(2) 2가 아니라면 cal 함수를 다시 호출해서 eval을 돌림
   
---
* 정답 코드
```python
def cal(operator, n, exp):
    if n == 2:
        return str(eval(exp))
    res = eval(operator[n].join([
        cal(operator, n+1, e) for e in exp.split(operator[n])
    ]))
    return str(res)

def solution(expression) :
    answer = 0
    operators = [
        ['+', '-', '*'],
        ['+', '*', '-'],
        ['*', '-', '+'],
        ['*', '+', '-'],
        ['-', '*', '+'],
        ['-', '+', '*']
    ]
    for op in operators :
        res = int(cal(op, 0, expression))
        answer = max(answer, abs(res))
        
    return answer
```
- 시간복잡도 : O(1)
- 공간복잡도 : O(N)
- 문제 유형 : 완전탐색, 분할정복
---
---
## 10주 공통 문제 2
* 3️⃣❓ [프로그래머스 67259 경주로 건설](https://programmers.co.kr/learn/courses/30/lessons/67259)

* 접근 방법
	* 처음에 최단 경로 문제라고 생각해서 다익스트라로 풀어보려다가 망함.. 여기서 시간을 너무 많이 빼앗김
  * 결국 이건 정답 코드를 여러 개 찾아봤는데 문제는 정답 코드를 참고해도 테스트 케이스 25번이 에러가 나서 아직도 통과를 못 하는 중입니다 ^_ㅠ
  * 관건은 큐에 좌표뿐 아니라 방향과 비용을 함께 담아야 한다는 것

* 풀이
  * (1) tmp_board라는 판을 똑같이 N*N 크기로 만들어서 최대값으로 채움. 이 tmp_board는 그 경로로 가는 최소값이 담기는 판
  * (2) 큐에 오른쪽, 아래로 가는 방향을 넣고 반복문 시작
  * (3) 만약 큐에서 꺼낸 x, y가 N-1이라면 마지막에 도달한 것이므로 answer와 비용을 비교해서 더 작은 값을 채택
  * (4) N-1, N-1이 아니라면 아직 진행할 수 있으므로 방향 벡터를 돌리기 시작. 만약 N 범위를 탈출하거나 벽이 있다면 넘어가고, 마찬가지로 반대쪽으로 돌아가는 방향이어도 넘어감
  * (5) dir == i라면 직선 도로이므로 100 추가, 그렇지 않다면 코너이므로 500+100 추가
  * (6) nx, ny 좌표의 임시 비용이 원래 비용보다 적다면 새로 최소값으로 갱신
  * (7) 큐가 빌 때까지 반복 후 answer 반환
  
---
* 정답 코드
```python
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solution(board):
    answer = 1e9
    N = len(board)
    tmp_board = [[1e9 for _ in range(N)] for _ in range(N)]

    qu = deque()
    qu.append((0, 0, 1, 0))
    qu.append((0, 0, 2, 0))

    while qu:
        x, y, dir, tmp_cost = qu.popleft()
        
        if x == N-1 and y == N-1:
            answer = min(answer, tmp_cost)
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            cost = 0
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 1:
                continue
            if dir+2 == i or dir-2 == i:
                continue
            if dir == i:
                cost = 100
            else:
                cost = 500 + 100
            if tmp_board[nx][ny] >= tmp_cost + cost:
                tmp_board[nx][ny] = tmp_cost + cost
                qu.append((nx, ny, i, tmp_cost + cost))
            
    return answer
```
- 시간복잡도 : O(N^2)
- 공간복잡도 : O(N^2)
- 문제 유형 : 완전탐색