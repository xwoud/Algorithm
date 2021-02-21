import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0

    answer = 0
    heap = []

    for i in works:
        heapq.heappush(heap,i*(-1))

    while(n>0):
        heapq.heappush(heap,heapq.heappop(heap)+1)
        n -= 1

    for i in heap:
        answer += (-i) ** 2

    return answer
