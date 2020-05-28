# chap06_Datahandling

# 1. dplyr 패키지

install.packages("dplyr")
library(dplyr)
library(help="dplyr")



# 1) 파이프 연산자 : %>%
# 형식) df(data.frame)%>%func1()%>%func2()

iris %>% head() # = head(iris)
## 그림

iris %>% head() %>% filter(Sepal.Length>=5.0)
# 150관측치 > 6관측치 > 3관측치

##############################################
install.packages("hflights")
library(hflights)

str(hflights)

# 2) tbl_df() : 콘설의 크기만큼 자료를 구성해서 보여줌
hflights_df <- tbl_df(hflights)
hflights_df
## 그림

# 3) filter() : 행 추출
# 형식) df %>% filter(조건식) 
names(iris)
iris %>% filter(Species=="setosa") %>% head()

iris %>% filter(Sepal.Width>3) %>% head()

iris_df <- iris %>% filter(Sepal.Width>3) # subset 만드는 방법
iris_df

# 형식) filter(df, 조건식)
filter(hflights_df, Month==1 & DayofMonth==1)
# == hflights_df %>% filter(Month==1 & DayofMonth==1)
filter(hflights_df, Month==1 | DayofMonth==1)

# 4) arrange() : 정렬함수
# 형식) df %>% arrange()
iris %>% arrange(Sepal.Width) %>% head() #오름차순
iris %>% arrange(desc(Sepal.Width)) %>% head() # 내림차순

# 형식) arrange(df, 칼럼명)
arrange(hflights_df, Month, ArrTime)  # 월(1~12) > 도착시간

arrange(hflights_df, desc(Month), ArrTime)

# 5) select() : 열 추출
# 형식) df %>% select()
names(iris)
iris %>% select(Sepal.Length, Petal.Length, Species) %>% head()

# 형식) select(df, col1, col2, ...)
names(hflights_df)
select(hflights_df, DepTime, ArrTime, TailNum, AirTime)

select(hflights_df, Dest:Cancelled)

# 문) Month 기준으로 내림차순 정렬하고,
# Year, Month, AirTime 칼럼 선택하기

hflights_df %>% arrange(desc(Month)) %>% select(Year, Month, AirTime)

select(arrange(hflights_df, desc(Month)), Year, Month, AirTime)


# 6) mutate() : 파생변수 생성
# 형식) df %>% mutate(변수 = 함수 or 함수)
iris %>% mutate(diff=Sepal.Length-Sepal.Width) %>% head()

# 형식) mutate(df, 변수 = 함수 or 함수)
mutate(hflights_df, diff_delay = ArrDelay - DepDelay)
select(mutate(hflights_df, diff_delay = ArrDelay - DepDelay),
       ArrDelay, DepDelay, diff_delay)

# 7) summarise() : 통계 구하기
# 형식) df %>% summarise(변수 = 통계함수())
iris %>% summarise(col1_avg = mean(Sepal.Length),
                   col2_sd = sd(Sepal.Width))

# 형식) summarise(df, 변수 = 통계함수())
summarise(hflights_df, 
          delay_avg = mean(DepDelay, na.rm=T),
          delay_tot = sum(DepDelay, na.rm=T))
# 출발지연시간 평균/합계
# delay_avg delay_tot
# <dbl>     <int>
# 9.44   2121251

# 8) group_by(df, 집단변수) : 집단별 그룹화
# 형식) df %>% group_by(집단변수)
names(iris) # "Species" --> 집단변수
table(iris$Species)
grp <- iris %>% group_by(Species)

summarise(grp, mean(Sepal.Length)) # 집단별 통계구하는데 유용
# 1 setosa                     5.01
# 2 versicolor                 5.94
# 3 virginica                  6.59

summarise(grp, sd(Sepal.Length))

# group_by() [실습]
install.packages("ggplot2")
library(ggplot2)


data("mtcars") # 자동차 연비
head(mtcars)
str(mtcars) # 집단변수로 쓸수 있는 variables 확인
table(mtcars$cyl) #  4  6  8
table(mtcars$gear) #  3  4  5

# group : cyl
grp <- group_by(mtcars, cyl)
grp

# 각 집단별 연비 평균/표준편차
summarise(grp, mpg_avg=mean(mpg), mpg_sd=sd(mpg))


# (문제) 각 gear 집단별 무게(wt) 평균/표준편차
grp_gear <- group_by(mtcars, gear)
summarise(grp_gear, wt_avg=mean(wt), wt_sd=sd(wt))

# 두 개의 집단 변수 -> 그룹화
grp2 <- group_by(mtcars, cyl, gear) # cyl-1차 그룹화 , gear-2차 그룹화
summarise(grp2, mpg_avg=mean(mpg), mpg_sd=sd(mpg))

# 형식 ) group_by(df, 집단변수)

# 예제) 각 항공기별 비행편수가 40편 이상이고, 
# 평균 비행거리가 2,000마일 이상인 경우의
# 평균 도착지연시간을 확인하시오.

# 1) 항공기별 그룹화
str(hflights_df) # 항공기 variable : TailNum
planes <- group_by(hflights_df, TailNum)
planes # Groups:   TailNum [3,320]

# 2) 항공기별 요약 통계 : 비행편수, 평균 비행거리, 평균 도착지연시간
planes_sta <- summarise(planes, count=n(), 
          dis_avg=mean(Distance, na.rm=T), 
          arr_avg=mean(ArrDelay, na.rm=T))

planes_sta

# 3) 항공기별 요약 통계 필터링
filter(planes_sta, count>=40 & dis_avg >= 2000)


#######################################################3
# 2. reshape2
install.packages("reshape2")
library(reshape2)

# 1) dcast() : long -> wide

data <- read.csv(file.choose())
# 변수 : Date(구매일자),Customer_ID(고객 구분자), Buy(구매수량)

# 형식) dcast(dataset, row~col, func)
# row ->Date(구매일자), col -> Customer_ID(고객 구분자)
wide1 <- dcast(data, Date ~ Customer_ID, sum )

wide <- dcast(data, Customer_ID ~ Date, sum )

library(ggplot2)
data(mpg)
str(mpg)

mpg_df <- as.data.frame(mpg)
mpg_df
str(mpg_df)

mpg_df <- select(mpg_df, c(cyl, drv, hwy))
head(mpg_df)

table(mpg_df$cyl) # 4집단
table(mpg_df$drv) # 3집단

#교차셀에 hwy 합계
tab <- dcast(mpg_df, cyl~drv, sum) # 4행 3열 table
tab

# 교차셀에 hwy 출현 건수
tab2 <- dcast(mpg_df, cyl ~ drv, length)
tab2

# 교차분할표
# table(집행단변수, 열집단 변수)
table(mpg_df$cyl, mpg_df$drv)

unique(mpg_df$cyl) # 4 6 8 5
unique(mpg_df$drv) #"f" "4" "r"

# 2) melt() : wide -> long
# 형식) melt(long frame 변경 데이터셋, id='row변수')
wide <- dcast(data, Customer_ID ~ Date, sum )
str(wide)

long <- melt(wide, id="Customer_ID")
long

# Customer_ID : 기준 칼럼
# variable : 열이름
# value : 교차셀의 값

names(long) <- c("User_ID", "Date", "Buy")
long

#############################################
# example : with -> long
data("smiths")
smiths

long <- melt(smiths, id="subject")
long

long2 <- melt(smiths, id = 1:2)
long2

# example : long -> with
wide <- dcast(long, subject ~ ...) # ... : 나머지 칼럼
wide



#############################################
# 3. acast(dataset, 행~열~면)
data("airquality")
str(airquality)

table(airquality$Month)
# 5  6  7  8  9   --> 월
# 31 30 31 31 30  --> 일

# wide >> long
air_melt <- melt(airquality, id=c("Month", "Day"), na.rm = T)
dim(air_melt) # 568   4
table(air_melt$variable)
# Ozone Solar.R    Wind    Temp 
# 116     146     153     153 

# [행, 열, 면] >> [일, 월, variable]
# acast(dataset, 일 ~ 월 ~ variable)
air_arr3d <- acast(air_melt, Day ~ Month ~ variable)
dim(air_arr3d) # 31  5  4

# 오존 data
air_arr3d[, ,1]
# 태양열 data
air_arr3d[, ,2]

########## 추가내용 ############
# 4. URL 만들기 : http://www.naver.com?name='홍길동'

# 1) base url 만들기
baseurl <- "http://www.sbus.or.kr/2018/lost/lost_02.htm"

# 2) page query 추가
# http://www.sbus.or.kr/2018/lost/lost_02.htm?Page=1
no <- 1:5
library(stringr)
page <- str_c('?Page=', no)
page

# outer(x(1), Y(n), func)
page_url <- outer(baseurl, page, str_c)
page_url
dim(page_url)

# reshape : 2차원 -> 1차원
page_url <- sort(as.vector(page_url))
page_url

# 3) sear query 추가
# http://www.sbus.or.kr/2018/lost/lost_02.htm?Page=2&sear=2 
no <- 1:3
sear <- str_c("&sear=", no)
sear

final_url <- outer(page_url, sear, str_c)
final_url <-sort(as.vector(final_url))
final_url




