## 11주 공통 문제 1
* 3️⃣❓ [프로그래머스 42627 디스크 컨트롤러](https://programmers.co.kr/learn/courses/30/lessons/42627)

* 접근 방법
	* 힙을 써야겠다는 건 알겠는데 냅다 다 힙에 집어넣는 게 아니라 조건에 맞을 때만 힙에 집어넣어야하는 문제였어서.. 매우 힘들었음
  * 거의 1시간 동안 대기 시간을 최소한으로 만들도록 힙을 2개 만들어야 하는 건지 고민하다가 인터넷에서 코드를 찾아본 문제
  * 솔직히.. 아직도 정확히 어떻게 푸는 건지 모르겠어요

* 풀이법
  * (1) 일단 들어온 jobs는 정렬하지 않은 채로 변수들과 힙을 선언해줌. 변수는 작업 시간, 처리한 작업 개수, 마지막 작업 시간
  * (2) 모든 작업을 다 끝내기 전까지 (3)부터 반복
  * (3) jobs에 들어 있는 일의 시작 시간과 작업에 필요한 시간을 루프를 돌려서, 이 작업이 들어온 시간이 전체 시스템의 마지막보다 나중이고 시작 시간이 전체 시간보다는 같거나 작은 경우에만 힙에 추가
  * (4) for루프가 끝나고 힙에 뭔가 작업이 있다면 하나 빼내는데, 이 때 work를 기준으로 작업 시간이 가장 짧은 것을 뽑게 됨. 전체 time에 해당 작업의 작업 시간을 추가하고 답 갱신, cnt도 갱신
  * (4)-(1) 만약 for루프가 끝났을 때 힙에 작업이 없다면 단순히 time을 1 늘리고 다시 while 루프 시작
   
---
* 정답 코드
```python
import heapq

def solution(jobs):
    answer = 0

    heap = []
    time = cnt = 0
    end = -1

    # 모든 작업이 끝나기 전까지..
    while cnt < len(jobs):
        for start, work in jobs:
            # 현재 작업의 시작 시간이 마지막 작업의 시간보다 나중이며.. 전체 시간보다 같거나 작을 때 추가
            if end < start and start <= time:
                heapq.heappush(heap, (work, start))
        
        # 힙에 작업이 있다면
        if len(heap):
            work, start = heapq.heappop(heap)
            end = time
            time += work    # 해당 작업의 소요 시간을 추가
            answer += (time - start)    # 답 갱신
            cnt += 1
        else:   # 힙에 작업이 없으면 시간 1 늘리기
            time += 1

    return answer // len(jobs)
```
- 시간복잡도 : O(NlogN)
- 공간복잡도 : O(N)
- 문제 유형 : 우선순위 큐
---
---
## 11주 공통 문제 2
* 3️⃣ [프로그래머스 43163 단어 변환](https://programmers.co.kr/learn/courses/30/lessons/43163)

* 접근 방법
	* 문제 보고 살짝 쫄았지만, 결국 1개 문자만 다른 것들을 거쳐서 얼마나 빨리 단어 변환할 수 있는 것인지 묻는 것이기 때문에 BFS로 풀 수 있었음
  * 생각보다 더 빨리 풀었음..

* 풀이
  * (1) 만약 target이 words에 없다면 아예 단어 변환 자체가 불가한 것이므로 끝냄
  * (2) 덱에 begin과 0(단어 변환 횟수)를 집어넣고 answer는 최대값으로 초기화함. 여러 번 방문하면 안 되기 때문에 visited도 관리
  * (3) 큐에 뭔가 있는 동안, 큐에 제일 먼저 들어간 것을 뽑아 target인지 확인한 후 target이라면 바로 return
  * (4) 문자가 하나만 달라야 변환이 가능하기 때문에 큐에서 뽑은 단어와 words의 단어들을 묶어서 알파벳을 대조해봄. 딱 1회여야 하기 때문에 1회가 넘어가면 그냥 패스
  * (5) 단어 변환이 가능하고 아직 방문하지 않은 단어라면 단어 방문 체크를 하고, cnt를 1 올려 큐에 집어넣음
  * (6) 큐가 다 빌 때까지 반복
  
---
* 정답 코드
```python
from collections import deque, defaultdict
def solution(begin, target, words):
    if target not in words:
        return 0
    
    qu = deque([(begin, 0)])
    answer = 1e9
    visited = defaultdict(int)
    
    while qu:
        s, cnt = qu.popleft()
        if s == target:
            return min(answer, cnt)
        for word in words:
            num = 0
            for c, w in zip(s, word):
                if c != w:
                    num += 1
                if num > 1:
                    break
            else:
                if not num:
                    continue
                if visited[word]:
                    continue
                visited[word] = 1
                qu.append((word, cnt+1))
    
    return answer
```
- 시간복잡도 : O(N^2)
- 공간복잡도 : O(N)
- 문제 유형 : BFS, 문자열