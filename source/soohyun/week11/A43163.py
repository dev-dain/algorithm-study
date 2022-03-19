# 프로그래머스 43163 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163

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