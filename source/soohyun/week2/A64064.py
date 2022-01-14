# 프로그래머스 64064 불량 사용자
# https://programmers.co.kr/learn/courses/30/lessons/64064


from itertools import permutations

# 응모 아이디 목록과 제재 아이디 목록이 같은지 확인
def check(pm, banned_id):
    for p, b in zip(pm, banned_id):
        if len(p) != len(b):
            return False
        for i in range(len(p)):
            if b[i] == '*':
                continue
            if p[i] != b[i]:
                return False
    return True

def solution(user_id, banned_id):
    user_pms = list(permutations(user_id, len(banned_id))) # 응모자 아이디의 순열
    answer = set() # 당첨에 제외되는 경우
    
    for pm in user_pms:
        if check(pm, banned_id):
            pm = frozenset(pm) # set에 넣은 개별항목은 변경될 수 없으므로 immutable set인 frozenset로 변환해야 한다
            answer.add(pm)
        else:
            continue
            
    return len(answer)