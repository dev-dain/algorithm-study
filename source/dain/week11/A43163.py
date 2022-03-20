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
