

# 1. 내 방식대로 (풀었음 !!! 근데 개오래걸림) - 총 3번의 for

'''똑같이 countlist 만들어서 하는데 

뒤에서 부터 요소 꺼내서 아웃풋 리스트에 넣을 때, 

1) 숫자 대신 문자를 넣고 
2) 원래 arr 에서 그 (숫자,문자) 인덱스 파악해서 만약 인덱스 len(arr)//2 보다 작으면 "-" 넣기 
해당 요소의 누적 카운트 위치에 해당하는 '''


def countingSort(arr):

    # define count list
    count_list = [0] * len(arr)
    for item in arr:
        count_list[int(item[0])]+=1

    # add count_list
    a_count_list = count_list.copy()
    for i in range(len(a_count_list)-1):
        a_count_list[i+1] += a_count_list[i]

    # define output array
    output_list = ['-'] * len(arr)

    # fill output array
    idx = 0
    for num, string in reversed(arr):
        input_idx = a_count_list[int(num)]-1
        if idx <len(arr)//2: # 역으로 가니까 작은 수로
            output_list[input_idx] = string
        idx +=1
        a_count_list[int(num)]-=1
    return ' '.join(output_list)


n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(input().rstrip().split())
print(countingSort(arr))



#2 예시 답안도 나랑 비슷하게 품.

n = int(input())
ar = []
for i in range(0, n):
    data = input().strip().split(' ')
    ar.append((int(data[0]), data[1]))

c = [0] * 100
for a in ar:
    c[a[0]] += 1

c1 = [0] * 100
for x in range(1, 100):
    c1[x] = c1[x - 1] + c[x - 1]

s = ['-'] * n
for i in range(0, n):
    if i >= n / 2:
        s[c1[ar[i][0]]] = ar[i][1]
    c1[ar[i][0]] += 1

print(' '.join(s))