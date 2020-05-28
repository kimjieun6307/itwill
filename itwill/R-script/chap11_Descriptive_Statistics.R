########################################
## chap11_Descriptive_Statistics 수업내용
########################################

# 기술통계(Descriptive Statistics) 
# 대푯값 : 평균(Mean), 합계(Sum), 중위수(Median), 최빈수(mode), 사분위수(quartile) 등
# 산포도 : 분산(Variance), 표준편차(Standard deviation), 최소값(Minimum), 최대값(Maximum), 범위(Range) 등 
# 비대칭도 : 왜도(Skewness), 첨도(Kurtosis)


# 실습파일 가져오기
setwd("C:/ITWILL/2_Rwork/Part-III")
data <- read.csv("descriptive.csv", header=TRUE)
head(data) # 데이터셋 확인

# 1. 척도별 기술통계량
#  - 데이터 특성 보기(전체 데이터 대상)
dim(data) # 행(300)과 열(8) 정보 - 차원보기
length(data) # 열(8) 길이
length(data$survey) #survey 컬럼의 관찰치 - 행(300) 

str(data) # 데이터 구조보기 -> 데이터 종류,행/열,data
str(data$survey) 

# 데이터 특성(최소,최대,평균,분위수,노이즈-NA) 제공
summary(data) 

# 1) 명목/서열 척도 변수의 기술통계량
# - 명목상 의미없는 수치로 표현된 변수 - 성별(gender)     
length(data$gender)
summary(data$gender) # 명목척도 최소,최대,중위수,평균-의미없음
table(data$gender) # 각 성별 빈도수 - outlier 확인-> 0, 5
# 0   1   2   5 
# 2 173 124   1 


data <- subset(data, data$gender == 1 | data$gender == 2) # 성별 outlier 제거
x <- table(data$gender) # 성별에 대한 빈도수 저장
x # outlier 제거 확인
#   1   2 
# 173 124 

barplot(x) # 범주형(명목/서열척도) 시각화 -> 막대차트
#&&그림1
prop.table(x) # 비율 계산 : 0< x <1 사이의 값
#         1         2 
# 0.5824916 0.4175084 

y <-  prop.table(x)
round(y*100, 2) #백분율 적용(소수점 2자리)
#     1     2 
# 58.25 41.75 


# 2) 등간/비율 척도 변수의 기술통계량
# - 비율척도 : 수치로 직접 입력한 변수(cost)  
length(data$cost) # 297 (gender 이상치 제거로 300->297)
summary(data$cost) # 요약통계량 - 의미있음(mean) - 8.784
mean(data$cost) # NA
data$cost

# 데이터 정제 - 결측치 제거 및 outlier 제거
plot(data$cost)
#&&그림2

# --------------------------------------
# -참고- 
boxplot(data$cost)$stats # 2.1 ~ 7.9
#---------------------------------------

data <- subset(data, data$cost >= 2 & data$cost <= 10) # 총점기준
data
dim(data)
x <- data$cost
x


# 2. 대푯값 : cost 변수  이용
mean(x) # 평균 : 5.354
# 평균이 극단치에 영향을 받는 경우 - 중위수(median) 대체
median(x) # 5.4  
min(x) # 2.1
max(x) # 7.9
range(x) # min ~ max

# vector 정렬 - sort
sort(x) # 오름차순 
sort(x, decreasing=T) # 내림차순  

dim(data) # 248 8 

# data.frame 정렬 - order, arrange : 특정 컬럼(cost)
data[sort(data$cost), ] # index 정렬 /원하는 형식으로 정렬이 안됨.
data[order(data$cost), ] # 내용정렬(기존 행번호 유지)

library(dplyr)
arrange(data, cost) # 내용정렬(새로운 행렬)

# order vs arrange
# order : 기존 행 번호 유지
# arrange : 새로운 행 번호 적용

# 최빈수(mode)
mode(x) # data type 제공 -  "numeric"

install.packages("prettyR")
library(prettyR)
Mode(x) # 5 - 가장 많이 출현한 

# 최빈수=중위수=평균 : 좌우 대칭
# 최빈수 < 중위수, 평균 : 왼쪽 기울어짐
# 최빈수 > 중위수, 평균 : 오른쪽 기울어짐

mean(x) # 평균 : 5.354
median(x) # 5.4 
Mode(x) # 5


# 3. 산포도 : cost 변수 이용 
var(x) # 분산 - 1.296826
sd(x) # 표준편차는 분산의 양의 제곱근 - 1.138783

quantile(x, 1/4) # 1 사분위수 - 25% 4.6
quantile(x, 3/4) # 3 사분위수 - 75% 6.2

min(x) # 최소값-2.1
max(x) # 최대값-7.9
range(x) # 범위(min ~ max)


# 4. 비대칭도 :  패키지 이용
install.packages("moments")  # 왜도/첨도 위한 패키지 설치   
library(moments)

cost <- data$cost # 정제된 data
cost
# 왜도 - 평균을 중심으로 기울어진 정도
skewness(cost)  # -0.297234
# 음수(-) : 오른쪽 기울어짐(# 최빈수 > 중위수, 평균)
# 양수(+) : 왼쪽 기울어짐(# 최빈수 < 중위수, 평균)

# 첨도 - 표준정규분포와 비교하여 얼마나 뾰족한가 측정 지표
kurtosis(cost)    # 2.674163
# 3이상이면 꼭지점 뾰족 / 3미만이면 완만한 

# 기본 히스토그램 
hist(cost)
# &&& 그림3


# 히스토그램 확률밀도/표준정규분포 곡선 
hist(cost, freq = F)

# 확률밀도 분포 곡선 : 히스토그램의 밀도 추정 
lines(density(cost), col='blue')
# &&& 그림4

# 표준정규분포 곡선 
x <- seq(0, 8, 0.1)
curve( dnorm(x, mean(cost), sd(cost)), col='red', add = T)
# &&& 그림5

# 정규성 검정
shapiro.test(cost)
# data:  cost
# W = 0.98187, p-value = 0.002959
# p-value = 0.002959 < 0.05 : 귀무가설(정규분포와 차이가 없다)기각
#[해설] 정규분포와 차이가 난다.




################################################################
# 5. 기술통계량 보고서 작성법

# 1) 거주지역 
# 척도 변경 : 연속형 -> 범주형 
data$resident2[data$resident == 1] <-"특별시"
data$resident2[data$resident >=2 & data$resident <=4] <-"광역시"
data$resident2[data$resident == 5] <-"시구군"

x<- table(data$resident2)
x
# 광역시 시구군 특별시 
# 87     34    110 

prop.table(x) # 비율 계산 : 0< x <1 사이의 값
# 광역시    시구군    특별시 
# 0.3766234 0.1471861 0.4761905 

y <-  prop.table(x)
round(y*100, 2) #백분율 적용(소수점 2자리)
#광역시 시구군 특별시 
#37.66  14.72  47.62

# 2) 성별
# 척도 변경 : 연속형 -> 범주형 
data$gender2[data$gender== 1] <-"남자"
data$gender2[data$gender== 2] <-"여자"
x<- table(data$gender2)
x
# 남자 여자 
# 146  102 

prop.table(x) # 비율 계산 : 0< x <1 사이의 값
y <-  prop.table(x)
round(y*100, 2) #백분율 적용(소수점 2자리)
#남자  여자 
#58.87 41.13

# 3) 나이
# 척도 변경 : 연속형 -> 범주형 
summary(data$age)# 40 ~ 69
data$age2[data$age <= 45] <-"중년층"
data$age2[data$age >=46 & data$age <=59] <-"장년층"
data$age2[data$age >= 60] <-"노년층"

x<- table(data$age2)
x
# 노년층 장년층 중년층 
# 61    169     18 

prop.table(x) # 비율 계산 : 0< x <1 사이의 값
y <-  prop.table(x)
round(y*100, 2) #백분율 적용(소수점 2자리)
#노년층 장년층 중년층 
#24.60  68.15   7.26

# 4) 학력수준
data$level2[data$level== 1] <-"고졸"
data$level2[data$level== 2] <-"대졸"
data$level2[data$level== 3] <-"대학원졸"

x<- table(data$level2)
x

prop.table(x) # 비율 계산 : 0< x <1 사이의 값
y <-  prop.table(x)
round(y*100, 2) #백분율 적용(소수점 2자리)
#고졸     대졸 대학원졸 
#39.41    36.44    24.15

# 5) 합격여부
data$pass2[data$pass== 1] <-"합격"
data$pass2[data$pass== 2] <-"실패"
x<- table(data$pass2)
x

prop.table(x) # 비율 계산 : 0< x <1 사이의 값
y <-  prop.table(x)
round(y*100, 2) #백분율 적용(소수점 2자리)
#실패  합격 
#40.85 59.15

head(data) # data Mart


# <논문/보고서에서 표본의 인구통계적특성 결과 제시 방법>

# <인구통계적 특성 결과 제시>
#'부모의 생활수준과 자녀의 대학진학 여부와 관련성이 있다.'를 분석하기 위해서 
# 자녀를 둔 A회사 225명의 부모를 대상으로 거주지, 성별, 나이, 학력수준, 진학여부 등의 항목을 
# 설문으로 조사하고, 정제된 데이터를 토대로 빈도분석을 실시하였다. 
# 분석결과 전체 응답자 중에서 부모의 학력수준은 고졸이 93명으로 39.41%를 차지하여 
# 가장 높은 빈도수를 나타냈고, 자녀의 성별 비율은 남자가 146명으로 58.87%를 차지하고, 
# 여학생은 102명으로 41.13%을 차지하였다. 또한 자녀의 대학진학여부에서 합격은 139명으로 
# 59.15%를 차지하고, 실패는 96명으로 40.85%를 차지한 것으로 나타났다.








