def solution(enroll, referral, seller, amount):
    
    brush = 100
    
    salary = dict()
    parti = dict() # enroll :  referral
    for i in range(len(enroll)):
        salary[enroll[i]] = 0
        parti[enroll[i]] = referral[i]
    
    # 이익의 10% 배분 / 나머지 나에게 배당
    for i in range(len(seller)):
        s = seller[i]
        price = brush * amount[i]
        
        while s != '-':
            salary[s] += price - (price // 10) # 나머지
            price = price // 10 # 이익
            if price == 0:
                break
            s = parti[s]
    
    return [salary[i] for i in enroll]