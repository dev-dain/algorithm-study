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
