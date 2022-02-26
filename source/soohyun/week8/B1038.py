# 백준 1038 감소하는 수
# https://www.acmicpc.net/problem/1038

n = int(input())

def solve(n):
    cnt = 0 # 몇번째 수인지
    num = 1 # 현재 수

    while True:
        str_num = str(num)
        flag = True # 감소하는 수인지 체크

        if len(str_num) == 1:  # 길이가 1이면 무조건 감수하는 수
            pass
        else:
            for i in range(1, len(str_num)):
                if int(str_num[i-1]) > int(str_num[i]):
                    continue
                else: # 감소하는 수가 아닌 경우 감소하는 수로 만들어준다
                    start = str_num[:i - 1]
                    mid = str(int(str_num[i - 1]) + 1)
                    end = '0' + str_num[i + 1:]
                    num = int(start + mid + end)
                    flag = False
                    break
        if flag:
            cnt += 1
            if cnt == n:  # n번째 감소하는 수라면 리턴
                return num
            num += 1

if n > 1022: # n번째 감소하는 수가 없는 경우
    print(-1)
elif n == 0: # 0번째 숫자인 경우
    print(0)
else:
    print(solve(n))