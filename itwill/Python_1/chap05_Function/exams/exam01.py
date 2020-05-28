'''
문1) Start counter 문제  

height : 3 <- 키보드 입력 
*
**
***
start 개수 : 6 
'''

# 함수 정의
def StarCount(height):
    s_cnt = 0 # 별 개수 카운트
    cnt =0
    for i in range(height):
        cnt +=1
        s_cnt += cnt
        print('*' * (i+1))
    return s_cnt

# 키보드 입력 
height = int(input('height : ')) # 층 수 입력 

# 함수 호출 및 start 개수 출력
print('start 개수 : %d'%StarCount(height))

#-----------------------------------------
def StarCount(height):
    s_cnt = 0  # 별 개수 카운트
    for i in range(height):
        s_cnt += (i+1)
        print('*' * (i + 1))
    return s_cnt
