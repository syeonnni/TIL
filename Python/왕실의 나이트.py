#왕실의 나이트
input_data = input()
#열, 행 변수 선언
row = int(input_data[1])
column = int(ord(input_data[0]) - int(ord('a'))+1)
#경우의 수 계산하는 변수 count 선언
count = 0

#나이트가 이동할 수 있는 8가지 단계 정의
steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

for step in steps:
    next_row = row+step[0]
    next_column = column+step[1]

    #8*8 좌표 안에 있는지 확인
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        count += 1

print(count)