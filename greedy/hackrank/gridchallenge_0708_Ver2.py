#!/bin/python3

import math
import os
import random
import re
import sys
import string

import time
start = time.time()


### 내가 푼거지만 공간복잡도 측면에서 별루인듯.


# Complete the gridChallenge function below.
def gridChallenge(grid):
    # 1. define map fuction
    def map(f, it):
        result = []
        for x in it:
            result.append(f(x))
        return result

    # 2. get sorted 2d list
    sorted_grid = map(sorted, grid)

    # 3. Transpose 2d list
    trans_grid = list(map(list, zip(*sorted_grid)))
    # print(trans_grid)

    # 3. check column sorting by using sum of ord
    final_result = True
    for idx in range(len(trans_grid)):
        if trans_grid[idx] == sorted(trans_grid[idx]):
            pass
        else:
            return ("NO")
    return ("YES")
    # print(alorder_sum)
    # if (idx == 0) or init_sum <= alorder_sum :
    #     init_sum = alorder_sum
    # elif init_sum > alorder_sum :# sum is lower than before sum


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())
        grid = []
        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

    print(result)
    print("time :", time.time() - start)


    #     fptr.write(result + '\n')
    #
    # fptr.close()