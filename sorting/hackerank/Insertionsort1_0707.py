


# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    sorted_array, right_array = [],[]
    key = arr[-1]
    for key_index in reversed(range(n)):
        if len(arr) == 1:
            print(" ".join(map(str,[key] + right_array)))
            break
        else:
            if key < arr[-2] :
                right_array.insert(0,arr[-2])
                arr.pop()
                print(" ".join(map(str,arr+right_array)))
            elif key >= arr[-2] :
                arr.pop()
                print(" ".join(map(str,arr+[key]+right_array)))
                break



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)



#
# #
# #### 참고해서 다시 짜기
# a = [5, 2, 4, 6, 1, 3]
# def insertion_sort2(num_list):
#
#     for index in range(1, len(num_list)):
#         print(num_list)
#         ## index 0 보다 크고, a[7]< a[6] 보다 크고(즉 정렬 안된상태) ## 정렬이 된 상태면 해당 인덱스 넘어가
#         while 0 < index and num_list[index] < num_list[index - 1]:
#             print(index)
#             num_list[index], num_list[index - 1] = num_list[index - 1], num_list[index]
#             index -= 1
#     return num_list
#
#
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().rstrip().split()))
#     insertion_sort2(n, arr)


#### 참고해서 다시 짜기
def insertion_sort2(n,num_list):
    key = num_list[-1]

    for c_index in reversed(range(n-1)):
        arr = num_list[:-1] # 맨마지막 친구 빼기
        while 0 < c_index and key < arr[-1]:
            num_list[c_index], num_list[c_index + 1] = arr[c_index], arr[c_index]
            c_index-=1
            print(num_list)


    return num_list


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    insertion_sort2(n, arr)
