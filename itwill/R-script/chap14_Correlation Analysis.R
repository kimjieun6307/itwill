# chap14_Correlation Analysis

##################################################
# chap14. 상관관계 분석(Correlation Analysis)
##################################################
# - 변수 간 관련성 분석 방법 
# - 관련함수 : cor(), cov(), cov2cor() 

product <- read.csv("C:/ITWILL/2_Rwork/Part-III/product.csv", header=TRUE)
head(product) 
#   제품_친밀도 제품_적절성 제품_만족도
# 1           3           4           3
# 2           3           3           2
# 3           4           4           4
# 4           2           2           2
# 5           2           2           2
# 6           3           3           3
# 친밀도/적절성/만족도(★등간척도★ - 5점 척도)
#@@10

# 기술통계량
summary(product) # 요약통계량

sd(product$제품_친밀도); sd(product$제품_적절성); sd(product$제품_만족도)

# ● 변수 간의 상관관계 분석 
# 형식) cor(x,y, method) - x변수, y변수, method(pearson): 방법

#@@피어슨 상관계수

# 1) 상관계수(coefficient of correlation) : 두 변량 X,Y 사이의 상관관계 정도를 나타내는 수치(계수)
cor(product$제품_친밀도, product$제품_적절성) 
# 0.4992086 -> 다소 높은 양의 상관관계

cor(product$제품_친밀도, product$제품_만족도) 
# 0.467145 -> 다소 높은 양의 상관관계

cor(product$제품_적절성, product$제품_만족도) 
# 0.7668527 -> 놓은 양의 상관관계

# ● 전체 변수 간 상관계수 보기
cor(product, method="pearson") # 피어슨 상관계수 - default
#@@11

# ● 방향성 있는 색생으로 표현 - 동일 색상으로 그룹화 표시 및 색의 농도 
install.packages("corrgram")   
library(corrgram)
corrgram(product) # 색상 적용 - 동일 색상으로 그룹화 표시
#@@12
corrgram(product, upper.panel=panel.conf) # 수치(상관계수) 추가(위쪽)
#@@13
corrgram(product, lower.panel=panel.conf) # 수치(상관계수) 추가(아래쪽)
#@@14

# ● 차트에 곡선과 별표 추가
install.packages("PerformanceAnalytics") 
library(PerformanceAnalytics) 

# ● 상관성,p값(*),정규분포 시각화 - 모수 검정 조건 
chart.Correlation(product, histogram=, pch="+") 
#@@15

# spearman : 서열척도 대상 상관계수

# 2) 공분산(covariance) : 두 변량 X,Y의 관계를 나타내는 양
cor(product)
cov(product)
#@@16

cov2cor(cov(product)) # 공분산 행렬 -> 상관계수 행렬 변환
#@@17

# 상관계수 vs 공분산
# 공통점 : 두 확률변수의 관계를 나타내는 값
# 상관계수 : 두 변수간의 관계를 크기(양)와 방향(-, +)으로 제공
# 공분산 : 두 변수간의 관계 크기(양) 제공
# ◈공분산 보다는 상관계수를 더 많이 선호함. 왜냐하면 공분산은 변수의 크기에 영향을 받기 때문이다. 

# - 공분산 계산해 보기 -
x <- product$제품_적절성
y <- product$제품_만족도

cov_xy <- mean((x-mean(x))*(y-mean(y)))
cov_xy  # 0.5442637

r= cov_xy / (sd(x)*sd(y))
r  #0.763948

# 공분산 : 크기 영향을 받는다
score_iq <- read.csv(file.choose())
head(score_iq)
#     sid score  iq academy game tv
# 1 10001    90 140       2    1  0
# 2 10002    75 125       1    3  3
# 3 10003    77 120       1    0  4
# 4 10004    83 135       2    3  2
# 5 10005    65 105       0    4  4
# 6 10006    80 123       3    1  1

cor(score_iq[-1])
#              score          iq    academy        game         tv
# score    1.0000000  0.88222034  0.8962647 -0.29819318 -0.8197516
# iq       0.8822203  1.00000000  0.6717826 -0.03151645 -0.5850329
# academy  0.8962647  0.67178257  1.0000000 -0.35131543 -0.9485507
# game    -0.2981932 -0.03151645 -0.3513154  1.00000000  0.2392166
# tv      -0.8197516 -0.58503295 -0.9485507  0.23921661  1.0000000

# 0.88222034  0.8962647

cov(score_iq[-1])
# 51.3375391  7.1199105
#@@18














