import pymysql
config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

try :
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    '''
    sql = """create table chemistry_table(
           시군명 varchar(20),
           연번 varchar(20), 
           사업장명 varchar(40), 
           소재지도로명주소 varchar(50), 
           소재지지번주소 varchar(50), 
           취급사고대비물질명 varchar(30), 
           연간취급량하한선 int, 
           연간취급량상한선 int,
           주민대피시설명칭 varchar(30), 
           주민대피시설주소 varchar(50),
           사업장과주민대피시설간이격거리 float,
           위도 float,
           경도 float
           )"""
    cursor.execute(sql)
    print('table 작성 완료!!')
    '''

    file = open("../my_data/chemistry.txt", encoding='utf-8')
    line = file.readline()

    while line:
        row = line.split('\t')
        a1 = row[0]; a2 = str(row[1]); a3 = row[2]; a4 = row[3]; a5 = row[4]
        a6 = row[5]; a7 = row[6]; a8 = row[7]; a9 = row[8]; a10 = row[9]
        a11 = row[10]; a12 = row[11]; a13 = row[12]

        sql = f"""insert into chemistry_table values(
        '{a1}', '{a2}', '{a3}', '{a4}', '{a5}', '{a6}',
        {a7}, {a8}, '{a9}', '{a10}', {a11}, {a12}, {a13})"""
        cursor.execute(sql)
        conn.commit()
        line = file.readline()  # 2~n번째
    file.close()
    print('2. 레코드 추가 성공~~~')


except Exception as e :
    print("예외 발생 : ", e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
