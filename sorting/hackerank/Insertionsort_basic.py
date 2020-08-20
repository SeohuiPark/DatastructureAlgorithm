

a = [5, 2, 4, 6, 1, 3]
def insertion_sort(num_list):

    for index in range(1, len(num_list)):
        print(num_list)
        ## index 0 보다 크고, a[7]< a[6] 보다 크고(즉 정렬 안된상태) ## 정렬이 된 상태면 해당 인덱스 넘어가
        while 0 < index and num_list[index] < num_list[index - 1]:
            print(index)
            num_list[index], num_list[index - 1] = num_list[index - 1], num_list[index]
            index -= 1
    return num_list
insertion_sort(a)






a = [5, 2, 4, 6, 1, 3]
def insertion_sort(num_list):

    for index in range(1, len(num_list)):
        print(num_list)
        ## index 0 보다 크고, a[7]< a[6] 보다 크고(즉 정렬 안된상태) ## 정렬이 된 상태면 해당 인덱스 넘어가
        while 0 < index and num_list[index] < num_list[index - 1]:
            print(index)
            num_list[index], num_list[index - 1] = num_list[index - 1], num_list[index]
            index -= 1
    return num_list
insertion_sort(a)

