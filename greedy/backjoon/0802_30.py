#
# '''
# 3 --> sum must be 3
# '''
# import sys
# n = list(sys.stdin.readline().rstrip())
# n.sort(reverse=True)
# if n[-1] != '0' or sum(map(int, n)) % 3 != 0:
#     print(-1)
# else:
#     print(''.join(n))

#
# h,w = map(int,sys.stdin.readline().split())
# print(h,w)


import sys
n = list(sys.stdin.readline().rstrip())
n.sort(reverse=True)
n = list(map(int,n))
if n[-1] !=0 :
    result = -1
else:
    div_list = [num%4 for num in n]
    print(div_list)
    if div_list.count(0) %3:
        result = n
    else:
        result = -1

print(result)