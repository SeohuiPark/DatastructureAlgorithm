temp_list = [1, 2, 3, 9, 10, 12]

import heapq

heapq.heapify(temp_list)
print(len(temp_list))
# a = heapq.heappushpop(temp_list,5)
# print(a)
#
#

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)

    while scoville[0]<K:
        if len(scoville)>=2:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        elif len(scoville)==1 :
            return -1
        else:
            return -1
        cnt +=1
        
    return cnt

