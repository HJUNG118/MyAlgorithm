import sys, heapq
n, m = map(int, input().split())
prices = [list(map(int, input().split())) for _ in range(m)]
sixPackage = sorted(prices, key = lambda x: x[0])
onePackage = sorted(prices, key = lambda x: x[1])
# 6개 패키지로 줄을 샀을 때와 하나를 필요한만큼 샀을 때를 나눈다.
if sixPackage[0][0] <= onePackage[0][1] * 6:
    answer = sixPackage[0][0] * (n//6) + onePackage[0][1] * (n%6)
    if sixPackage[0][0] < onePackage[0][1] * (n%6):
        answer = sixPackage[0][0] * (n//6 + 1)
else:
    answer = onePackage[0][1] * n
print(answer)

        

