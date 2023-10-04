N, M, K = map(int, input().split())
data = list(map(int, input().split()))
sum = 0
#입력받은 data 배열을 정렬함수 활용하여 정렬
data.sort()
#큰 수와 작은 수만 활용하므로, 각각 변수에 저장
first = data[N - 1]
second = data[N - 2]

while True:
    #K번동안 반복문 수행
    for i in range(K):
        sum += first
        M -= 1

    if M == 0:
        break

    sum += second
    M -= 1

print(sum)