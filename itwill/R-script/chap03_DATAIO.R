# chap03_DATAIO

# 1. DATA 불러오기(키보드 입력, 파일 가져오기)

# 1) 키보드 입력
x<- scan()
x
sum(x)
mean(x)

# 문자 입력
string <- scan(what=character())
string

# 2) 파일 읽기
setwd("C:/ITWILL/2_Rwork/Part-I")

# (1) read.table() : 칼럼 구분(공백, 특수문자)

# 제목 없음, 공백 구분
student <- read.table("student.txt")
student
# 기본 제목 : V1   V2  V3 V4

# 제목 있는 경우, 칼럼 구분 : 특수문자
student2 <- read.table("student2.txt", header=TRUE,sep=";" )
student2

# 결측치 처리하기
student3 <- read.table("student3.txt", header=TRUE, na.strings="-")
student3
student3$키
mean(student3$키, na.rm=T)

str(student3)
class(student3)


# (2) read.csv()
student4 <- read.csv("student4.txt", na.strings = "-") # header=T, sep=","
student4

# 탐색기 이용 : 파일 선택
excel <- read.csv(file.choose())
excel

# (3) read.xlsx() : xls/xlsx 파일 읽기 / 별도 패키지 설치 필요
install.packages("xlsx")
library(rJava)
library(xlsx)


kospi <- read.xlsx("sam_kospi.xlsx", sheetIndex = 1)
kospi

# 한글이 포함된 xlsx 파일 읽기
st_excel <- read.xlsx("studentexcel.xlsx", sheetIndex = 1, encoding = 'UTF-8')
st_excel

# 3) 인터넷 파일 읽기
# 데이터 셋 제공 사이트 
# http://www.public.iastate.edu/~hofmann/data_in_r_sortable.html - Datasets in R packages
# https://vincentarelbundock.github.io/Rdatasets/datasets.html
# https://r-dir.com/reference/datasets.html - Dataset site
# http://www.rdatamining.com/resources/data

titanic <- read.csv("https://vincentarelbundock.github.io/Rdatasets/csv/COUNT/titanic.csv")
str(titanic)
dim(titanic)
head(titanic)

# 생존여부
table(titanic$survived)
# no yes 
# 817 499 

# 성별구분
table(titanic$sex)
# man women 
# 869   447

# class 구분
table(titanic$class)
# 1st class 2nd class 3rd class 
# 325       285       706 


# 성별 vs 생존여부 : 교차분할표
table(titanic$survived, titanic$sex)
# man women
# no  694   123
# yes 175   324

tab <- table(titanic$survived, titanic$sex)
barplot(tab, col=rainbow(2))

# 행 제한 풀기 : options(max.print = 999999999) 
titanic
getOption("max.print") # 1000

options(max.print = 999999999)
titanic

# 2. 데이터 저장(출력)하기

# 1) 화면 출력
x = 20
y = 30
z = x+y

cat('z =', z) # 문자 출력 가능
print(z) # 함수내에서 출력 / 수식 가능
z

# 2) 파일 저장(출력)
# read.table -> write.table : 구분자(공백, 특수문자)
# read.csv -> write.csv : 구분자(콤마)
# read.xlsx -> write.xlsx : 엑셀(패키지 필요)

# (1) write.table() : 공백
setwd("C:/ITWILL/2_Rwork/output")

write.table(titanic, "titanic.txt", row.names = F)
write.table(titanic, "titanic2.txt", quote= F, row.names = F)

# (2) write.csv() : 콤마
head(titanic)
titanic_df <- titanic[-1]
titanic_df
str(titanic_df)

write.csv(titanic_df, "titanic_df.csv", row.names=F, quote=F)

# (3) write.xlsx : 엑셀파일

search()
write.xlsx(titanic,"titanic.xlsx", sheetName = "titanic", row.names = F)


