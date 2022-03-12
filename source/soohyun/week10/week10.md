## 10주차 공통문제
### [프로그래머스 67257 수식 최대화](https://programmers.co.kr/learn/courses/30/lessons/67257)
- 문제 유형: 완전탐색
- 시간 복잡도: O(N^2)
- 공간 복잡도: O(N)
- 접근 방법
    - 먼저 세 연산자의 모든 경우를 구하기 위해 순열을 사용해야겠다고 생각했다.
    - 그리고 모든 경우를 탐색하면서 우선순위에 따른 식의 결과값을 구하면 된다.
    - 이 때, 우선순위에 따른 결과값을 구하기 위해서는 스택을 활용해야 했다.
    - 또한, 모든 경우을 탐색하기 위해 식을 deepcopy 해야한다.
<br/><br/>
- 풀이
    1. 모든 연산자 우선순위 경우를 구한다.
    2. 입력받은 식을 숫자, 연산자로 분리한다.
    3. 모든 연산자 경우에 따른 식의 결과값을 구한다. (스택 활용)
    4. 식에서 값을 하나 가져와 그것이 현재 우선순위 연산자와 같다면 식을 계산하여 스택에 저장한다.
    5. 같지 않다면 그 값을 스택에 다시 넣는다. (다음 우선순위의 연산자에서 계산하기 위해서!)
    6. 식의 계산이 끝나면 결과값을 리턴한다.
    7. 마지막으로 결과를 출력한다.
<br/><br/>
- 코드
```python
from itertools import permutations
import copy

def cal(op, exp):
    # 연산자 우선순위에 따른 식의 결과값 구하기
    for o in op:
        stack = []
        while exp:
            e = exp.pop(0)
            if e == o: # 현재 우선순위 연산자와 같다면 식을 계산
                stack.append(str(eval(stack.pop() + o + exp.pop(0)))) # 좌측 숫자 + 연산자 + 우측 숫자
            else:
                stack.append(e)
        exp = stack # 다음 연산자로 넘어가기 위해 stack에 남은 것들을 exp에 저장
    
    return abs(int(exp[0]))
    
def solution(expression):
    answer = 0
    op = ['*', '+', '-']
    ops = list(permutations(op, 3)) # 가능한 연산자 우선순위 조합
    exp = []
    num = ''
    
    # 숫자와 연산자 분리하기
    for e in expression:
        if e.isdigit():
            num += e
        else:
            exp.append(num)
            exp.append(e)
            num = ''
    exp.append(num) # 마지막 숫자까지 추가
    
    for op in ops:
        result = cal(op, copy.deepcopy(exp))
        answer = max(answer, result)
            
    return answer
```

### [프로그래머스 67259 경주로 건설](https://programmers.co.kr/learn/courses/30/lessons/67257)
- 문제 유형: 그래프, 완전탐색
- 시간 복잡도: O(NM)
- 공간 복잡도: O(N)
- 접근 방법
    - 기존 그래프 문제와 비슷하게 동서남북으로 이동하면서 가능한 경로를 찾는 문제였다.
    - 직선 경로인지, 코너 경로인지 구분하여 비용을 구하는 것이 핵심이었다.
    - 직선 경로는 현재 위치 방향 = 다음 위치 방향 일 때이고, 코너 경로는 현재 위치 방향 != 다음 위치 방향 일 때였다.
    - BFS를 활용하여 코드를 완성했는데 마지막 테스트 케이스만 통과가 되지 않았다.
    - 질문하기를 살펴보니 예외의 케이스가 존재했고, BFS + DP를 활용하여 풀어야 했다.
<br/><br/>
- 풀이
    1. 방향, 위치에 따른 3차원 비용 리스트를 생성한다.
    2. 시작점, 0행 1열, 1행 0열을 먼저 초기화한다,
    3. 큐에서 노드를 하나 가져와 이동 가능한 범위이며 빈칸인 경우 다음 위치의 비용을 구한다.
    4. 다음 위치의 비용이 기존 다음 위치의 비용보다 작다면 비용을 갱신한다.
    5. 최소 비용을 출력한다.
<br/><br/>
- 코드
```python
from collections import deque

def solution(board):
    n = len(board)
    cost = [[[1e9] * n for _ in range(n)] for _ in range(4)] # 방향, 위치에 따른 비용 리스트
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
    queue = deque([])
    
    # 시작점 초기화
    for i in range(4):
        cost[i][0][0] = 0
        
    # 0행 1열 초기화
    if board[0][1] == 0:
        queue.append([0, 1, 0, 100])
        cost[0][0][1] = 100
    
    # 1행 0열 초기화
    if board[1][0] == 0:
        queue.append([1, 0, 1, 100])
        cost[1][1][0] = 100
    
    while queue:
        x, y, d, c = queue.popleft() # 위치, 방향, 비용
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]: # 이동 가능한 범위이며 빈칸인 경우
                new_cost = c + 100 if d == i else c + 600 # 다음 위치의 비용
                if cost[i][nx][ny] > new_cost: # 기존 다음 위치 비용보다 더 작다면 비용 갱신
                    cost[i][nx][ny] = new_cost
                    queue.append([nx, ny, i, new_cost])   
    
    return min([cost[i][-1][-1] for i in range(4)]) # 최소 비용
```