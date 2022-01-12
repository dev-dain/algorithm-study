# 백준 5525

n = int(input())
m = int(input())
s = str(input())

cnt = 0
answer = 0
i = 0 
while i < m-1:
    if s[i-1] == 'I'and s[i]=='O' and s[i+1] == 'I':
        cnt += 1
        if cnt == n:
            cnt -= 1
            answer += 1
        i += 1
    else:
        cnt = 0
    i += 1            
          
print(answer)