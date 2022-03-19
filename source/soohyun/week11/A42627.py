# 프로그래머스 42627 디스크 컨트롤러
# https://programmers.co.kr/learn/courses/30/lessons/42627

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