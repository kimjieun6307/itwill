# chap02_DataStructure

# 자료구조의 유형(5)

# 1. vector 자료구조
# - 동일한 자료형을 갖는 1차원 배열구조
# - 생성함수 : c(), seq(), rep()

# (1) c()
x<-c(1,3,5,7)
y<-c(3,5)
length(x) # 4의 원소(길이)를 가지고 있는

# 집합관련 함수
union(x, y) # 합집합(x + Y) : [1] 1 3 5 7
setdiff(x, y) # 차집함(x - y) : [1] 1 7  
intersect(x,y) # 교집합 : [1] 3 5

# 벡터변수 유형
num <- 1:5 # c(1,2,3,4,5)
num
num<- c(-10:5)
num
num<- c(1,2,3,"4")
num # [1] "1" "2" "3" "4" : 동일할 자료형을 갖기 때문에 모두 문자형

# 벡터 원소 이름 지정
names <- c("hong", "lee", "kang")
names
age <- c(35, 45, 55)
age
names(age) <- names
age
mode(age)

str(age) # 객체의 자료구조 제공
# Named num [1:3] 35 45 55 >> 데이터(data)
# - attr(*, "names")= chr [1:3] "hong" "lee" "kang" >> 원소이름 (names)

# 2) seq()
?seq

num<- seq(1, 10, by=2)
num # [1] 1 3 5 7 9

num2<-seq(10, 1, by=-2)
num2

# 3) rep()
help(rep) # rep(x, ...)
rep(1:3, times=3) # [1] 1 2 3 1 2 3 1 2 3
rep(1:3, each=3) # [1] 1 1 1 2 2 2 3 3 3


# 색인(index) : 저장 위치
# 형식) object[n]
a<- 1:50
a # a객체(변수)의 전체 원소 출력
a[10] #>> 10 : 10번째 특정 원소 한 개 출력
a[10:20] #>> 10~20
a[10:20, 30:35] #>> Error in a[10:20, 30:35] : incorrect number of dimensions
# - [행, 열] : 1차원 데이터인 vecbtor 사용 할수 없음 >> c함수 이용하여 출력하면 됨.
a[c(10:20, 30:35)] # >> 10 11 12 13 14 15 16 17 18 19 20 30 31 32 33 34 35


# 함수 이용
length(a) #>> 50 ※길이=원소 개수
a[10:length(a)-5] #>> 5~45
a[10:(length(a)-5)]  #>> 10~45
a[seq(2,length(a), by=2)] #-- 함수를 이용하여 인텍스 출력

# 특정 원소 제외(-)
a[-c(15, 25, 30:35)]

# boolean : 조건식을 위한 인텍스
a[a>=10 & a<=30] # &(and)
a[a>=10 | a<=30] # |(or)
a[!(a>=10)] # !(not)


# 2. Matrix 자료구조
# - 동일한 자료형을 갖는 2차원 배열구조
# - 생성함수 : matrix(), rbind(), cbind()
# - 처리함수 : apply() 

# (1) matrix
m1<- matrix(data=c(1:5)) # 행:n, 열:1
m1
dim(m1) #5X1
mode(m1)
class(m1)

m2<- matrix(data=c(1:9), nrow=3, ncol = 3, byrow = TRUE)
m2
dim(m2)

# (2) rbind()
x<-1:5
y<-6:10
x
y
m3<-rbind(x,y)
m3
dim(m3)

# (3) cbind()
m4<-cbind(x,y)
m4
dim(m4)

#(ADsp 문제 예) 
xy<-rbind(x,y)
# 다음 보기중에서 틀린 답은?
# 1. xy[1,]는 x와 같다.
# 2. xy[,1]는 y와 같다.
# 3. dim(xy)는 2x5이다.
# 4. class(xy)는 matrix이다.
xy[1,]
xy[,1]
dim(xy)
class(xy)
# 정답 : 2

# 색인(index) : matrix
# 형식) object[row, colum]
m5<- matrix(data=c(1:9), nrow=3, ncol = 3, byrow = TRUE)
m5

# 특정 행/열 색인
m5[1,]
m5[,1]
m5[1, 2:3]
m5[2,3]

# box 선택
m5[2:3, 1:2]

# - 속성
m5[-2,] # 2행 제외
m5[,-3] # 3열 제외
m5[,-c(1,3)]


# 열(칼럼=변수=변인) 이름 지정하기
colnames(m5)<-c("one", "two", "three")
m5

m5[,'one']
m5[,'one':'two'] #error
m5[,1:2]

# broadcast 연산
# - 작은 차원 -> 큰 차원 늘어나는 연산

x<- matrix(1:12, nrow=4, ncol=3, byrow=T)
x
dim(x)

# 1) scala(0) vs matrix(2)
0.5*x

# 2) vactor(1) vs matrix(2)
y<-10:12
y
y+x


# 3) 동인한 모양(shape)
x+x
x-x


# 4) 전치행렬 : 행-> 열, 열->행
x
t(x)

# 처리 함수 : apply()
?apply
# apply(X, MARGIN, FUN, ...)
x
apply(x, 1, sum) # 행 단위 합계
apply(x, 2, mean) # 열 단위 평균
apply(x, 1, var) # 행 단위 분산
apply(x, 1, sd) # 행 단위 표준편차


# 3. Array 자료구조
# - 동일한 자료형을 갖는 3차원 배열구조
# - 생성함수 : array()

# 1차원 -> 3차원
arr<-array(data = c(1:12), dim = c(3,2,2))
arr
dim(arr) # >> [1] 3 2 2 : 3행 2열 2면

# 3차원의 색인(index)
arr
arr[,,1] # 1면
arr[,,2] # 2면


data()
data(iris3)
iris3
dim(iris3)
50*4*3

# 붓꽃 dataset
iris3[,,1] # 꽃의 종1
iris3[,,2] # 꽃의 종2
iris3[,,3] # 꽃의 종3

iris3[10:20, 1:2,1]


# 4. data. frame
# - '열 단위 서로다른 자료형'을 갖는 2차원 배열구조
# - 생성 함수 : data.frame()
# - 처리 함수 : apply() -> 행렬 처리

# 1) vector 이용 
no <-1:3
name <- c('홍길동', '이순신', '유관순')
pay <- c(250, 350, 200)

emp<- data.frame(NO=no, NAME=name, PAY=pay)
emp
dim(emp) # >> 3 3
class(emp) # >> "data.frame"
mode(emp)  # >> "list" (2개 이상 자료형 포함)

# 자료참조 : 칼럼 참조 or index 참조
# 형식) object $ 칼럼
emp $ PAY
PAY <- emp $ PAY
PAY
mean(PAY)  # >> 266.6667
sd(PAY)  # >> 76.37626


# 형식) object[row, column]
emp_row <- emp[c(1,3),]
emp_row
emp_row1<- emp[-2,]
emp_row1


# 2) csv, text file, db table
setwd("c:/ITWILL/2_Rwork/Part-I")
getwd()

emp_txt <- read.table("emp.txt", header = T, sep = "")
emp_txt
class(emp_txt)

emp_csv <- read.csv("emp.csv") # 콤마 구분자
emp_csv
class(emp_csv) #"data.frame"

# [실습]
sid <- 1:3 # 이산형(정수)
score <- c(90, 85, 83) # 연속형(소수점 올수 있음)
gender <-c('M', 'F', 'M') # 문자형_범주형(카테고리 형성 할수 있음)

student <- data.frame(SID=sid, SCORE=score, GENDER=gender)
student

# 자료구조 보기
str(student) 
#'data.frame':	3 obs. of  3 variables:
# $ SID   : int  1 2 3 -- 이산형
# $ SCORE : num  90 85 83 -- 연속형
# $ GENDER: Factor w/ 2 levels "F","M": 2 1 2 -- 요인형(문자형 -> DF(요인형))


#stringsAsFactors = T : 문자형 -> 요인형 변환 여부

student <- data.frame(SID=sid, SCORE=score, GENDER=gender, stringsAsFactors = F)
str(student)
#'data.frame':	3 obs. of  3 variables:
# $ SID   : int  1 2 3
# $ SCORE : num  90 85 83
# $ GENDER: chr  "M" "F" "M" -- 문자형

# 특정칼럼 -> vector
score<- student$score

mean(score)
sum(score)
var(score)

# 표준편차
sqrt(var(score))
sd(score)

# 산포도 : 분산, 표준편차 

# 모집단에 대한 분산, 표준편차
# 분산 = sum((x-산술평균)^2)/n
# 표준편차 = sqrt(분산)

# 표본에 대한 분산, 표준편차  <- R함수
# 분산 = sum((x-산술평균)^2)/n-1

avg <- mean(score)
diff <- (score-avg)^2
VAR <- sum(diff)/(length(score)-1)
VAR

SD <- sqrt(VAR)
SD

# 5. List 자료구조
# - key와 value 한쌍으로 자료가 저장된다.
# - key는 중복 불가, value중복 가능하다.
# - key를 통해서 값(value)을 참조한다.
# - 다양한 자료형, 다양한 자료구조을 갖는 자료구조이다.

# 1) key 생략 : [key1=value1, key2=value2, ...]
lst <- list('lee', '이순신', 35, 'hong', '홍길동', 30)
lst
# 첫번째 원소 : key + value
# [[1]]   -- 기본키(default key)
# [1] "lee"  -- 값1(value)

# 두번째 원소 : key + value
# [[2]]   -- 기본키(default key)
# [1] "이순신"  -- 값2(value)

lst[1] #-- 첫번째 원소 index
# [[1]]
# [1] "lee"

lst[6] #-- 마지막 원소 index
# [[1]]
# [1] 30

# key를 통해서 value 참조
lst[[5]] # >> "홍길동"

# 2) key=value
lst2<- list(first=1:5, second=6:10)
lst2
# $first  -- key
# [1] 1 2 3 4 5  -- value

# $second   -- key
# [1]  6  7  8  9 10  -- value


# key -> value 참조
lst2$first # 1 2 3 4 5
lst2$first[3] # 3

lst2$second # 6  7  8  9 10
lst2$second[2:4] # 7 8 9

# data.frame($) vs list($)
# data.frame변수명$칼럼명
# list변수명$key이름

# 3) 다양한 자료형(문자형, 숫자형, 논리형)
lst3<-list(name=c('홍길동', '유관순'),
           age=c(35,25),
           gender=c('M','F'))
lst3

mean(lst3$age) #30

# 4) 다양한 자료구조(vector, matrix, array)

lst4 <-list(one=c('one', 'two', 'three'),
            two=matrix(1:9, nrow = 3),
            three=array(1:12, c(2,3,2)))
lst4

# 5) list 형변환
multi_list <- list(r1=list(1,2,3),
                   r2=list(10,20,30),
                   r3=list(100,200,300))

multi_list

# do.call(func,  object)
mat<-do.call(rbind, multi_list)
mat

# 6) list 처리 함수
x<-list(1:10) # key 생략
x

# list -> vector
v <- unlist(x)
v

a <- list(1:5)
b <- list(6:10)
a;b

# lapply(x, func) : list 객체에 함수 적용
lapply(c(a,b), max) # -- list로 반환
sapply(c(a,b), max) # -- vector로 반환


# 6. 서브셋(subset)
# - 특정 행 또는 열 선택 -> 새로운 dataset 생성

x <- 1:5
y <- 6:10
z <- letters[1:5]

df <- data.frame(x, y, z)
df

help("subset")
# subset(x, subset, select, drop = FALSE, ...)

# 1) 조건식으로 subset 생성 : 행 기준
df2 <- subset(df, x>=2)


# 2) select로 subset 생성 : 칼럼 기준
df3 <- subset(df, select=c(x, z))

# 3) 조건식 & select
df4 <- subset(df, x>2 & x<=4, select=c(x,z))


class(df2)
class(df3)
class(df4)

# 4) 특정 컬럼의 특정 값으로 subset 생성
df5 <- subset(df, z %in% c('a','c','e')) # %in% 연산자

# [실습] iris dataset 이용 생성
iris
str(iris)

iris_df = subset(iris, Sepal.Length >= mean(Sepal.Length), 
                 select=c(Sepal.Length, Petal.Length, Species))
iris_df
str(iris_df)


# 7. 문자열 처리와 정규표현식
install.packages("stringr")
library(stringr)

string = "hong35lee45kang55유관순25이사도시45"
string

# (1) str_extract_all

# 메타 문자 : 패턴지정 특수 기호

# 1) 반복관련 메타문자 : [x] : x 1개, {n} : n개 연속
str_extract_all(string, "[a-z]{3}") # 영문자소문자 연속 3개 오는 원소

str_extract_all(string, "[a-z]{3,}") # 3자 이상 연속

name <- str_extract_all(string, "[가-힣]{3,}") # 한글 3자이상
name
# list -> vector
unlist(name)

# 숫자(나이)추출
ages <- str_extract_all(string, "[0-9]{2,}")
# list -> vector로 변경
ages_vec <- unlist(ages)

#문자형 -> 숫자형 변환
num_ages <- as.numeric(ages_vec)

cat('나이평균=', mean(num_ages))


# 2) 단어와 숫자 관련 메타문자
# 단어 : \\w
# 숫자 : \\d

jumin <- "123456-5234567"

str_extract_all(jumin, "[0-9]{6}-[1-4][0-9]{6}")
str_extract_all(jumin, "[0-9]{6}-[1-4]\\d{6}")

# \\w : 영문, 숫자, 한글 -> 특수문자 제외
email <- "ka1234@naver.com"
str_extract_all(email, "[a-z]{3,}@[a-z]{3,}.[a-z]{2,}")
str_extract_all(email, "[a-z]\\w{3,}@[a-z]{3,}.[a-z]{2,}")

email2 <- "ka1$234@naver.com"

# 3) 접두어(^)/ 접미어($) 메타문자
email3 <- "1kp1234@naver.com"
str_extract_all(email3, "[a-z]\\w{3,}@[a-z]{3,}.[a-z]{2,}")
str_extract_all(email3, "^[a-z]\\w{3,}@[a-z]{3,}.[a-z]{2,}")

str_extract_all(email, "[a-z]\\w{3,}@[a-z]{3,}.com$")

# 4) 특정 문자 제외 메타문자
string
# 숫자 제외 나머지 반환
result <- str_extract_all(string,"[^0-9]{3,}")
result # [[1]] : 기본키
# 불용어 제거 : 숫자, 특수문자
name <- str_extract_all(result[[1]], "[가-힣]{3,}")
unlist(name)


# (2) str_length : 문자열 길이 반환
string

length(string)
str_length(string)

# (3) str_locate / str_locate_all
str_locate(string, 'g')
str_locate_all(string, 'g')

# (4) str_replace / str_replace_all
str_replace_all(string, "[0-9]{2}", "") ## 숫자제거

# (5) str_sub : 부분 문자열
str_sub(string, start=3, end = 5)


# (6) str_split : 문자열 분리(토큰)
string2 = "홍길동,이순신,강감찬,유관순"
result <- str_split(string2, ",")

name <- unlist(result)
name

# (7) 문자열 결함(join) : 기본함수
paste(name, collapse = ",")



