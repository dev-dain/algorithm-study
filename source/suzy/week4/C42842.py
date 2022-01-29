def solution(brown, yellow):
    # 전체 면적
    s =  brown + yellow
    
    for w in range(s, 2, -1):
        
        if s % w == 0: # 가로
            h = s//w # 세로
            
            if (w-2)*(h-2) == yellow:
                return [w,h]