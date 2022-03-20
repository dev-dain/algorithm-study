def bfs(begin, target, words, visited):
    count = 0
    stack = [(begin, 0)]
    while stack:
        cur, depth = stack.pop()
        if cur == target:
            return depth
        
        for i in range(len(words)):
            if visited[i] == True:
                continue
            cnt = 0
            for a,b in zip(cur, words[i]): # 서로 다른 부분 check
                if a!=b:
                    cnt += 1
            if cnt == 1:
                visited[i] = True
                stack.append((words[i], depth+1))
                
            

def solution(begin, target, words):
    answer = 0
    # words 존재하지 않는 경우
    if target not in words:
        return 0

    visited = [False]*(len(words))

    answer = bfs(begin, target, words, visited)

    return answer
