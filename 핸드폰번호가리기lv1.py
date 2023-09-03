def solution(phone_number):
    answer = list(phone_number)
    for i in range(len(answer[0:-4])):
        answer[i] = "*"
    return answer

print(*solution("0238722243"))
