from collections import deque
m, n, k = map(int, input().split())
maps = [[0]*n for _ in range(m)]
for _ in range(k):
    l_x, l_y, r_x, r_y = map(int, input().split())
    for i in range(l_y, r_y):
        for j in range(l_x, r_x):
            maps[i][j] = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = []
def bfs(x, y):
    cnt = 1
    deq = deque([(x, y)])
    maps[x][y] = 1
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] == 0:
                maps[nx][ny] = 1
                deq.append((nx, ny))
                cnt += 1
    return cnt
for i in range(m):
    for j in range(n):
        if maps[i][j] == 0:
            cnt = bfs(i, j)
            result.append(cnt)
result.sort()
print(len(result))
print(*result)
    
            
        