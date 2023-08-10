n = int(input())
h = list(map(int, input().split()))
cnt = 0
if sum(h)%3 == 0:
    for i in h:
        cnt += i//2
    if cnt >= sum(h)//3: # 1과2 물뿌리개를 같이 사용했을 때도 2를 사용하기 때문에 클 때도 가능
        print('YES')
    else:
        print('NO')
else:
    print('NO')