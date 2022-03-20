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
