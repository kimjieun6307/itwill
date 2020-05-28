#################################
## <제9장-1 연습문제>
################################# 

# 01. 다음과 같은 단계를 통해서 테이블을 호출하고, SQL문을 이용하여 레코드를 조회하시오.
# (DBMS : Oracle 사용)

library(DBI)
Sys.setenv(JAVA_HOME='C:\\Program Files\\Java\\jre1.8.0_151')
library(rJava)
library(RJDBC)

drv<-JDBC("oracle.jdbc.driver.OracleDriver", 
          "C:/oraclexe/app/oracle/product/11.2.0/server/jdbc/lib/ojdbc6.jar")


conn<-dbConnect(drv, "jdbc:oracle:thin:@//127.0.0.1:1521/xe","scott","tiger")


# [단계 1] 사원테이블(EMP)을 검색하여 결과를 EMP_DF로 변수로 불러오기
EMP_DF <- dbGetQuery(conn, "select * from emp")
EMP_DF

# [단계 2] EMP_DF 변수를 대상으로 부서별 급여의 합계를 막대차트로 시각화
str(EMP_DF)

library(lattice)
library(dplyr)

EMP_DEPTNO <- EMP_DF%>%group_by(DEPTNO)%>%summarise(sal_sum=sum(SAL))
EMP_DEPTNO 

# (1)
barplot(EMP_DEPTNO, col=rainbow(3)) # Error - 'height'는 반드시 벡터 또는 행렬이어야 합니다
barplot(EMP_DEPTNO$sal_sum, col=rainbow(3))
# &&& 4

# (2)
EMP1<- as.data.frame(EMP_DEPTNO)
barchart(sal_sum~DEPTNO, data=EMP1, horiz = F)
# &&& 5
#################################################
qplot(EMP_DEPTNO)



# [단계 3] 막대차트를 대상으로 X축의 축눈금을 부서명으로 표시하기
str(dbGetQuery(conn, "select * from dept"))
str(dbGetQuery(conn, "select * from emp"))

query <- "select d.deptno, d.dname, e.sal
from dept d, emp e
where d.deptno = e.deptno"

EMP2 <- dbGetQuery(conn, query)
EMP2_EX <- EMP2%>%group_by(DNAME)%>%summarise(SAL_SUM=sum(SAL))
EMP2_DF <- as.data.frame(EMP2_EX)

barchart(SAL_SUM ~ DNAME, data=EMP2_DF, horiz = F)
# &&& 6




#########################################################
# 강사님
# [단계 1] 사원테이블(EMP)을 검색하여 결과를 EMP_DF로 변수로 불러오기
EMP_DF <- dbGetQuery(conn, "select * from EMP")
# [단계 2] EMP_DF 변수를 대상으로 부서별 급여의 합계를 막대차트로 시각화(col)
# 부서별 그룹 생성 
emp_g <- group_by(EMP_DF, DEPTNO) # 부서번호 기준 그룹 
# 부서별 급여 합계 
emp_sal_tot <- summarise(emp_g, dept_tot = sum(SAL))

barplot(emp_sal_tot$dept_tot, col = rainbow(3))

# [단계 3] 막대차트를 대상으로 X축의 축눈금을 부서명으로 표시하기
# 부서 테이블 조회 
dept <- dbGetQuery(conn, "select * from dept")

# 부서명 추출 
dname <- dept$DNAME[1:3]

# x축 눈금(names.arg) : 부서명 표시 
barplot(emp_sal_tot$dept_tot, 
        col = rainbow(3),
        names.arg = dname)
# &&& 7





