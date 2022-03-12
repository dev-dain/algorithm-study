# 프로그래머스 67257 수식 최대화
# https://programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations
import copy

def cal(op, exp):
    # 연산자 우선순위에 따른 식의 결과값 구하기
    for o in op:
        stack = []
        while exp:
            e = exp.pop(0)
            if e == o: # 현재 우선순위 연산자와 같다면 식을 계산
                stack.append(str(eval(stack.pop() + o + exp.pop(0)))) # 좌측 숫자 + 연산자 + 우측 숫자
            else:
                stack.append(e)
        exp = stack # 다음 연산자로 넘어가기 위해 stack에 남은 것들을 exp에 저장
    
    return abs(int(exp[0]))
    
def solution(expression):
    answer = 0
    op = ['*', '+', '-']
    ops = list(permutations(op, 3)) # 가능한 연산자 우선순위 조합
    exp = []
    num = ''
    
    # 숫자와 연산자 분리하기
    for e in expression:
        if e.isdigit():
            num += e
        else:
            exp.append(num)
            exp.append(e)
            num = ''
    exp.append(num) # 마지막 숫자까지 추가
    
    for op in ops:
        result = cal(op, copy.deepcopy(exp))
        answer = max(answer, result)
            
    return answer