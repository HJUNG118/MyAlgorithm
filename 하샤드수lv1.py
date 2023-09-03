def solution(x):
    answer = True
    x = str(x)
    value = 0
    for i in range(len(x)):
        value += int(x[i])
    if int(x)%value != 0:
        answer = False
    return answer
print(solution(11))