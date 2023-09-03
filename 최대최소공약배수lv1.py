def max_num(n, m):
    if m%n == 0:
        return n
    else:
        answer = max_num(m%n, n)
    return answer

def solution(n, m):
    answer = [0, 0]
    if n <= m:
        answer[0] = max_num(n, m)
    else:
        answer[0] = max_num(m, n)
    answer[1] = (n*m)//answer[0]
    return answer