## 7주차 공통문제
### [백준 16637](https://www.acmicpc.net/problem/16637)
- 문제 유형: 완전탐색
- 시간 복잡도: O(N)
- 공간 복잡도: O(N)
- 접근 방법
    - 괄호가 존재하지 않는 경우와 괄호가 존재하는 경우로 나누어 줍니다
    - 괄호가 어디에 위치할때 최대값인지 출력합니다
<br/><br/>
- 풀이
    - 입력 받은 문자열을 문자와 연산자로 나누고 각 연산자의 수식을 계산하는 함수를 선언합니다
    - 재귀적으로 연산자 idx, 계산값을 ret를 매개변수로 갖는 dfs 함수를 호출하여 괄호의 위치에 따라 계산된 값의 최대값을 반환합니다  
<br/><br/>
- 코드
```python
import sys
input = sys.stdin.readline

n = int(input())
m = input()

# 각 연산자 계산
def cal(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2

max_sum = float('-inf')
# 완전탐색
def dfs(idx, ans):
    global max_sum
    if idx >= len(opr):
        max_sum = max(max_sum, ans)
        return
    
    dfs(idx+1, cal(ans,num[idx+1],opr[idx]))
    
    # 괄호가 뒤에 존재하는 경우
    if idx+1 < len(opr):
        dfs(idx+2, cal(ans, cal(num[idx+1],num[idx+2],opr[idx+1]), opr[idx]))
        
num,opr = [], []
def sol(m):
    # 숫자와 연산자 분리
    for i in m[:-1]:
        if i.isdigit():
            num.append(int(i))
        else:
            opr.append(i)
    dfs(0, num[0])
sol(m)
print(max_sum)
```

### [백준 17136](https://www.acmicpc.net/problem/17136)
- 문제 유형: 구현, 완전탐색
- 시간 복잡도: O(N^2)
- 공간 복잡도: O(N)
- 접근 방법
    - 각 색종이를 활용하여 1이 적힌 칸을 색종이로 덮어야합니다
    - 1이 적힌 모든 칸을 붙이는데 필요한 색종이의 최소의 개수를 반환해야합니다
<br/><br/>
- 풀이
    - 색종이로 가릴 수 있는지 없는지 확인한 후 1을 만나면 붙이게 된 경우임으로 0으로 떼는 경우가 존재한다면 다시 1로 
    - 그래프를 돌며 최대로 가릴 수 있는 경우를 확인합니다
<br/><br/>
- 코드
```python
import sys
input = sys.stdin.readline

n = 10
graph = [list(map(int, input().split())) for _ in range(n)]
papers = [0,5,5,5,5,5] # 각 색종이 개수

# 색종이를 붙일 수 있는지 확인
def checkarr(x,y,size):
    for i in range(x,x+size):
        for j in range(y,y+size):
            if 0<=i<n and 0<=j<n and graph[i][j] == 1:
                pass
            else:
                return False
    return True

# 색종이를 붙이거나 떼기
def updatepaper(x,y,size,method):
    # 붙였을 경우 0으로 떼는 경우 1로
    for i in range(x, x+size):
        for j in range(y, y+size):
            graph[i][j] =  method
            
result = 25
# 완전탐색 dfs
def dfs(cnt):
    global result
    
    if cnt > result:
        return
    
    F = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                x,y = i,j
                F = 1
                break
        if F ==1 :
            break
        
    # 1이 더이상 없을 경우
    if F == 0:
        if cnt < result:
            result = cnt
        return
    
    for size in range(5,0,-1): # 5부터 1까지 색종이 size
        if papers[size]>0 and checkarr(x,y,size):
            updatepaper(x,y,size,0)
            papers[size] -= 1
            dfs(cnt+1)
            updatepaper(x,y,size,1)
            papers[size] += 1

dfs(0)
if result == 25:
    print(-1)
else:
    print(result)
```

### [백준 17406](https://www.acmicpc.net/problem/17406)
- 문제 유형: 구현, 완전탐색
- 시간 복잡도: O(N^M)
- 공간 복잡도: O(N)
- 접근 방법
    - 모든 순서를 정해야함으로 순열을 사용합니다
    - 배열을 복사하여 회전하는 경우를 모두 계산하고 가장 최솟값을 출력합니다
<br/><br/>
- 풀이
    - 모든 순서에 대하여 배열을 복사하여 회전합니다
    - 배열의 각 행 중 합이 가장 작은 값을 출력합니다
<br/><br/>
- 코드
```python
from itertools import permutations
from copy import deepcopy
import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
rcs = [list(map(int, input().split())) for _ in range(k)]

ans = float('inf')

# 회전 순서
for p in permutations(rcs, k):
    # 원본 복사
    cp_a = deepcopy(a)
    for r,c,s in p:
        r -= 1
        c -= 1
        for n in range(s,0,-1):
            tmp = cp_a[r-n][c+n]
            cp_a[r-n][c-n+1:c+n+1] = cp_a[r-n][c-n:c+n]  # 맨 위쪽
            
            for row in range(r-n, r+n): # 왼쪽 테두리
                cp_a[row][c-n] = cp_a[row+1][c-n]
                
            cp_a[r+n][c-n:c+n] = cp_a[r+n][c-n+1:c+n+1] # 맨 아리쪽
            
            for row in range(r+n, r-n,-1): # 오른쪽 테두리
                cp_a[row][c+n] = cp_a[row-1][c+n]
                
            cp_a[r-n+1][c+n] = tmp
            
    # 각 행의 최소값
    for row in cp_a:
        ans = min(ans, sum(row))
print(ans)
```