#3

### 내림 차순 인덱스로 풀기
def solution(citations):
    sort_cit = sorted(citations, reverse=True)
    for idx in range(len(sort_cit)):
        print(idx + 1, sort_cit[idx])
        if idx + 1 > sort_cit[idx]:
            return idx
    return len(sort_cit)



#### 오름 차순 인덱스로 풀기
def solution2(citations):
    ## [0,1,3,5,6]
    sort_cit = sorted(citations)
    for idx in range(len(sort_cit)):
        print(sort_cit[idx], idx)
        if sort_cit[idx] >= (len(sort_cit) - idx):
            return (len(sort_cit) - idx)


a = [10,50,100]
# a = [3, 0, 6, 1, 5]
print(solution2(a))