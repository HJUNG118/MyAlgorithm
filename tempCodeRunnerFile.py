while True: # 자 평소처럼 큐에서 바로 꺼내면 안돼 왜냐하면 꼬리가 큐에 들어가기 때문에 꼬리는 사과를 못만났을 때 나와서 0으로 바뀌어야돼
    nr = x + dr[d]
    nc = y + dc[d]
    if nr < 0 and nc < 0 and nr >= n and nc >= n and maps[nr][nc] == 1: # 벽을 만나면 종료
        break
    if  maps[nr][nc] == 2:
        maps[nr][nc] = 1
    elif maps[nr][nc] == 0:
        maps[nr][nc] = 1
        r_, c_ = deq.popleft(r_, c_)
        maps[r_][c_] = 0
    time += 1
      
    for dir in direction:
        if time == dir[0]:
            if dir[1] == 'D':
              d = (d+1)%4
            else:
              d = (d+3)%4
    deq.append((nr, nc))
print(time)

    

                
                

    
    
