N, M = map(int, input().split())

result = 0
count = 0

for i in range(N):
    data = list(map(int, input().split()))
    count += 1
    if count > M:
        break

    min_value = min(data)

    result = max(result, min_value)

print(result)
