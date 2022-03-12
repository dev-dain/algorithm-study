## 9주차 공통문제
### [백준 21610](https://www.acmicpc.net/problem/21610)
- 문제 유형: 구현
- 시간 복잡도: O(N*M)
- 공간 복잡도: O(N)
- 접근 방법
    - 주어진 조건에 충실하여 .. 구현하면 되는 문제였습니다
    - M번 만큼 이동 횟수를 반복하며 구름을 이동시키고 추가적인 조건을 구현하여 반복 후 물 양의 합을 출력하면 됩니다 !
<br/><br/>
- 풀이
    - 이동한 구름의 위치에서 대각선 4개 방향을 탐색하며 물이 있는 갯수만큼 추가합니다
    - 전체 칸을 탐색하며 물이 2 이상인 칸에 구름을 생성하고 이전에 구름이 존재한 곳에는 생성하지 않습니다
<br/><br/>
- 코드
```python
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
    
# 초기 구름 위치
clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
for _ in range(m):
    d,s = map(int, input().split())
    
    move = []
    for idx in range(len(clouds)):
        x, y = clouds[idx]
        #  0번과 N-1번 인덱스가 연결
        nx = (n + x + (dx[d-1]*s)) % n
        ny = (n + y + (dy[d-1]*s)) % n
        
        move.append((nx,ny)) #구름이 이동한 좌표
    
    # 구름의 위치를 확인하고 물 추가
    cloud_loc = [[False]*n for _ in range(n)]
    for i,j in move:
        graph[i][j] += 1
        cloud_loc[i][j] = True
        
    # 대각선의 위치를 탐색하기 위한 idx
    find = [1,3,5,7]
    for i,j in move:
        cnt = 0
        for f in find:
            fx, fy = i + dx[f], j + dy[f]
            
            if not 0<=fx<n or not 0<=fy<n: # 범위 밖인 경우
                continue
            if graph[fx][fy] == 0 : # 물이 없는 경우
                continue
            
            cnt += 1
        graph[i][j] += cnt
        
    clouds = [] # 새 구름 생성
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= 1: # 물 양이 1이면 제외
                continue
            if not cloud_loc[i][j]:
                clouds.append((i,j))
                graph[i][j] -= 2
print(sum(sum(graph, [])))
```

### [프로그래머스 77486](https://programmers.co.kr/learn/courses/30/lessons/77486)
- 문제 유형: 구현
- 시간 복잡도: O(NlogN)
- 공간 복잡도: O(n)
- 접근 방법
    - 이익의 10% -> 추천인에게 이익 배당 , 나머지는 자신에게 배당
    - 칫솔은 개당 100원이고 10% 를 계산한 금액이 1원 미만인 경우 분배하지 x
<br/><br/>
- 풀이
    - 딕셔너리를 사용해서 주어진 조건에 맞춰 각 노드가 얻게 되는 수익의 총합을 출력하면 되는 문제였습니다
    - 트리 구조의 입력이 주어져서 괜히 어렵게 생각했지만 생각보다 단순히 구현하는 식의 풀이가 나와 기분이 좋았습니다 !
<br/><br/>
- 코드
```python
def solution(enroll, referral, seller, amount):
    
    brush = 100 # 개 당 가격
    
    salary = dict()
    parti = dict() # enroll :  referral
    for i in range(len(enroll)):
        salary[enroll[i]] = 0
        parti[enroll[i]] = referral[i]
    
    # 이익의 10% 배분 / 나머지 나에게 배당
    for i in range(len(seller)):
        s = seller[i]
        price = brush * amount[i]
        
        while s != '-':
            salary[s] += price - (price // 10) # 나머지
            price = price // 10 # 이익
            if price == 0:
                break
            s = parti[s]
    
    return [salary[i] for i in enroll]
```