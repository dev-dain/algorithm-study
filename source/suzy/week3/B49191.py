from collections import defaultdict
def solution(n, results):
    answer = 0
    win = defaultdict(set)
    lose = defaultdict(set)
    
    for i,j in results:
        win[j].add(i) # 이긴사람 : 이긴사람한테 진사람
        lose[i].add(j) # 진사람 : 진사람을 이긴사람
    
    print(win)
    # 1번부터 N번까지 선수
    for i in range(1, n+1):
        # i한테 진 애들은 i를 이긴 애들한테도 짐
        for w in win[i]:
            lose[w].update(lose[i])
        # i를 이긴 애들은 i한테 진 애들한테도 이김
        for l in lose[i]:
            win[l].update(win[i])
        
    # i한테 이기고 진애들을 합쳐서 n-1 이면 순위가 정해진것
    for i in range(1,n+1):
        if len(win[i])+len(lose[i]) == n-1:
            answer += 1
    
    return answer