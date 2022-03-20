## 11주차 공통문제
### [프로그래머스 42627 디스크 컨트롤러](https://programmers.co.kr/learn/courses/30/lessons/42627)
- 문제 유형: 힙
- 시간 복잡도: O(N)
- 공간 복잡도: O(N)
- 접근 방법
<br/><br/>
- 풀이
    - 먼저 작업 소요 시간이 짧은 작업부터 처리하는 것이 최소 평균 작업 시간을 구할 수 있다는 것을 파악했다.
    - 그래서 힙에 소요 시간 기준으로 저장될 수 있도록 [소요 시간, 작업 요청 시간] 순으로 저장하면 됐다.
    - 작업을 언제 힙에 넣고 빼야할지 감이 안와서 다른 사람의 풀이 방법을 약간 참고했다.
    - 이것을 알고나니 코드 작성을 수월했다.
<br/><br/>
- 코드
    1. 모든 작업이 완료될 때까지 while문을 반복한다.
    2. 현재 시점(시간)에서 처리할 수 있는 작업을 힙에 저장한다.
    3. 처리할 작업이 없는 경우 다음 시간으로 넘어간다.
    4. 처리할 작업이 있는 경우 작업을 처리한다.
        - 작업 완료 시간을 현재 시간으로 변경한다.
        - 현재 시간을 작업 종료 시간으로 변경한다.
        - 모든 작업 시간에 해당 작업 시간을 추가한다.
        - 완료한 작업 수에 +1을 해준다.
    5. 모든 작업이 완료되면 최소 평균 작업 시간을 출력한다.
```python
import heapq

def solution(jobs):
    answer, i, start, now = 0, 0, -1, 0 # 모든 작업 시간, 완료한 작업 수, 최근 작업 완료 시간, 현재 시간
    heap = []
    
    while i < len(jobs):
        # 현재 시점에 처리할 수 있는 작업을 힙에 저장
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]]) # [소요 시간, 작업 요청 시간] 순으로 저장
        
        # 처리할 작업이 있는 경우 작업을 처리한다
        if heap:
            work = heapq.heappop(heap)
            start = now
            now += work[0]
            answer += now - work[1]
            i += 1 #
        # 처리할 작업이 없는 경우 다음 시간으로 넘어간다
        else:
            now += 1
    
    return answer // len(jobs)
```

### [프로그래머스 43163 단어 변환](https://programmers.co.kr/learn/courses/30/lessons/43163)
- 문제 유형: DFS, BFS
- 시간 복잡도: O(N)
- 공간 복잡도: O(N)
- 접근 방법
    - 재귀함수의 탈출 조건과 반복되는 작업이 명확하기 때문에 DFS를 사용하기로 했다.
    - 단어와 target이 같아지면 재귀함수를 탈출하면 되고 이 때, 변환 횟수를 갱신하면 된다.
    - 단어와 target이 같지 않다면 변환할 수 있는 단어를 찾아 변환하면 된다.
    - DFS를 사용해서 모든 경우를 다 해보면 되는 문제였다. 오랜만에 내가 풀 수 있는 재귀함수 문제여서 좋았다 ^~^
<br/><br/>
- 풀이
    1. 사용한 단어인지 확인할 수 있는 리스트인 checked를 생성한다.
    2. 현재 단어에서 변환할 수 있는 단어를 찾는다.
    3. 모든 단어를 탐색하여 사용한 단어가 아닌 경우 현재 단어와 해당 단어의 다른 문자 개수를 센다.
    4. 다른 문자 개수가 1개라면 변환할 수 있는 단어이므로 재귀함수를 호출한다.
    5. 현재 단어가 target과 같아지면 변횐 횟수를 갱신하고 리턴한다.
    6. 마지막으로 조건에 따른 결과를 출력한다.
<br/><br/>
- 코드
```python
answer = 1e9 # 변환 횟수

def dfs(word, cnt, target, words, checked):
    global answer
    
    # 단어가 targer과 같아지면 변환 횟수를 갱신하고 리턴
    if word == target:
        answer = min(answer, cnt) 
        return
    
    # 변환할 수 있는 단어를 찾아 변환한다
    for i in range(len(words)):
        if not checked[i]: # 사용한 단어가 아닌 경우
            diff = 0
            for a, b in zip(word, words[i]): # 다른 문자 개수를 센다
                if a != b:
                    diff += 1
            
            # 다른 문자가 1개인 경우 단어를 변환한다
            if diff == 1:
                checked[i] = 1
                dfs(words[i], cnt+1, target, words, checked)
                checked[i] = 0 # 초기화
    
def solution(begin, target, words):
    checked = [0] * len(words) # 사용한 단어인지 확인하는 리스트
    dfs(begin, 0, target, words, checked)
    
    return answer if answer != 1e9 else 0
```
