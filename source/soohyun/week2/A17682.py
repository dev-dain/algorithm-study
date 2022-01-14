# 프로그래머스 17682 다트게임
# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    score = []
    bonus = {'S': 1, 'D': 2, 'T': 3}
    num = ''
    
    for d in dartResult:
        if d.isdigit():
            num += d
        elif d in 'SDT':
            score.append(int(num))
            num = ''
            score[-1] **= bonus[d]
        elif d == '*':
            if len(score) == 1:
                score[-1] *= 2
            else:
                score[-1] *= 2
                score[-2] *= 2
        elif d == '#':
            score[-1] = -score[-1]   
    
    return sum(score)