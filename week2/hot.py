def solution(scoville, K):
    cnt = 0
    low_list, upper_list = [], []
    for i in scoville:
        if i < K:
            low_list.append(i)
        else:
            upper_list.append(i)
    low_list = sorted(low_list, reverse=True)

    i = 0
    while low_list:
        print(low_list)
        if len(low_list) != 1:
            if len(low_list) == 2:
                low_list = sorted(low_list, reverse=True)
            else:
                low_list[-3:] = sorted(low_list[-3:], reverse=True)
            mix_num = low_list[-1] + (low_list[-2] * 2)
            cnt += 1
            print(mix_num,low_list[-1],low_list[-2])
            low_list.pop()
            low_list.pop()
        else:
            return -1
        if mix_num >= K: upper_list.append(mix_num)
        else: low_list.append(mix_num)

    return cnt


a = [1, 1,2]
b = 3
print(solution(a, b))

