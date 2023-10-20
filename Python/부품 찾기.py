#부품 찾기
N = int(input())
number_list = list(map(int, input().split()))
number_list.sort()

M= int(input())
ask_list = list(map(int, input().split()))

def search_list(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if array[mid] < target:
            end = mid-1
        elif array[mid] == target:
            return mid
        else:
            start = mid+1
    return None

for i in ask_list:
    result = search_list(number_list, i, 0, N-1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ') 
