'''
문제2) goods 테이블을 이용하여 다음과 같은 형식으로 출력하시오.

    [ goods 테이블 현황 ]
1 냉장고 2 850000
2 세탁기 3 550000
3 전자레인지 2 350000
4 HDTV 2 1500000
전체 레코드 수 : 4

    [ 상품별 총금액 ]
냉장고 상품의 총금액은 1,700,000
세탁기 상품의 총금액은 1,650,000
전자레인지 상품의 총금액은 700,000
HDTV 상품의 총금액은 3,000,000
'''

import sqlite3

try :
    conn = sqlite3.connect('../data/sqlite.db')
    cursor = conn.cursor()

    '''
    code = int(input("수정할 코드 입력 : "))
    su = int(input("수정할 수량 입력 : "))
    dan = int(input("수정할 단가 입력 : "))
    sql = f"update goods set su = {su}, dan = {dan} where code = {code}"
    cursor.execute(sql)
    conn.commit()
    '''

    cursor.execute("select * from goods")
    dataset = cursor.fetchall()
    print('     [ goods 테이블 현황 ]')
    for row in dataset :
        print("%d %s %d %d"%(row))
    print('전체 레코드 수 :', len(dataset))

    print('     [ 상품별 총금액 ]')
    for row in dataset:
        print(f"{row[1]}상품의 총금액은", format(int(row[2]*row[3]), '3,d'))

except Exception as e :
    print('예외 발생 : ',e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()


'''
    print('     [ 상품별 총금액 ]')
    for row in dataset:
        print(f"{row[1]}상품의 총금액은{row[2]*row[3]}" )
        
     [ 상품별 총금액 ]
냉장고상품의 총금액은1700000.0
세탁기상품의 총금액은1650000.0
전자레인지상품의 총금액은700000.0
HDTV상품의 총금액은3000000.0
'''

