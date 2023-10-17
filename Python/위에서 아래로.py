#위에서 아래로
#정렬 문제

N = int(input())
array = []
for i in range(N):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')
