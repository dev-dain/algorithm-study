## 11주차 공통문제
### [프로그래머스 42627](https://programmers.co.kr/learn/courses/30/lessons/42627)
- 문제 유형: 
- 시간 복잡도: O(NlogN)
- 공간 복잡도: O(N)
- 접근 방법
    - 힙을 사용하지 않고 리스트와 정렬로만 구현했더니 테스트 케이스 하나 제외 다 틀리다고 나와서 1차 멘붕에 빠졌습니다
    - [[1,10],[3,3],[10,3]] 테스트 케이스를 더 찾아보니 작업시간이 1인 경우를 고려하지 않아서 ..
<br/><br/>
- 풀이
    - 작업의 소요시간을 오름차순으로 정렬하여 작업량만큼 반복하고 시작점이 0이 아닌 1로 시작하는 경우 1을 더해줍니다
    - 시작점은 다음 작업량을 더한 값으로 갱신합니다
<br/><br/>
- 코드
```python
def solution(jobs):
    answer = 0
    # 작업시간 기준 오름차순으로 정렬
    job = sorted(jobs, key=lambda x:x[1])

    # 테스트 케이스 추가 [[3, 3], [10, 3], [1, 10]]
    
    start = 0
    while job:
        for i in range(len(job)): # 작업량만큼 돌면서
            if job[i][0] <= start:
                start += job[i][1] # 시작점 갱신
                answer += start - job[i][0] # 작업량
                job.pop(i)
                break

            if i == len(job) - 1: # 시작점이 1에서 시작하는 경우
                start += 1
    
    return answer // len(jobs)
```

### [프로그래머스 43163](https://programmers.co.kr/learn/courses/30/lessons/43163)
- 문제 유형: 그래프, bfs
- 시간 복잡도: O(NlogN)
- 공간 복잡도: O(n)
- 접근 방법
    - bfs 로 탐색하면서 하나의 알파벳이 다른 경우에만 단어를 변환해줍니다
    - 한 번에 한 개의 알파벳만 바꿀 수 있는 경우를 구현하다가 .. 해당 부분의 다양한 풀이를 찾아보았습니다
<br/><br/>
- 풀이
    - target 단어가 words 배열에 존재하는 경우 bfs 를 탐색하고 현단어가 target 일 경우 depth 를 반환합니다
    - 두 문자열의 서로 다른 부분을 셀 때 zip 함수를 활용하여 서로 다른 부분을 체크합니다
<br/><br/>
- 코드
```python
def bfs(begin, target, words, visited):
    count = 0
    stack = [(begin, 0)]
    while stack:
        cur, depth = stack.pop()
        if cur == target:
            return depth
        
        for i in range(len(words)):
            if visited[i] == True:
                continue
            cnt = 0
            for a,b in zip(cur, words[i]): # 서로 다른 부분 check
                if a!=b:
                    cnt += 1
            if cnt == 1:
                visited[i] = True
                stack.append((words[i], depth+1))
            

def solution(begin, target, words):
    answer = 0
    # words 존재하지 않는 경우
    if target not in words:
        return 0

    visited = [False]*(len(words))

    answer = bfs(begin, target, words, visited)

    return answer
```