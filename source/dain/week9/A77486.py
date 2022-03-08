def solution(enroll, referral, seller, amount):
    people = {}
    atomy = {}
    for i in range(len(enroll)):
        people[enroll[i]] = i
        if referral[i] == '-':
            atomy[enroll[i]] = 'root'
            continue
        atomy[enroll[i]] = referral[i]
    
    money = [0] * (len(enroll))
    for i in range(len(seller)):
        num = people[seller[i]] # 셀러의 번호
        cash = amount[i] * 100    # 셀러가 번 돈
        refer = atomy[seller[i]]    # 셀러를 조직에 넣은 사람
        money[num] += cash   # 일단 판 돈을 받는다
        while refer != 'root' and cash > 0:
            give = cash // 10   # 추천인에게 주는 돈
            take = cash - give  # 자기가 갖는 돈
            cash = give # 추천인에게 남는 돈
            money[num] -= give  # 헌납하는 돈을 뺀다
            num = people[refer]
            money[num] += give
            refer = atomy[refer]
        if cash > 0:
            money[num] -= cash // 10
    return money