
# 11286 절대값 힙
import heapq

heap_list = []
heapq.heapify(heap_list)

for i in int(input()):
    num = int(input())
    if num == 0:
        if len(heap_list) == 0:
            print(0)
        else:
            print(heapq.heappop(heap_list)[1])
    else:
        heapq.heappush(heap_list, (abs(num), num))


### 최대값 힙
for i in int(input()):
    num = int(input())
    if num == 0:
        if len(heap_list) == 0:
            print(0)
        else:
            print(heapq.heappop(heap_list)[1])
    else:
        heapq.heappush(heap_list, (-num, num))


### 최대값 힙
for i in int(input()):
    num = int(input())
    if num == 0:
        if len(heap_list) == 0:
            print(0)
        else:
            print(heapq.heappop(heap_list))
    else:
        heapq.heappush(heap_list, num)

