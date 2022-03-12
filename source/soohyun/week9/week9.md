## 9주차 공통문제
### [프로그래머스 77486 다단계 칫솔 판매](https://programmers.co.kr/learn/courses/30/lessons/77486)
- 문제 유형: 구현, 시뮬레이션
- 시간 복잡도: O(N^2)
- 공간 복잡도: O(N)
- 접근 방법
    - 문제가 긴 것을 보니 구현 문제구나 싶었다. 문제를 꼼꼼히 읽는 것이 중요했다.
    - 판매원 이름별로 이익을 구해야해서 딕셔너리를 사용하는 것이 편할 것이라고 생각했다.
    - 주의해야 할 조건은, 분배할 수익이 1원 미만인 경우 수익을 분배하지 않는 것이었다!
<br/><br/>
- 풀이
    1. 조직 관계와 판매원별 이익을 저장할 딕셔너리를 생성한다.
    2. 조직 관계를 구하고, 판매원별 이익을 초기화한다.
    3. 판매 기록에 따른 판매원별 이익을 구한다.
        - 더 이상 이익을 분배할 대상이 없을 때까지 이익 분배를 한다.
        - 분배할 이익이 1원 미만인 경우 현재 판매원이 이익을 다 가지고 이익 분배를 종료한다
        - 분배할 이익이 1원 이상인 경우에는 판매원의 center 여부에 따라 처리를 해준다.
        - 판매원이 center라면 더 이상 이익을 분배할 대상이 없으므로 모든 이익을 가진다.
        - 그렇지 않다면, 남은 이익을 가진다.
        - 다음 이익 분배를 위해 현재 판매원과 이익을 변경한다.
    4. 문제에서 요구하는 조건에 맞게 결과를 출력하기 위해 출력 형식을 맞춰주고 출력한다.
<br/><br/>
- 코드
```python
def solution(enroll, referral, seller, amount):
    graph, answer = {'-': ''}, {'-': 0} # 조직 관계, 판매원별 이익
    result = []
    
    # 조직 관계 구하기, 판매월별 이익 초기화
    for e, r in zip(enroll, referral):
        graph[e] = r
        answer[e] = 0
    
    # 판매 기록에 따른 판매원별 이익 구하기
    for i, s in enumerate(seller):
        person = s # 현재 판매원
        money = amount[i] * 100 # 현재 판매원의 이익
        
        while person != '':
            give = int(money * 0.1) # 분배할 이익
            
            if give < 1: # 분배할 이익이 1원 미만일 경우 이익 분배를 종료한다
                answer[person] += money
                break
            else:
                if person == '-': # 현재 판매원이 center인 경우 이익을 분배할 대상이 없으므로 모든 이익을 가진다
                    answer[person] += money
                else: # 그렇지 않은 경우 남은 이익을 가진다
                    answer[person] += money - give

            money = give
            person = graph[person]
    
    # enroll에 따른 판매원별 이익 구하기
    for e in enroll:
        result.append(answer[e])
        
    return result
```

### [백준 21610 마법사 상어와 비바라기](https://www.acmicpc.net/problem/21610
- 문제 유형: 구현, 시뮬레이션
- 시간 복잡도: O(NM)
- 공간 복잡도: O(N)
- 접근 방법
    - 문제에 주어진대로 구현만 하면 되는 문제여서 특별한 알고리즘을 생각할 필요는 없었다.
    - 대신 구현 문제이기 때문에 제시된 조건에 주의해야 했다.
<br/><br/>
- 풀이
    1. 필요한 정보를 저장할 변수를 생성한다.
    2. 현재 구름 리스트에 있는 구름을 가져와 이동시킨 후 이동한 위치의 물의 양을 1 증가시킨다.
    3. 물복사 마법으로 대각선에 물이 있는 구름 위치의 물의 양을 증가시킨다.
    4. 다음 구름이 생길 위치를 구하고 현재 구름은 없앤다.
    5. 물의 양의 합을 출력한다.
<br/><br/>
- 코드
```python
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
move = [list(map(int, input().split())) for _ in range(m)]
# 서, 서북, 북, 동북, 동, 동남, 남, 서남
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
cloud, new_cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]], [] # 현재 구름 위치, 다음 구름 위치

for d, s in move:
    d -= 1
    visited = [[0] * n for _ in range(n)] # 각 위치의 구름 방문 확인 리스트
    loc = [] # 이동한 구름 위치

    # 구름이 이동한 위치의 물의 양이 1 증가
    for x, y in cloud:
        nx = (x + s * dx[d]) % n
        ny = (y + s * dy[d]) % n
        board[nx][ny] += 1
        visited[nx][ny] = 1
        loc.append([nx, ny])
    
    # 물복사 버그 마법으로 해당 위치의 물의 양이 증가
    for x, y in loc:
        for i in [1, 3, 5, 7]:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > 0:
                board[x][y] += 1

    # 다음 구름 위치 구하기
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and visited[i][j] == 0:
                new_cloud.append([i, j])
                board[i][j] -= 2

    cloud, new_cloud = new_cloud, []

print(sum([sum(b) for b in board])) # 물의 양의 합 
```