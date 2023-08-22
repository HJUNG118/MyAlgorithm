import heapq
def solution(jobs):
    heap = []
    answer, now, i = 0, 0, 0
    start = -1
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, (job[1], job[0]))
        if heap:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now-cur[1]
            i += 1
        else:
            now += 1
    return answer//i
