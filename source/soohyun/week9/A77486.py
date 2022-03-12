# 프로그래머스 77486 다단계 칫솔 판매
# https://programmers.co.kr/learn/courses/30/lessons/77486

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