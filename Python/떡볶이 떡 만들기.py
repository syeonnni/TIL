#떡볶이 떡 만들기
#터무니없이 조건이 큰 수가 주어졌다면(=10억) 이진 탐색을 생각해보기

N, M = map(int, input().split())
data_list = list(map(int, input().split()))

start = 0
end = max(data_list)

result = 0
while start <= end:
    total = 0
    mid = (start+end) // 2

    for i in data_list:
        if i > mid:
            total += i - mid
            
    if total < M:
        end = mid-1
        
    else:
        result = mid
        start = mid+1

print(result)
