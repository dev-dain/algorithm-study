## 10주차 공통문제
### [프로그래머스 67257](https://programmers.co.kr/learn/courses/30/lessons/67257)
- 문제 유형: 완전탐색
- 시간 복잡도: O(N)
- 공간 복잡도: O(N)
- 접근 방법
    - 이전에 풀어본 백준 16637번과 유사한 문제라 생각합니다 !
    - 스택과 순열을 활용하여 받을 수 있는 가장 큰 금액을 반환하면 되는 문제였습니다
<br/><br/>
- 풀이
    - 각 연산자에 맞는 수식을 만들어 계산하는 operation 함수를 생성합니다
    - 표현식을 숫자와 연산자로 나누어 스택에 저장하고 수식이 생성되는 경우 opration 매개변수로 넘겨 답을 갱신합니다
    - 가장 큰 값을 구하기 위해 abs() 절대값을 씌워 반환합니다
<br/><br/>
- 코드
```python
from itertools import permutations

def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))
    
def calculate(exp,op):
    array=[]
    tmp=""
    for i in exp:
        if i.isdigit()==True:
            tmp+=i
        else:
            array.append(tmp)
            array.append(i)
            tmp=""
    array.append(tmp)
    
    for o in op:
        stack=[]
        while len(array)!=0:
            tmp = array.pop(0)
            if tmp == o:
                stack.append(operation(stack.pop(), array.pop(0), o))
            else:
                stack.append(tmp)
        array = stack
            
    return abs(int(array[0]))

def solution(expression):
    op = ['+', '-', '*']
    op = list(permutations(op, 3))
    result=[]
    for i in op:
        result.append(calculate(expression, i))
    return max(result)
```

### [프로그래머스 67259](https://programmers.co.kr/learn/courses/30/lessons/67259)
- 문제 유형: 그래프, bfs
- 시간 복잡도: O(NlogN)
- 공간 복잡도: O(n)
- 접근 방법
    - 여러 풀이를 찾아보고 해결했습니다 .. ^^
    - 마지막 테스트케이스에서 계속 오답이 나서 도무지 혼자 해결이 힘들었습니다
    - 기존의 bfs 문제에서 방문처리만 했던 것에 더해 비용까지 기록해야하는 문제였습니다
<br/><br/>
- 풀이
    - 최소 비용을 기록하는 3차원 리스트를 만들고 x, y, 비용과 방향을 담아줍니다
    - 비용은 현재 방향과 다음 이동할 방향이 다르다면 직각을 생성하므로 +600 그렇지 않을 경우 +100 합니다
<br/><br/>
- 코드
```python
import collections
x_move = [1,0,-1,0]
y_move = [0,1,0,-1]
MAX = 987654321
answer = MAX

def bfs(board):
    global answer
    # 최소비용을 기록하는 3차원 리스트
    visited = [[[MAX for y in range(len(board))] for x in range(len(board))] for z in range(4)]
    q = collections.deque()
    # [x, y, cost, dir]
    # dir -> 밑,오른쪽,위,왼쪽 -> 0,1,2,3
    for z in range(4):
        visited[z][0][0]= 0
    
    if board[0][1] != 1:
        q.append([0,1,100,1])
        visited[1][0][1] = 100
    
    if board[1][0] != 1:
        q.append([1,0,100,0])
        visited[0][1][0] = 100
    
    while q:
    	# x축, y축, 비용, 방향
        x, y, cost, dir = q.pop()
        
        for i in range(4):
            n_x = x + x_move[i]
            n_y = y + y_move[i]
            
            # 현재 방향과 다음 방향이 틀리다면 +600
            if dir != i:
                n_cost = cost + 600
            # 같은 경우
            else:
                n_cost = cost + 100
            
            if 0 <= n_x < len(board) and 0 <= n_y < len(board):
                # 범위내에서 벽이 아니라면
                if board[n_x][n_y] != 1:
                	# 해당 [방향][x축][y축]에 기록되어있는 것보다 현재 비용이 작다면, 큐에 넣고 바꾸어준다
                    if visited[i][n_x][n_y] > n_cost:
                        q.append([n_x, n_y, n_cost, i])
                        visited[i][n_x][n_y] = n_cost
    # x축y축 끝의 4방향 중에서 최솟값을 찾는다.
    for z in range(4):
        if answer > visited[z][len(board)-1][len(board)-1]:
            answer = visited[z][len(board)-1][len(board)-1] 
    return answer


def solution(board):
    return bfs(board)
```