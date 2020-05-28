#################################
## <제11장 연습문제>
################################# 

#01. descriptive.csv 데이터 셋을 대상으로 다음 조건에 맞게 빈도분석 및 기술통계량 분석을 수행하시오

setwd("C:/ITWILL/2_Rwork/Part-III")
data <- read.csv("descriptive.csv", header=TRUE)
head(data) # 데이터셋 확인

# 조건1) 명목척도 변수인 학교유형(type), 합격여부(pass) 변수에 대해 빈도분석을 수행하고 
# 결과를 막대그래프와 파이차트로 시각화 
x <- table(data$type)
x1 <- table(data$pass)

barplot(x, main = '학교유형(type) 빈도분석')
barplot(x1, main = '합격여부(pass) 빈도분석')

pie(x, main = '학교유형(type) 빈도분석')
pie(x1, main = '합격여부(pass) 빈도분석')

# 조건2) 비율척도 변수인 나이 변수에 대해 요약치(평균,표준편차)와 비대칭도(왜도와 첨도)
# 통계량을 구하고, 히스토그램으로 비대칭도 설명
summary(data$age)


mean(data$age) #53.88
sd(data$age) # 6.813247
skewness(data$age) # 0.3804892
kurtosis(data$age) # 1.866623

hist(data$age)

# [해설] 대칭적이지 않다.

# 조건3) 나이 변수에 대한 밀도분포곡선과 정규분포 곡선으로 정규분포 검정
hist(data$age, freq = F)
lines(density(data$age), col='blue')

x <- seq(20, 80, 0.1)
curve( dnorm(x, mean(data$age), sd(data$age)), col='red', add = T)

Mode(data$age) # 48 < mean : 왼쪽 기울
#[해설] 정규분포에 비해 왼쪽으로 기울어졌다.
