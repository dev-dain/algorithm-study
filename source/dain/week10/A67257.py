def cal(operator, n, exp):
    if n == 2:
        return str(eval(exp))
    res = eval(operator[n].join([cal(operator, n+1, e) for e in exp.split(operator[n])]))
    return str(res)

def solution(expression) :
    answer = 0
    operators = [
        ['+', '-', '*'],
        ['+', '*', '-'],
        ['*', '-', '+'],
        ['*', '+', '-'],
        ['-', '*', '+'],
        ['-', '+', '*']
    ]
    for op in operators :
        res = int(cal(op, 0, expression))
        answer = max(answer, abs(res))
        
    return answer