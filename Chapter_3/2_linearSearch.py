'''
    --- 선형 검색 ---

    배열에서 검색하는 방법 중 가장 기본적인 알고리즘이다.
    선형은 직선 모양으로 늘어선 배열에서 검색하는 경우 앞에서 순서대로 스캔하는 알고리즘이다(순차검색).

'''

a = [1,2,3,4]
i = 0
key = 4
while True : 
    print(f'{i}')
    if i == len(a) :  
        print(f'검색 실패!')
    if a[i] == key: 
        print(f'검색 성공')
    i += 1