#################################
## <제15장 연습문제>
################################# 

###################################
## 선형 회귀분석 연습문제 
###################################

# 01. ggplot2패키지에서 제공하는 diamonds 데이터 셋을 대상으로 
# carat, table, depth 변수 중 다이아몬드의 가격(price)에 영향을 
# 미치는 관계를 다음과 같은 단계로 다중회귀분석을 수행하시오.

library(ggplot2)
data(diamonds)

#(1)
head(diamonds)
str(diamonds)

y<- diamonds$price
x1 <- diamonds$carat
x2 <- diamonds$table
x3 <- diamonds$depth

df <- data.frame(x1, x2, x3, y) # == df <- diamond[c()]
head(df)

#(2)
cols <- names(diamonds)
cols
dia_data <- diamonds[c(cols[1], cols[5:7])]

# 단계1 : 다이아몬드 가격 결정에 가장 큰 영향을 미치는 변수는?
result <- lm(formula = y ~ x1 + x2 + x3, data = df)
result
summary(result)
# (해석) t value(절대값) : x1(555.36) > x2(-33.26) > x3(-31.38)
#        x1(carat)변수가 가격 결정에 가장 큰 영향을 미친다.

# (2)
# 1. model 유의성 검정 : 
# 2. 

# 단계2 : 다중회귀 분석 결과를 정(+)과 부(-) 관계로 해설
# Coefficients:
# (Intercept)           x1           x2           x3  
#     13003.4       7858.8       -104.5       -151.2  
#(해석) x1(carat)변수는 가격과 정(+)관계, 
#       x2(table)와 x3(depth)변수는 부(-) 관계를 갖는다.

##########################################################################
# 02. mtcars 데이터셋을 이용하여 다음과 같은 단계로 다중회귀분석을 수행하시오.

library(datasets)
str(mtcars) # 연비 효율 data set 

y2 <- mtcars$mpg
x21 <- mtcars$hp
x22 <- mtcars$wt

df2 <- data.frame(x21, x22, y2)
head(df2)
result2 <- lm(formula = y2 ~ x21+x22, data = df2)
result2
summary(result2)

# 단계1 : 연비(mpg)는 마력(hp), 무게(wt) 변수와 어떤 상관관계를 갖는가? 
# Coefficients:
# (Intercept)          x21          x22  
#    37.22727     -0.03177     -3.87783  
#(해석) 음의 상관관계를 갖는다.

# 상관관계 : cor
cor(df2)
#y2  -0.7761684 -0.8676594  1.0000000
#[해석] 모두 음의 상관관계를 갖느다


# 단계2 : 마력(hp)과 무게(wt)는 연비(mpg)에 어떤 영향을 미치는가? 

# x21   -0.03177    0.00903  -3.519  0.00145 **  : 마력 < 0.05 영향 미침
# x22   -3.87783    0.63273  -6.129 1.12e-06 *** : 무게 < 0.05 영향 미침
#(해석) 마력(x21)과 무게(x22)가 무거울 수록 연비는 적어지는 부(-) 관계를 갖는다.
#       마력보다는 무게가 연비에 더 많은 영향을 미친다.

#[해설] x변수 모두 유의미한 수준에서 음의 영향이 미친다고 볼 수 있다.
# 특히 wt는 매우 유의미한 수준에서 y에 영향을 미친다고 볼 수 있다.

# 단계3 : hp = 90, wt = 2.5t일 때 회귀모델의 예측치는?
predict(result2, data.frame(x21=90, x22=2.5) ) 
# 24.67313

##############################################################3
# 03. product.csv 파일의 데이터를 이용하여 다음과 같은 단계로 다중회귀분석을 수행하시오.
setwd("C:/ITWILL/2_Rwork/Part-IV")
product <- read.csv("product.csv", header=TRUE)

head(product)


#  단계1 : 학습데이터(train),검정데이터(test)를 7 : 3 비율로 샘플링
nrow(product) # 264

# sample(nrow(product), 0.7*nrow(product), replace = F)
a <- sample(1: nrow(product), 0.7*nrow(product))
product_train <- product[a,]
product_test <- product[-a, ]

#  단계2 : 학습데이터 이용 회귀모델 생성 
#        변수 모델링) y변수 : 제품_만족도, x변수 : 제품_적절성, 제품_친밀도
product_lm <- lm(formula = 제품_만족도 ~ . , data=product_train)

summary(product_lm)

#  단계3 : 검정데이터 이용 모델 예측치 생성 
product_pred <- predict(product_lm, product_test)
product_pred


#  단계4 : 모델 평가 : MSE, cor()함수 이용  
product_true <- product_test$제품_만족도
ERROR <- product_true - product_pred
MSE <- mean(ERROR**2)
MSE # 0.3538749

r <- cor(product_true, product_pred)
cat('r= ', r) # 0.754717


###################################
## 로지스틱 회귀분석 연습문제 
###################################
# 04.  admit 객체를 대상으로 다음과 같이 로지스틱 회귀분석을 수행하시오.
# <조건1> 변수 모델링 : y변수 : admit, x변수 : gre, gpa, rank 
# <조건2> 7:3비율로 데이터셋을 구성하여 모델과 예측치 생성 
# <조건3> 분류 정확도 구하기 

# 파일 불러오기
admit <- read.csv('admit.csv')
str(admit) # 'data.frame':	400 obs. of  4 variables:
#$ admit: 입학여부(y) - int  0 1 1 1 0 1 1 0 1 0 ...
#$ gre  : 시험점수 - int  380 660 800 640 520 760 560 400 540 700 ...
#$ gpa  : 시험점수 - num  3.61 3.67 4 3.19 2.93 3 2.98 3.08 3.39 3.92 ...
#$ rank : 학교등급 - int  3 3 1 4 4 2 1 2 3 2 ...

# 1. data set 구성 
idx <- sample(1:nrow(admit), nrow(admit)*0.7)
train_admit <- admit[idx, ]
test_admin <- admit[-idx, ]

# 2. model 생성 
model <- glm(admit ~ ., data = train_admit, family = 'binomial')
model

# 3. predict 생성 
y_pred <- predict(model, newdata=test_admin, type="response")
cpred <- ifelse(y_pred>=0.5, 1, 0)

# 4. 모델 평가(분류정확도) : 혼돈 matrix(교차분할표) 이용/ROC Curve 이용
y_true <- test_admin$admit

tab<-table(y_true, cpred)
#        cpred
# y_true  0  1
#      0 79  5
#      1 30  6

acc <- (tab[1,1]+tab[2,2])/nrow(test_admin)  # 0.7083333
# [해석] 약 70% 분류 정확도를 가진다.
no_acc <- (tab[1,2]+tab[2,1])/nrow(test_admin) # 0.2916667

no <- tab[1,1]/(tab[1,1]+tab[1,2])  # 0.9404762 
recall <- tab[2,2]/(tab[2,1]+tab[2,2]) # 0.1666667

precision <- tab[2,2]/(tab[1,2]+tab[2,2])

F1_score =2*((recall*precision)/(recall+precision))
F1_score 



pr <- prediction(y_pred, test$admit)
prf <- performance(pr, measure = "tpr", x.measure = "fpr")
plot(prf)

