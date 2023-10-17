#성적이 낮은 순서로 학생 출력하기
#정렬 문제

N = int(input())

array = []
for i in range(N):
    data = input().split()
    #이름은 문자열 그대로, 점수는 int형으로 추가
    array.append((data[0], int(data[1])))

#key를 이용하여 점수를 기준으로 정렬 
array = sorted(array, key = lambda student: student[1])

for student in array:
    print(student[0], end =' ')
