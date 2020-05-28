# chap01_Basic

# 수업내용
# 1. 패키지와 세션
# 2. 패키지 사용법
# 3. 변수와 자료형
# 4. 기본함수와 작업공간

# 1. 패키지와 세션
dim(available.packages())
# [1] 15297(패키지 수)  17(패키지 정보)

available.packages()
dim(available.packages())
# [1] 15308    17

15308-15297   #11
15308-15250   #58

getOption("max.print") #1000

58*17 #986


# session
sessionInfo() # 세션 정보 제공
# R환경, os환경, 다국어(locale)정보, 기본 7패키지

# 주요 단축키
# script 실행 : ctrl + Enter
# save : ctrl + s
# 자동완성 : ctrl + space bar
# 여러줄 주석 : 드래그 + ctrl + shift + c (토글)
# a <- 10
# b <- 20
# c <- a+b
# print(c)

# 2. 패키지 사용법 : package=fuction + dataset

# 1) 패키지 설치
install.packages('stringr')
install.packages(stringr) #Error: 객체 'stringr'를 찾을 수 없습니다


# 패키지(1) + 의존성 패키지(3)

# 2) 패키지 설치 경로
.libPaths()
# [1] "C:/Users/user/Documents/R/win-library/3.6" -- 확장 패키지
# [2] "C:/Program Files/R/R-3.6.2/library"  --기본 30개 패키지

# 3) in memory : 패키지 -> upload
library(stringr) # = library('stringr') 둘다 쓸수 있음.

# memory 로딩된 패키지
search()

str_extract('홍길동35이순신45', '[가-힣]{3}')
# [1] "홍길동"
str_extract_all('홍길동35이순신45', '[가-힣]{3}')
# [[1]][1] "홍길동" "이순신"


# 4) 패키지 삭제
remove.packages('stringr') 
# 설치할때는 의존성 패키지 3건도 같이 설치 됬지만 삭제는 stringr 하나만 삭제됨
# 물리적 삭제 가능(폴더로 들어가서 파일 직접 삭제)


# 2020.02.27 수업
install.packages('stringr')

# 구버전 패키지 현재 위치에 설치 하는 방법 
# install.packages('https://cran.rstudio.com/bin/windows/contrib/3.2/xxx.zip', repos=null)



###############################
## 패키지 설치 error 해결법
###############################

# 1. 최초 패키지 설치
# - RStudio 관리자 권한으로 실행

# 2. 기존 패키지 설치
# 1) remove.packages('패키지')
# 2) rebooting
# 3) install.packages('패키지')


# 3. 변수와 자료형
# 1) 변수 : 메모리 이름 

# 2) 변수 작성 규칙 및 특징
# - 첫자는 영문, 두번째는 숫자, 특수문자(_  .)
#  ex) score2020, score_2020, score.2020
# - 예약어, 함수명
# - 대소문자 구분
#  ex) NUM=100, num=100 >> 다른 변수임.
# - 변수 선언시 type 선언 없음
# - R표현 : score = 90  vs C언어 표현 : int score = 90
# - 가장 최근값으로 변경됨
# - R의 모든 변수는 객체(object)

var1 <- 0 #같은식 var1 = 0
var1 <- 1

var1
print(var1)

var2 <- 10
var3 <- 20

var1; var2; var3
# [1] 1
# [1] 10
# [1] 20


# 색인(index) : 저장 위치
var3 <- c(10, 20, 30, 40, 50)
var3
# [1] 10 20 30 40 50
var3[5]
# [1] 50


# 대소문
NUM = 100
num = 200
print(NUM == num) # 관계식 >> True/False
# [1] FALSE

# object.member
member.id = 'hong' # == "hong"
member.name = "홍길동"
member.age = 35

member.id; member.age

# scala(0) vs vector(1)
score <- 95 # scala
scores <- c(85, 75, 95, 100) #vector

score # [1] 95
scores # [1]  85  75  95 100



# 3) 자료형(data type) : 숫자형, 문자형, 논리형

int <- 100
float <- 125.23
string <- "대한민국"
bool <- TRUE # TRUE, T, FALSE, F

# mode : 자료형 반환 함수 >> 
mode(int) # [1] "numeric"
mode(float) #[1] "numeric"
mode(string) #[1] "character"
mode(bool) #[1] "logical"

# is.xxxx
is.numeric(int) #[1] TRUE
is.character(string) #[1] TRUE
is.logical(bool) #[1] TRUE
is.numeric(string) #[1] FALSE

datas <- c(84, 85, 62, NA, 45)
datas #[1] 84 85 62 NA 45

is.na(datas) # 결측치 >> TRUE 
#[1] FALSE FALSE FALSE  TRUE FALSE



# 4) 자료형변환 함수 : P.20
# (1) 문자형 -> 숫자형 변환
x<-c(10, 20, 30) # vector
x
mode(x)

x<-c(10, 20, 30, '40') # vector
x
mode(x)

x<- as.numeric(x)
x*2 # 숫치 연산
x**2
x
plot(x)


# (2) 요인형(factor)
# 범주형 변수(집단변수) 생성

gender <- c('남', '여', '남', '여', '여')
mode(gender) #[1] "character"

# 문자형 -> 요인형(범주형) 변환
fgender<-as.factor(gender)
mode(fgender) #[1] "numeric"

plot(fgender)
plot(gender)

gender #[1] "남" "여" "남" "여" "여"
fgender
# [1] 남 여 남 여 여
# Levels: 남 여 >> Levels 순서는 오름차순(변경가능)
str(fgender) # Factor w/ 2 levels "남","여": 1 2 1 2 2

# mode vs class

# mode:자료형 확인
mode(fgender) #"numeric" >> 요인형은 숫자타입이지만 숫자의미는 없음.(=더미변수)
# 더미변수 : 숫자에 의미가없는 숫자형

# class : 자료구조 확인 
class(fgender) #[1] "factor"

# 숫자형 변수
x<-c(4,2,4,2)
mode(x) #[1] "numeric"

# 숫자형 -> 요인형
f<-as.factor(x)
f

# 요인형 -> 숫자형
x2<-as.numeric(f)
x2

# 요인형 -> 문자형
c<- as.character(f)
c

# 문자형 -> 숫자형
x2<-as.numeric(c)
x2


# 4. 기본함수와 작업공간

# 1) 기본함수 : 7개 패키지에 속한 함수
sessionInfo() #attached base packages:stats,graphics,grDevices, utils, datasets, methods, base  

library(stringr) #저번시간에 삭제해서 없음.

#패키지 도움말
library(help='stats')

# 함수 도움말
help(sum) #sum(..., na.rm = FALSE)

x<-c(10,20,30,NA)
sum(x, na.rm=TRUE) #[1] 60
sum(10,20,30,NA, na.rm=TRUE) #[1] 60
sum(1:5) #[1] 15
sum(1,2,3,4,5) #[1] 15

?mean # mean(x, ...)
mean(10,20,30,NA, na.rm=TRUE) #[1] 10 >> 잘못된 결과값 나옴.
mean(x, na.rm=TRUE) #[1] 20


# 2) 기본 데이터셋
data() #데이터셋 확인
data(Nile) #in memory

Nile
length(Nile)
mode(Nile)
plot(Nile)
hist(Nile)


# 3) 작업공간
getwd() #[1] "C:/ITWILL/2_Rwork"
setwd("c:/ITWILL/2_Rwork/Part-I")
getwd() #[1] "c:/ITWILL/2_Rwork/Part-I"

emp <-read.csv("emp.csv", header = T)
emp
