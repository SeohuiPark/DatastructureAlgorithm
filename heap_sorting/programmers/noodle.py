
import heapq

# def solution(stock, dates, supplies, k):
#     start = 0
#     cnt = 0
#     h = []
#     while stock < k: #재고개수 전체k 보다 작을때 항상 반복문 돌고 ! 넘으면 stop
#         for i in range(start, len(dates)):
#             if dates[i] <= stock: # 재고 남아있는 상황
#                 heapq.heappush(h,(-supplies[i],supplies[i])) # h리스트에 힙으로 저장해두
#                 start = i+1 #해외수입가능날보기
#             else:
#                 break
#         stock+= heapq.heappop(h)[1]
#         cnt+=1
#     return cnt


import heapq
from collections import deque
def solution(stock, dates, supplies, k):
    cnt = 0
    h = []
    dates = deque(dates)
    supplies = deque(supplies)
    for now in range(1, k):
        stock-=1
        if len(dates) == 0 or stock > k:
            break
        else:
            if now == dates[0]:
                heapq.heappush(h, (-supplies[0], supplies[0]))
                dates.popleft()
                supplies.popleft()
                if stock >= now:
                    pass
                else:
                    stock += heapq.heappop(h)[1]
                    cnt += 1
            else:
                pass
    return cnt

dates  = [4,10,15]
supplies = [20,5,10]
k = 30
stock = 4
a = solution(stock, dates, supplies, k)
print("A",a)


