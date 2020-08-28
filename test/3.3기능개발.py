import math
from collections import deque

def solution(progresses, speeds):

    # 1. make run time list
    runtime_list = deque([])
    for one_progress, one_speed in zip(progresses,speeds):
        run_time = math.ceil((100 - int(one_progress)) // int(one_speed)) # 2.3 일 -> 3일 되도록 올림
        runtime_list.append(run_time)

    # 2. check time list
    day = 1
    result_list = []
    while runtime_list: # 하루씩 증가하며 run time list 확인
        today_output = 0
        if runtime_list[0] == day: # 맨앞의 시간이 오늘과 같으면,
            while len(runtime_list) > 0 and runtime_list[0] <= day: # 오늘 시간 보다 큰 값이 나오기 전까지 다 빼줌
                runtime_list.popleft()
                today_output += 1

            result_list.append(today_output)
        day+=1

    return result_list

