from collections import deque
import sys
input = sys.stdin.readline
n, l, r = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
cnt = 0
def bfs(row, col, visit):
    result = [(row, col)]
    deq = deque([(row, col)])
    visit[row][col] = True
    while deq:
        r_, c_ = deq.popleft()
        for i in range(4):
            nr = r_ + dr[i]
            nc = c_ + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visit[nr][nc]:
                if l <= abs(maps[nr][nc] - maps[r_][c_]) <= r:
                    result.append((nr, nc))
                    deq.append((nr, nc))
                    visit[nr][nc] = True
    if len(result) > 1:
        return result
    else:
        return False

def average(result):
    value = 0
    for i, j in result:
        value += maps[i][j]
    return value//len(result)

def change_value(result, value):
    for i, j in result:
        maps[i][j] = value

while True:  
  visit = [[False]*n for _ in range(n)]       
  flag = 0                
  for i in range(n):
      for j in range(n):
          if not visit[i][j]:
            result = bfs(i, j, visit)
            if result:
              flag = 1
              value = average(result)
              change_value(result, value)
  if flag == 1:
      cnt += 1
  else:
      break
print(cnt)

