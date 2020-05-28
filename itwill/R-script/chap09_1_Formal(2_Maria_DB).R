# chap09_1_Formal(2_Maria_DB)

# Maria DB 정형 데이터 처리

# 패키지 설치
# - RJDBC 패키지를 사용하기 위해서는 우선 java를 설치해야 한다.
#install.packages("rJava")
#install.packages("DBI")
#install.packages("RJDBC") # JDBC()함수 제공 

# 패키지 로딩
library(DBI)
# 최근 버전에서는 안해됨 Sys.setenv(JAVA_HOME='C:\\Program Files\\Java\\jre1.8.0_151')
library(rJava)
library(RJDBC) # rJava에 의존적이다.

################ MariaDB or MySql ###############
# 1.  JDBC 함수 이용해서 드라이브 객체 만들기
drv <- JDBC(driverClass="com.mysql.jdbc.Driver", 
            classPath="C:/ITWILL/2_Rwork/tools(R)/mysql-connector-java-5.1.46/mysql-connector-java-5.1.46/mysql-connector-java-5.1.46-bin.jar")

# driver가 완전히 로드된 후 db를 연결한다.
conn <- dbConnect(drv, "jdbc:mysql://127.0.0.1:3306/work", "scott", "tiger")

# 127.0.0.1 -- 내컴퓨터, 3306 -- mariaDB 설치시 포트번호
# work -- mairaDB 데이터베이스 , scott / tiger -- mairaDB 사용자 계정/아이디
#################################################           

query <- "show tables"
dbGetQuery(conn, query)

# 레코드 조회
dbGetQuery(conn, "select * from goods")


# DB 구조 변경
# 1. 레코드 추가
query <- "insert into goods values(5, '전화기', 4, 450000)"
dbSendUpdate(conn, query)

# 2. 레코드 수정 : 전화기 >> phone
query <- "update goods set name = 'phone' where code=5 "
dbSendUpdate(conn, query)

# 3. 레코드 삭제 : code = 5 삭제하기
query <- "delete from goods where code = 5"
dbSendUpdate(conn, query)

# R변수 저장
goods <- dbGetQuery(conn, "select * from goods")
goods
str(goods)

price <- goods$su*goods$dan

goods$price <- price
goods

# table >> 처리 >> file save
write.csv(goods, "goods.csv", quote = F, row.names = F)

# table >> 처리 >> table save
# (참고) table 생성
query <- "create table goods_manager1(
code int, name varchar(50), su int, dan int, price int)"
dbSendUpdate(conn, query)
dbGetQuery(conn, "show tables")
dbGetQuery(conn, "select * from goods_manager1")

dbSendUpdate(conn, "drop table goods_manager1")

# [단계] R의 object >> table save

dbWriteTable(conn, name ="goods_manager" , value = goods)
dbGetQuery(conn, "show tables")
dbGetQuery(conn, "select * from goods_manager")
dbDisconnect(conn)






