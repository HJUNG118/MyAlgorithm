import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
k = int(input())
maps = [[0]*n for _ in range(n)]
for i in range(k):
    apple = list(map(int, input().split()))
    maps[apple[0]-1][apple[1]-1] = 2
m = int(input())
direction = {}
for _ in range(m):
    x, c = input().split()
    direction[int(x)] = c
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

deq = deque([(0, 0)])
x, y, d, time = 0, 0, 0, 0
while True: # 뱀의 꼬리를 큐에 넣는다고 생각하고 큐를 사용한다.
    nr = x + dr[d]
    nc = y + dc[d]
    if nr < 0 or nc < 0 or nr >= n or nc >= n or maps[nr][nc] == 1: # 벽 또는 뱀의 몸을 만나면 종료
        break
    if maps[nr][nc] != 2: # 사과가 없다면 꼬리를 없애준다.
        r_, c_ = deq.popleft()
        maps[r_][c_] = 0
    maps[nr][nc] = 1
    time += 1
    x = nr
    y = nc
    deq.append((x, y))
    for dir in direction.keys():
        if time == dir:
            if direction[dir] == 'D':
              d = (d+1)%4
            else:
              d = (d-1)%4
print(time+1) # 마지막 벽을 만나려고 할 때 멈추기 때문에 벽에 부딪히는 시간 1을 더해야 한다.

    

                
                

    
    
