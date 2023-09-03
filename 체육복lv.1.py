def solution(n, lost, reserve):
    answer = 0
    reserve = set(reserve) - set(lost) # 여분을 가지고 왔지만 잃어버린 상태라면 여분이 없다고 생각해야함
    lost = set(lost) - set(reserve) # 잃어버렸는데 여분이 있으면 안잃어버린거임
    for person in reserve:
        if person-1 in lost:
            lost.remove(person-1)


    return reserve

print(solution(5, [2, 4],	[1, 3, 5]))