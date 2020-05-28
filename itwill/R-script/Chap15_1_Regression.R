# Chap15_1_Regression

######################################################
# 회귀분석(Regression Analysis)
######################################################
# - 특정 변수(독립변수:설명변수)가 다른 변수(종속변수:반응변수)에 
# 어떠한 영향을 미치는가(인과관계) 분석

###################################
# 1. 단순회귀분석 
# - "단순" : 독립변수와 종속변수가 1개인 경우

# 단순선형회귀 모델 생성  
# 형식) lm(formula= y ~ x 변수, data) 

setwd("C:/ITWILL/2_Rwork/Part-IV")
product <- read.csv("product.csv", header=TRUE)
head(product) # 친밀도 적절성 만족도(등간척도 - 5점 척도)

str(product) # 'data.frame':  264 obs. of  3 variables:
y = product$'제품_만족도' # 종속변수
x = product$'제품_적절성' # 독립변수
df <- data.frame(x, y)


# 회귀모델 생성 : lm(formula=, data=)
result.lm <- lm(formula=y ~ x, data=df)
result.lm # 회귀계수 (Intercept) : y절편 0.7789 , x : 기울기 0.7393
# Coefficients:
# (Intercept)            x  
#      0.7789       0.7393  

# 회귀방정식(y) = a.x + b (a:기울기, b:절편)
head(df)
#   x y
# 1 4 3
# 2 3 2
# 3 4 4
# 4 2 2
# 5 2 2
# 6 3 3

x <- 4 # 입력변수
y <- 3 # 정답
a <- 0.7393 # 기울기
b <- 0.7789 # 절편

# 회귀방정식 : y의 예측치
Y <- a*x +b
cat('Y의 예측치 =', Y)
# Y의 예측치 = 3.7361

err <- Y-y
cat('model error = ', err)
# model error =  0.7361

names(result.lm)
# [1] "coefficients"  "residuals"    
# [3] "effects"       "rank"         
# [5] "fitted.values" "assign"       
# [7] "qr"            "df.residual"  
# [9] "xlevels"       "call"         
# [11] "terms"         "model"

# "coefficients" : 회귀계수
# "residuals"  : 오차(잔차)
# "fitted.values" : 적합치(예측치)

result.lm$coefficients
# (Intercept)           x 
#   0.7788583   0.7392762 

result.lm$residuals #각각의 관측치 별에 대한 오차
# 1           2           3 
# -0.73596305 -0.99668687  0.26403695 
# 4           5           6 
# -0.25741069 -0.25741069  0.00331313 
# 7           8           9 
# 0.26403695 -0.25741069  0.74258931 

#>> 1. -0.7359630  = (model error =  0.7361) : 모델값과 공식값 동일

result.lm$fitted.values
# 1        2        3        4        5 
# 3.735963 2.996687 3.735963 2.257411 2.257411 
# 6        7        8        9       10 
# 2.996687 3.735963 2.257411 2.257411 2.257411

#>> 1. 3.735963 = (Y의 예측치 = 3.7361) : 모델값과 공식값 동일


# 회귀모델 예측 : predict(model, data.frame(x= ))
# x데이터 : model 생성시 동일한 변수명으로 해야 함.
predict(result.lm, data.frame(x=5) ) 
# 4.475239  --y의 예측값

# (2) 선형회귀 분석 결과 보기 
# : x -> y 인과관계가 있는지 유의미한지 분석
# result.lm <- lm(formula=y ~ x, data=df)
summary(result.lm)
#@@1
# <회귀모델 해석 순서>
# 1. F-statistic: p-value < 0.05 : 통계적으로 유의하다
# 2. Adjusted R-squared:  0.5865  : (피어슨의 R) 설명력(예측력) 1에 가까울수록 100% 예측
# 3. x의 유의성 검정 : t value(-1.96~+1.96),  Pr(>|t|) < 0.05 
# : Pr(>|t|)가 0에 가까울수록 x는 유의하다.

cor(df)
#           x         y
# x 1.0000000 0.7668527
# y 0.7668527 1.0000000
r <- 0.7668527
r_squared <- r**2
r_squared # 0.5880631 = Adjusted R-squared:  0.5865


#[결과1]
# 음료수 제품의 당도와 가격수준을 결정하는 제품 적절성은 제품 만족도에 
# 정(正)의 영향을 미칠 것이라는 연구가설을 검정한 결과 
# 검정통계량 t=19.340, p=0.05미만으로 통계적 유의수준 하에서 
# 영향을 미치는 것으로 나타났기 때문에 연구가설을 채택한다.

#[결과2]
# 회귀모형은 상관계수 R=.767로 두 변수 간에 다소 높은 상관관계를 나타내며, 
# R2=.587로 제품 적절성 변수가 제품 만족도를 58.7% 설명하고 있다. 
# 또한 회귀모형의 적합성은 F=374.020(p-value : < 2.2e-16)으로 회귀선이 모형에 적합하다고 볼 수 있다.



# (3) 단순선형회귀 시각화
# x,y 산점도 그리기 
plot(formula=y ~ x, data=df)
#@@2
# 회귀분석
result.lm <- lm(formula=y ~ x, data=df)
# 회귀선 
abline(result.lm, col='red')
#@@3

plot(formula=y ~ x, data=df, xlim=c(0,5), ylim=c(0,5))
#@@4

result.lm$coefficients
# (Intercept)           x 
#   0.7788583   0.7392762 

y <- product$'제품_만족도'
x <- product$'제품_적절성'

# x 기울기 = Covxy / Sxx
Covxy = mean((x-mean(x))*(y-mean(y)))
Sxx = mean((x-mean(x))**2)
a <- Covxy / Sxx
a # 0.7392762 

# y의 절편
b <- mean(y) - (a* mean(x))
b # 0.7788583

##########################################################
# 2. 다중회귀분석
# - 여러 개의 독립변수 -> 종속변수에 미치는 영향 분석
# - 가설 : 음료수 제품의 적절성(x1)과 친밀도(x2)는 제품 만족도(y)에 정의 영향을 미친다.

product <- read.csv("product.csv", header=TRUE)
head(product) # 친밀도 적절성 만족도(등간척도 - 5점 척도)


#(1) 적절성 + 친밀도 -> 만족도  
y = product$'제품_만족도' # 종속변수
x1 = product$'제품_친밀도' # 독립변수1
x2 = product$'제품_적절성' # 독립변수2

df <- data.frame(x1, x2, y)

# ● 다중선형회귀 모델 생성  
# 형식) lm(formula=y ~ ., data=df)
result.lm <- lm(formula=y ~ x1 + x2, data=df)


# 계수 확인 
result.lm
# Coefficients:
#   (Intercept)           x1           x2  
#       0.66731      0.09593      0.68522  

b <- 0.66731
a1 <- 0.09593
a2 <- 0.68522

head(df)
#   x1 x2 y
# 1  3  4 3
# 2  3  3 2
# 3  4  4 4
X1 <- 3
X2 <- 4

y = (a1*X1 + a2*X2) + b
y  # 3.69598 --예측값
Y = 3  # --정답
err = Y-y
abs(err) # 절대값

# 분석결과 확인
summary(result.lm)
# F-statistic: p-value: < 2.2e-16 < 0.05 : 유의하다
# Adjusted R-squared:  0.5945 : 59% 정도의 예측력
#         t value Pr(>|t|)    
#   x1      2.478   0.0138 *   -> 친밀도 < 0.05 : y에 (적은)영향을 미친다
#   x2     15.684  < 2e-16 *** -> 적절성 < 0.05 : y에 (많은)영향을 미친다


#-----------------------------------------------------------
install.packages('car') # 다중공선성 문제 확인
library(car)

Prestige # 'car'에서 제공하는 dataset : 102개 직업군 평판 
str(Prestige)
# 'data.frame':	102 obs. of  6 variables:
# $ education: num  13.1 12.3 12.8 11.4 14.6 ...
# $ income   : int  12351 25879 9271 8865 8403 11030 8258 14163 11377 11023 ...
# $ women    : num  11.16 4.02 15.7 9.11 11.68 ...
# $ prestige : num  68.8 69.1 63.4 56.8 73.5 77.6 72.6 78.1 73.1 68.8 ...
# $ census   : int  1113 1130 1171 1175 2111 2113 2133 2141 2143 2153 ...
# $ type     : Factor w/ 3 levels "bc","prof","wc": 2 2 2 2 2 2 2 2 2 2 ...

# X변수 : education(교육수준), women(여성비율), prestige(평판) 
# Y변수 : income(수입)

row.names(Prestige) # 102개의 직업군
# [1] "gov.administrators"       
# [2] "general.managers"         
# [3] "accountants"              
# [4] "purchasing.officers"      
# [5] "chemists"   
# ~[102]

df <- Prestige [ ,c(1:4)]
str(df)

# 회귀모델 만들기
model <- lm(formula = income ~ ., data = df)
model
# (Intercept)    education        women     prestige  
#      -253.8        177.2        -50.9        141.4  

summary(model)
# 1. p-value: < 2.2e-16 : 유의미한 수준에서 회귀모델은 유의하다.
# 2. Adjusted R-squared:  0.6323 : 설명력(예측력) 
# 2. education Pr(>|t|) 0.347 > 0.05 : 교육수준은 수입에 영향을 미치지 못한다.
#   여성비율과 평판은 매우 유의미한 수준에서 수입에 영향을 미친다.
#              Estimate Std. Error t value Pr(>|t|)    
# (Intercept) -253.850   1086.157  -0.234    0.816    
# education    177.199    187.632   0.944    0.347      (상관없음)
# women        -50.896      8.556  -5.948 4.19e-08 ***  (음의 상관)
# prestige     141.435     29.910   4.729 7.58e-06 ***  (양의 상관)

res <- model$residuals # 잔차(오차)=정답-예측치
summary(res)  # 표준화 됬는지 확인 >> 표준화 안되어 있음
#     Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
# -7715.3  -929.7  -231.2     0.0   689.7 14391.8 
length(res) # 102

# MSE(평균제곱오차) : 모델 평가 방법 
mse <- mean(res**2)
cat('MSE=', mse)
# MSE= 6369159 >> 잔차가 표준화 안되서 평가하기 적절하지 않음.
# 표준화 해서 MSE  구하면 0에 가까울수록 적합한 모델로 평가 할 수 있음.

mean(res) #  1.704083e-14

# 잔차 표준화
res_scale <- scale(res) # mean=0, sd=1
summary(res_scale)
# V1          
# Min.   :-3.04210  
# 1st Qu.:-0.36658  
# Median :-0.09116  
# Mean   : 0.00000  
# 3rd Qu.: 0.27194  
# Max.   : 5.67460  
shapiro.test(res) # p-value = 1.816e-11

# MSE(평균제곱오차) : 표준화 하여 모델 평가 방법 
mse <- mean(res_scale**2)
cat('MSE=', mse)
# MSE= 0.9901961 : 표준화 후 MSE >> 값이 작을수록 적합한 모델이라고 할 수 있다.

# 제곱 : 부로 절대값, 패널티
# 평균 : 전체 오차에 대한 평균

#############################################################
# 3. x변수 선택

new_data <- Prestige[, c(1:5)]
# 변수 : education(교육수준), women(여성비율), prestige(평판), census(직업수)
# Y변수 : income(수입)
dim(new_data) # 102   5

model2 <- lm(income ~., data=new_data)

library(MASS)
step <- stepAIC(model2, direction = 'both')
# Start:  AIC=1607.93 >> 작으면 작을수록 좋은 모델
# income ~ education + women + prestige + census
# ....
# Step:  AIC=1604.96 >> 가장 최소
# income ~ women + prestige >> 가장 최적의 변수 모형

model3 <- lm(income ~ women + prestige, data = new_data )
summary(model3)
# Adjusted R-squared:  0.6327
# 0.6323 vs 0.6327


#################################################
# 4. 다중공선성(Multicolinearity)
# - 독립변수 간의 강한 상관관계로 인해서 회귀분석의 결과를 신뢰할 수 없는 현상
# - 생년월일과 나이를 독립변수로 갖는 경우
# - 해결방안 : 강한 상관관계를 갖는 독립변수 제거

# (1) 다중공선성 문제 확인 : vif(model), sqrt(vip(model)) >2
library(car)
fit <- lm(formula=Sepal.Length ~ Sepal.Width+Petal.Length+Petal.Width, data=iris)
vif(fit)
# Sepal.Width Petal.Length  Petal.Width 
#    1.270815    15.097572    14.234335
# Petal.Length 변수와 Petal.Width 변수의 상관성이 높아보임.

sqrt(vif(fit))>2 
# Sepal.Width Petal.Length  Petal.Width 
#       FALSE         TRUE         TRUE
# root(VIF)가 2 이상인 것은 다중공선성 문제 의심 
# Petal.Length 변수와 Petal.Width 변수의 다중공선성 문제 의심 

# (2) iris 변수 간의 "상관계수" 구하기
cor(iris[,-5])   # 변수간의 상관계수 보기(Species 제외) 
#              Sepal.Length Sepal.Width Petal.Length Petal.Width
# Sepal.Length    1.0000000  -0.1175698    0.8717538   0.8179411
# Sepal.Width    -0.1175698   1.0000000   -0.4284401  -0.3661259
# Petal.Length    0.8717538  -0.4284401    1.0000000   0.9628654
# Petal.Width     0.8179411  -0.3661259    0.9628654   1.0000000
# Petal.Length 변수와 Petal.Width 변수의 상관계수 0.9628654로 1에 가까움(계수값 높음)
# x변수간 상관계수값이 높을 수도 있다. -> 해당 변수 제거(모형 수정) <- Petal.Width


# (3) 학습데이터와 검정데이터 분류
# sample(nrow(df), 0.7*nrow(df), replace = F)
nrow(iris) # 150
x <- sample(1:nrow(iris), 0.7*nrow(iris)) # 전체중 70%만 추출
train <- iris[x, ] # 학습데이터 추출
test <- iris[-x, ] # 검정데이터 추출
dim(train)  # 105   5 -> model 학습용
dim(test)   # 45  5 -> model 검정용


# (4) model 생성 : Petal.Width 변수를 제거한 후 회귀분석 
iris_model <- lm(formula=Sepal.Length ~ Sepal.Width + Petal.Length, data=train)
iris_model
summary(iris_model)
# p-value: < 2.2e-16 : 모델 유의함.
# Adjusted R-squared:  0.8455 >> 약 83%의 예측력
# Sepal.Width   0.57391    0.07729   7.425 3.51e-11 ***
# Petal.Length  0.46941    0.01972  23.800  < 2e-16 ***

# (5) model 예측치 : test set(x) -> y predict
y_pred <- predict(iris_model, test)
y_pred
length(y_pred) # 45

# (6) model 평가 : MSE, 상관계수 r
# MSE : 표준화 o
y_true <- test$Sepal.Length
ERROR <- y_true - y_pred
MSE <- mean(ERROR**2)
cat('MSE =', MSE) #MSE = 0.1054836

# 상관계수 r : 표준화 x
r <- cor(y_true, y_pred)
cat('r= ', r) 
# r=  0.9036857 : 93% 예측했다는 것 >> 적합한 모델임.

# 시각화 평가

plot(y_true, col='blue', type='l', label='y true')
points(y_pred, col='red', type = 'l', label='y pred')

# 범례 추가
legend("topleft", legend = c('y true', 'y pred'), col=c('blue', 'red'), pch = '-')

#@@8



##########################################
##  5. 선형회귀분석 잔차검정과 모형진단
##########################################

# 1. 변수 모델링  : x, y 변수 선정
# 2. 회귀모델 생성 : lm()
# 3. 모형의 잔차검정 
#   1) 잔차의 등분산성 검정 >> plot 1
#   2) 잔차의 정규성 검정 >> plot2
#   3) 잔차의 독립성(자기상관) 검정 
# 4. 다중공선성 검사 
# 5. 회귀모델 생성/ 평가 


names(iris)

# 1. 변수 모델링 y:Sepal.Length <- x:Sepal.Width, Petal.Length, Petal.Width
formula = Sepal.Length ~ Sepal.Width + Petal.Length + Petal.Width


# 2. 회귀모델 생성 
model <- lm(formula = formula,  data=iris)
model
summary(model)
names(model)


# 3. 모형의 잔차검정
plot(model)
#Hit <Return> to see next plot: 잔차 vs 적합값 -> 패턴없이 무작위 분포:등분산성 검정(포물선 분포 좋지않은 적합) 
#@@5
#Hit <Return> to see next plot: Normal Q-Q -> 정규분포 : 대각선이면 잔차의 정규성 
#@@6
#Hit <Return> to see next plot: 척도 vs 위치 -> 중심을 기준으로 고루 분포 
#Hit <Return> to see next plot: 잔차 vs 지렛대값 -> 중심을 기준으로 고루 분포 

# (1) 등분산성 검정 
plot(model, which =  1) 
#@@7
methods('plot') # plot()에서 제공되는 객체 보기 

# (2) 잔차 정규성 검정
attributes(model) # coefficients(계수), residuals(잔차), fitted.values(적합값)
res <- residuals(model) # 잔차 추출 
res <- model$residuals
shapiro.test(res) # 정규성 검정 - p-value = 0.9349 >= 0.05
# 귀무가설 : 정규성과 차이가 없다.(=같다)

# 정규성 시각화  
hist(res, freq = F) 
qqnorm(res)

# (3) 잔차의 독립성(자기상관 검정 : Durbin-Watson) 
install.packages('lmtest')
library(lmtest) # 자기상관 진단 패키지 설치 
dwtest(model) # 더빈 왓슨 값
# DW = 2.0604, p-value = 0.6013
# DW : 2~4 채택역, p-value >= 0.05 채택 : 잔차들 간의 관련이 없다. >> 독립적이다.

# 4. 다중공선성 검사 
library(car)
sqrt(vif(model)) > 2 # TRUE 
# Sepal.Width Petal.Length  Petal.Width 
# FALSE         TRUE         TRUE 
# (결론) Petal.Width 변수 제거

# 5. 모델 생성/평가 
formula = Sepal.Length ~ Sepal.Width + Petal.Length 
model <- lm(formula = formula,  data=iris)
summary(model) # 모델 평가


##################################################################
# 6. 범주형 변수 사용
# - 범주형(ex:gender)변수 -> 더미변수(0,1) 생성
# - 더미변수 : 기준을 '0' 으로 잡고 기준이 아닌 것은 '1'로 
# - 범주형 변수는 기울기에 영향 없음(y절편에만 영향 미침)
# - 범주형 범주가 n개이면 더미변수 수 : n-1
# ex) 혈액형(AB, A, B, O) : 3개 더미변수
#      x1, x2, x3
#    A  1   0   0
#    B  0   1   0 
#    o  0   0   1
#   AB  0   0   0 (base) : levels
# Factor : 범주형 -> 더미변수 자동으로 만들어 줌.  
# (참고:파이썬 같은 경우는 R처럼 자동으로 더미변수 만들어 주지 않음)


# 의료비 예측 : insurance.csv
insurance <- read.csv(file.choose())
str(insurance)
# 'data.frame':	1338 obs. of  7 variables:
# $ age     :나이 int  19 18 28 33 32 31 46 37 37 60 ...
# $ sex     :성별 Factor w/ 2 levels "female","male": 1 2 2 2 2 1 1 1 2 1 ...
# $ bmi     :비만도지구 num  27.9 33.8 33 22.7 28.9 ...
# $ children:자녀수 int  0 1 3 0 0 0 1 3 2 0 ...
# $ smoker  :흡연유무 Factor w/ 2 levels "no","yes": 2 1 1 1 1 1 1 1 1 1 ...
# $ region  :지역명 Factor w/ 4 levels "northeast","northwest",..: 4 3 3 2 2 3 3 2 1 2 ...
# $ charges :의료비(y) num 16885 1726 4449 21984 3867 ...

# 범주형 변수 : sex(성별/2), smoker(흡연유무/2), region(지역명/4)
# 기준(base) : level1(base)=0, level2=1

# 회귀모델 생성
insurance2 <- insurance[,-c(5:6)] # 흡연유무, 지역 제외
head(insurance2)

ins_model <- lm(charges ~ ., data=insurance2)
ins_model
# Coefficients:
# (Intercept)          age      sexmale          bmi     children  
#     -7460.0        241.3       1321.7        326.8        533.2  

# sexmale  1321.7
# female = 0,  male = 1  (알파벳 순에 의해 base 결정됨.)
# [해석] 여성에 비해서 남성의 의료비 증가 (1321원 증가)
# y = a.x + b
y_male = 1321.7*1 +(-7460.0)   # = -6138.3
y_female = 1321.7*0 +(-7460.0)   # = -7460

# ● Levels  base 변경
x <- c('male', 'female')
insurance2$sex <- factor(insurance2$sex, levels = x)
insurance2$sex
# Levels: male female  ---> base : male

ins_model <- lm(charges ~ ., data=insurance2)
ins_model
# Coefficients:
# (Intercept)      age    sexfemale        bmi     children  
#     -6138.2    241.3      -1321.7      326.8        533.2  

# sexfemale     -1321.7  
#[해석] 여성이 남성에 비해서 의료비 절감(-1321.7)

#------------------------------------------------------------------
# - 증명 -
male <- subset(insurance2, sex=='male')
female <- subset(insurance2, sex=='female')

mean(male$charges)     # 13956.75
mean(female$charges)    # 12569.58
mean(male$charges)-mean(female$charges)    # 1387.172
#-------------------------------------------------------------------

# ● dummy 변수 vs 절편 
# :범주형 변수는 y절편에만 영향 미침

insurance3 <- insurance[, -6]
head(insurance3)
#   age    sex    bmi children smoker   charges
# 1  19 female 27.900        0    yes 16884.924
# 2  18   male 33.770        1     no  1725.552
# 3  28   male 33.000        3     no  4449.462

ins_model2 <- lm(charges ~smoker, data=insurance3)
ins_model2
# (Intercept)    smokeryes  
#        8434        23616

# base : smokerno=0, smokeryes=1
#[해석] 흡연자가 비흡연자에 비해서 23616 의료비 증가

no <- subset(insurance3, smoker=='no')
mean(no$charges) # 8434.268   ---> y절편
yes <- subset(insurance3, smoker=='yes')
mean(yes$charges) # 32050.23

32050.23-8434-268    # 23348.23

#--------------------------------------------------------------

# < n개의 범주 >
# 4개 범주 -> 3개 더미 변수 생성
insurance4 <- insurance

ins_model3 <- lm(charges ~ region, data=insurance4)
ins_model3
# (Intercept)  regionnorthwest  regionsoutheast  regionsouthwest  
#     13406.4           -988.8           1329.0          -1059.4  
##    y 절편          x1                x2              x3 
## x0 : regionnortheast (base) ---절편으로 표현




