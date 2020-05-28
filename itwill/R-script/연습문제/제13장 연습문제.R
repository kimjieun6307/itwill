# chap13_Ttest_Anova(연습문제)

#############################################
# 추론통계분석 - 1-1. 단일집단 비율차이 검정
#############################################

# 01. 중소기업에서 생산한 HDTV 판매율을 높이기 위해서 프로모션을 진행한 결과 
# 기존 구매비율 15% 보다 향상되었는지를 각 단계별로 분석을 수행하여 검정하시오.

#연구가설(H1) : 기존 구매비율과 차이가 있다.
#귀무가설(H0) : 기존 구매비율과 차이가 없다.

#조건) 구매여부 변수 : buy (1: 구매하지 않음, 2: 구매)

#(1) 데이터셋 가져오기
setwd("C:/ITWILL/2_Rwork/Part-III")
hdtv <- read.csv("hdtv.csv", header=TRUE)

head(hdtv)
#   user.id buy
# 1       1   2
# 2       2   1
# 3       3   1
# 4       4   1
# 5       5   2
# 6       6   2

# (2) 빈도수와 비율 계산
table(hdtv$buy)
# 1  2 
# 40 10 

prop.table(table(hdtv$buy))
# 1   2 
# 0.8 0.2 

# (3)가설검정
binom.test(10, 50, p=0.15)
# p-value = 0.321 > 0.05 --귀무가설 채택
#(결론) 귀무가설(H0) : 기존 구매비율과 차이가 없다. 
# >> 프로모션을 진행한 결과가 좋지 않다(=프로모션 실패)

# **오답**
binom.test(table(hdtv$buy))
# p-value = 2.386e-05 < 0.05 -- 귀무가설 기각 
# (결론) 연구가설(H1) : 기존 구매비율과 차이가 있다.


#################################################
# 추론통계학 분석 - 1-2. 단일집단 평균차이 검정
#################################################

# 02. 우리나라 전체 중학교 2학년 여학생 평균 키가 148.5cm로 알려져 있는 상태에서 
# A중학교 2학년 전체 500명을 대상으로 10%인 50명을 표본으로 선정된 데이터 셋을 이용하여
# 모집단의 평균과 차이가 있는지를 각 단계별로 분석을 수행하여 검정하시오.

#(1) 데이터셋 가져오기
sheight<- read.csv("student_height.csv", header=TRUE)

str(sheight)

# (2) 기술통계량 평균 계산
she_hi<- sheight$height
mean(she_hi)


# (3) 정규성 검정
shapiro.test(she_hi)
# p-value = 0.0001853 < 0.05
# (결론) 정규성이 아니다.
hist(she_hi)

# (4) 가설검정 

# - 오답-
t.test(she_hi, mu=148.5) 
# p-value = 0.1212 > 0.05 --귀무가설 채택
# (결론) 귀무가설 : A중학교 2학년 여학생 평균 키는 전체 평균(148.5)과 차이가 없다.

wilcox.test(she_hi, mu=148.5)
# V = 826, p-value = 0.067
# p-value = 0.067 < 0.05 -- 귀무가설 기각
# (결론) A중학교 2학년 여학생 평균 키는 전체 평균(148.5)과 차이가 난다.



#################################################
# 추론통계학 분석 - 2-1. 두집단 비율 차이 검정
#################################################

# 03. 대학에 진학한 남학생과 여학생을 대상으로 진학한 대학에 
# 대해서 만족도에 차이가 있는가를 검정하시오.

# 힌트) 두 집단 비율 차이 검정
#  조건) 파일명 : two_sample.csv, 변수명 : gender(1,2), survey(0,1)
# gender : 남학생(1), 여학생(2)
# survey : 불만(0), 만족(1)
# prop.test('성공횟수', '시행횟수')

sample <- read.csv(file.choose())
head(sample)

table(sample$gender)
table(sample$survey)
table(sample$gender, sample$survey, useNA="ifany" )
sum(sample$gender)

prop.test(c(138, 107), c(174, 126))
# X-squared = 1.1845, df = 1, p-value = 0.2765
# p-value = 0.2765 > 0.05 : 귀무가설 채택
# (결론) 남학생, 여학생간의 대학 진학율에 대한 만족도 차이가 없다.

##################################################
# 추론통계학 분석 - 2-2. 두집단 평균 차이 검정
##################################################

# 04. 교육방법에 따라 시험성적에 차이가 있는지 검정하시오.

#힌트) 두 집단 평균 차이 검정
#조건1) 파일 : twomethod.csv
#조건2) 변수 : method : 교육방법, score : 시험성적
#조건3) 모델 : 교육방법(명목)  ->  시험성적(비율)
#조건4) 전처리 : 결측치 제거 : 평균으로 대체 

twomethod <- read.csv(file.choose())
head(twomethod)

method <- twomethod$method
score <- twomethod$score

summary(score) # 결측치 있음.
table(method)

method1 <- subset(twomethod, method==1)
method2 <- subset(twomethod, method==2)

method1_score <- method1$score
method2_score <- method2$score

mean(method1_score, na.rm = T) # 16.40909
mean(method2_score, na.rm = T) # 29.22857

var.test(method1_score, method2_score)
# F = 1.0648, num df = 21, denom df = 34, p-value = 0.8494
# p-value = 0.8494 > 0.05 : 두 집단이 동질한 것으로 본다

t.test(method1_score, method2_score)
# t = -5.6056, df = 43.705, p-value = 1.303e-06
# p-value = 1.303e-06 < 0.05 : 귀무가설 기각
# 귀무가설 : 교육방법에 따라 시험성적에 차이가 없다.
# (결론) 교육방법에 따라 시험성적에 차이가 있다


# - 결측치 평균으로 대체 -
m1 <- ifelse(is.na(method1_score), mean(method1_score, na.rm = T), method1_score)
m2 <- ifelse(is.na(method2_score), mean(method2_score, na.rm = T), method2_score)

mean(m1) # 16.40909
mean(m2) # 29.22857

var.test(m1, m2)
# F = 1.0866, num df = 23, denom df = 38, p-value = 0.8011
# p-value = 0.8011 > 0.05 :  두 집단이 동질한 것으로 본다 

t.test(m1, m2)
# t = -6.1741, df = 47.255, p-value = 1.438e-07
# p-value = 1.438e-07 < 0.05 : 귀무가설 기각
# 귀무가설 : 교육방법에 따라 시험성적에 차이가 없다.
# (결론) 교육방법에 따라 시험성적에 차이가 있다

############################################################################
# 05. iris 데이터셋을 이용하여 다음과 같이 분산분석(aov)을 수행하시오.
# 독립변수 : Species(집단변수)
# 종속변수 : 1번 칼럼 ~ 4번 칼럼중에 전제조건을 만족하는 변수 선택
# 분산분석 수행 -> 사후검정 해석

#(참고) 전제조건 : 동질하다

str(iris)
# Sepal.Length / Sepal.Width / Petal.Length / Petal.Width

table(iris$Species)
# setosa versicolor  virginica 
# 50         50         50 

# outlier 확인
iris$Sepal.Length
plot(iris$Sepal.Length)

iris$Sepal.Width
plot(iris$Sepal.Width)

iris$Petal.Length
plot(iris$Petal.Length)

iris$Petal.Width
plot(iris$Petal.Width)

# 동일성 검정
# (1) Sepal.Length
iris_data1 <- subset(iris, !is.na(Sepal.Length), c(Species, Sepal.Length)) 
head(iris_data1)

bartlett.test(Sepal.Length ~ Species, data=iris_data1)
# Bartlett's K-squared = 16.006, df = 2, p-value = 0.0003345
# p<0.05 : 동질하지 않다.

# (2) Sepal.Width
iris_data2 <- subset(iris, !is.na(Sepal.Width), c(Species, Sepal.Width)) 
head(iris_data2)

bartlett.test(Sepal.Width ~ Species, data=iris_data2)
#  p-value = 0.3515 > 0.05 : 동질하다

# (3) Petal.Length
iris_data3 <- subset(iris, !is.na(Petal.Length), c(Species, Petal.Length)) 
head(iris_data3)

bartlett.test(Petal.Length ~ Species, data=iris_data3)
# p-value = 9.229e-13 < 0.05 : 동질하지 않다.

# (4) Petal.Width
iris_data4 <- subset(iris, !is.na(Petal.Width), c(Species, Petal.Width)) 
head(iris_data4)

bartlett.test(Petal.Width ~ Species, data=iris_data4)
# p-value = 3.055e-09 < 0.05 : 동질하지 않다.

# 분산검정
iris_result <- aov(Sepal.Width ~ Species, data=iris_data2)
summary(iris_result)
#              Df Sum Sq Mean Sq F value Pr(>F)
# Species       2  11.35   5.672   49.16 <2e-16
# Residuals   147  16.96   0.115  

# p(<2e-16) < 0.05 : 귀무가설 기각
# (해석) 꽂 종류간의 Sepal.Width 평균의 차이가 있다.
# [결론] 매우 유의미한 수준에서 적어도 한 집단의 평균 차이가 난다.

# 사후검정
TukeyHSD(iris_result)
#                        diff         lwr        upr     p adj
# versicolor-setosa    -0.658 -0.81885528 -0.4971447 0.0000000
# virginica-setosa     -0.454 -0.61485528 -0.2931447 0.0000000
# virginica-versicolor  0.204  0.04314472  0.3648553 0.0087802

#[해설]
# 95% 신뢰수준에서 3집단(꽃의 종별) 모두 평균차이가 있다.
# 꽃잎의 넓이(Sepal.Width) 변수는 versicolor-setosa에서 가장 큰 평균 차이를 보인다.

plot(TukeyHSD(iris_result))
# 3집단 모두 신뢰구간이 0을 포함하지 않는다.

methods(plot)

library(dplyr) # df %>% funcion()

iris %>% group_by(Species) %>% summarise(width_mu=mean(Sepal.Width))
# Species    width_mu
#   <fct>         <dbl>
# 1 setosa         3.43
# 2 versicolor     2.77
# 3 virginica      2.97







