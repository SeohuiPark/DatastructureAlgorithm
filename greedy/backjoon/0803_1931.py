

#
#
# import sys
# N = int(input())
# info_list = []
# for idx in range(N):
#     st,end = map(int, sys.stdin.readline().split())
#     dur = end - st
#     info_list.append((st,end,dur))
#
# info_list = sorted(info_list, key = lambda x:(x[0],x[2],x[1]))
#
# chk_dict = {}
# st_list = []
# end_list = []
# min_end = 12129831209873109
# idx =0
# for info in info_list:
#     st, end, dur = info[0],info[1],info[2]
#     if min_end <= st:
#         print("APPEND",info)
#         for key, values in chk_dict.items():
#             if values[len(values)-1][1] <= st:
#                 values.append(info)
#             else:pass
#     else:
#         print("KEY", info)
#         chk_dict[idx] = [info]
#         st_list.append(st)
#         end_list.append(end)
#         if min_end > end:
#             min_end = end
#         idx+=1
#
#
#
# print(chk_dict)
# print(st_list)
# print(end_list)
#
# print("ANWSER", max([len(val) for val in chk_dict.values()]))



# ffinal_list = sorted(final_list, key=lambda x: (-x[0], -x[1], x[2]))
#
# for info in info_list:
'''
시작 숫자 기준으로 하나씨 ㄱ리스트 만들어

((0, 6, 6), (6, 10, 4) (12, 14, 2)]
(1, 4, 3), (5, 7, 2), (8, 11, 3),  (12, 14, 2)]
(2, 13, 11), 
(3, 5, 2), (5, 7, 2)or (6, 10, 4)   (12, 14, 2)]
(3, 8, 5), (8, 11, 3) (12, 14, 2)]


만약 끝수랑 같거나 큰게 나오면 거기에 쌓아줘 
근데 같은 시작시점인데 숫자가 더 길면 버려? 

 (5, 9, 4), 
'''

import sys

N = int(input())
info_list = []
for idx in range(N):
    st,end = map(int, sys.stdin.readline().split())
    dur = end - st
    info_list.append((st,end,dur))

info_list = sorted(info_list, key = lambda x:(x[0],x[2],x[1]))
chk_dict = {}
min_end = 12129831209873109
idx =0

for info in info_list:
    st, end, dur = info[0],info[1],info[2]
    if min_end <= st:
        for key, values in chk_dict.items():
            if values[len(values)-1][1] <= st:
                values.append(info)
            else:pass
    else:
        chk_dict[idx] = [info]
        if min_end > end:
            min_end = end
        idx+=1

print(info_list)

print(max([len(val) for val in chk_dict.values()]))


for key, value in chk_dict.items():
    print(key,':',value)
### 가장 먼저 끝나는 걸 찾는다는 컨셉으로 다시 풀기


