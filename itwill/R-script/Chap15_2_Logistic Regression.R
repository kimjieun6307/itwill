# Chap15_2_Logistic Regression

###############################################
# 15_2. 로지스틱 회귀분석(Logistic Regression) 
# - model <- glm(RainTomorrow ~ ., data = train, family = 'binomial')
# - pred <- predict(weater_model, newdata=test, type="response")  
###############################################

# 목적 : 일반 회귀분석과 동일하게 종속변수와 독립변수 간의 관계를 나타내어 
# 향후 예측 모델을 생성하는데 있다.

# 차이점 : 종속변수가 범주형 데이터를 대상으로 하며 입력 데이터가 주어졌을 때
# 해당 데이터의결과가 특정 분류로 나눠지기 때문에 분류분석 방법으로 분류된다.
# 유형 : 이항형(종속변수가 2개 범주-Yes/No), 다항형(종속변수가 3개 이상 범주-iris 꽃 종류)
# 다항형 로지스틱 회귀분석 : nnet, rpart 패키지 이용 
# a : 0.6,  b:0.3,  c:0.1 -> a 분류 

# 분야 : 의료, 통신, 기타 데이터마이닝

# 선형회귀분석 vs 로지스틱 회귀분석 
# 1. 로지스틱 회귀분석 결과는 0과 1로 나타난다.(이항형)
# 2. 정규분포 대신에 이항분포를 따른다.
# 3. 로직스틱 모형 적용 : 변수[-무한대, +무한대] -> 변수[0,1]사이에 있도록 하는 모형 
#    -> 로짓변환 : 출력범위를 [0,1]로 조정
# 4. 종속변수가 2개 이상인 경우 더미변수(dummy variable)로 변환하여 0과 1를 갖도록한다.
#    예) 혈액형 AB인 경우 -> [1,0,0,0] AB(1) -> A,B,O(0)


# 단계1. 데이터 가져오기
weather = read.csv("C:/ITWILL/2_Rwork/Part-IV/weather.csv", stringsAsFactors = F) 
# stringsAsFactors = F : (factor형으로 가져 오지 않고)순수한 문자형으로 가져오기
dim(weather)  # 366  15
head(weather)
str(weather) # 문자형은 x변수로 사용할 수 없음.
#@@9

# 불필요한 변수 제거 :  chr 칼럼, Date, RainToday 칼럼 제거 
weather_df <- weather[, c(-1, -6, -8, -14)]
str(weather_df)

# 더비변수 생성 : RainTomorrow 칼럼 -> 로지스틱 회귀분석 결과(0,1)에 맞게 "더미변수" 생성      
weather_df$RainTomorrow[weather_df$RainTomorrow=='Yes'] <- 1
weather_df$RainTomorrow[weather_df$RainTomorrow=='No'] <- 0
weather_df$RainTomorrow <- as.numeric(weather_df$RainTomorrow)
head(weather_df)

# y 빈도수
table(weather_df$RainTomorrow)
#   0   1 
# 300  66 

prop.table(table(weather_df$RainTomorrow))
#         0         1 
# 0.8196721 0.1803279 


#  단계2.  데이터 샘플링 sample(1:nrow(df), nrow(df)*0.7)
idx <- sample(1:nrow(weather_df), nrow(weather_df)*0.7)
train <- weather_df[idx, ]
test <- weather_df[-idx, ]


#  단계3.  로지스틱  회귀모델 생성 glm() : 학습데이터 train
weater_model <- glm(RainTomorrow ~ ., data = train, family = 'binomial') # family = 'binomial' : y의 변수는 이항(2개)이다.
weater_model 
summary(weater_model) 


# 단계4. 로지스틱  회귀모델 예측치 생성 predict() : 검정데이터 test
# newdata=test : 새로운 데이터 셋, type="response" : 0~1 확률값으로 예측
#(참고)
# type='response' : 0~1 확률 예측 -> sigmoid 함수(yes/no)  
# type='probs' : 0~1 확률 예측 -> softmax 함수(a, b, c) 

pred <- predict(weater_model, newdata=test, type="response")  
pred 
range(pred, na.rm = T)  #  0.001301264 0.983154799
summary(pred)
str(pred)


# cut off=0.5
cpred <- ifelse(pred>=0.5, 1, 0)
table(cpred)
#  0  1 
# 95 13 


y_true <- test$RainTomorrow

# 교차분할표
tab<-table(y_true, cpred)
#         cpred
# y_true    0  1
#      0   88  4    = 92
#      1    7  9    = 16

#@@2

# 단계 5 : 모델 평가

# 1) 정분류 : 분류정확도
acc <- (88+9)/nrow(test)
acc <- (tab[1,1]+tab[2,2])/nrow(test)
cat('accuracy = ', acc)
# accuracy =  0.8818182 : 분류정확도 88%

# 2) 오분류
no_acc <- (7+4)/nrow(test) 
no_acc <- (tab[1,2]+tab[2,1])/nrow(test)

# 3) 특이도(Specificity) : 실제값 No인 경우 No 예측 비율
no <- 88/(88+4) # 0.9565217
no <- tab[1,1]/(tab[1,1]+tab[1,2]) 

# 4) 재현율(Recall) = 민감도(Sensitivity) : 실제값 Yes인 경우 Yes 예측 비
yes <- 9/(7+9) # 0.5625  
recall <- tab[2,2]/(tab[2,1]+tab[2,2])
#[해석] 비가 올때의 예측율이 56%로 비가 안 올때(95%)보다 예측력이 떨어진다.

# 5) 정확률 : 예측치(yes) -> yes
precision <- 9/(88+9)    # 0.09278351
precision <- tab[2,2]/(tab[1,2]+tab[2,2])
#[해석] 


# 6) F1_score : 불균형 비율
F1_score =2*((recall*precision)/(recall+precision))
#[해석] 종합적으로 검토했을때 55% 예측률을 갖는다


#--------------------------------------------------------------
#- 샘플링 할때마다 값이 달라지니깐 수식화-
# 교차분할표/정분류/오분류/민감도/특이도
tab <- table(y_true, cpred)

acc <- (tab[1,1]+tab[2,2])/sum(tab)
no_acc <- (tab[1,2]+tab[2,1])/sum(tab)

no <- tab[1,1]/(tab[1,1]+tab[1,2]) 
recall <- tab[2,2]/(tab[2,1]+tab[2,2])

precision <- tab[2,2]/(tab[1,2]+tab[2,2])

F1_score =2*((recall*precision)/(recall+precision))



#-------------------------------------------------------------


### ROC Curve를 이용한 모형평가(분류정확도)  ####
# Receiver Operating Characteristic

install.packages("ROCR")
library(ROCR)

# ROCR 패키지 제공 함수 : prediction() -> performance
pr <- prediction(pred, test$RainTomorrow)
prf <- performance(pr, measure = "tpr", x.measure = "fpr")
plot(prf)

#@@1


##################################################################################
# 다항형 로지스틱 회귀분석 
# - nnet, rpart 패키지 이용
# model <- multinom(Species ~ ., data=train)

install.packages("nnet")
library(nnet)

idx <- sample(nrow(iris), nrow(iris)*0.7)
train <- iris[idx,]
test <- iris[-idx,]

# 활성함수 
# 이항 : sigmoid funcion : 0~1 확률값
# 다항 : softmax funcion : 0~1 확률값 (sum=1)
# y1=0.1, y2=0.2, y3=0.7  ---> 가장 큰 확률값을 갖는 값(y3)을 정답으로 예측하는 
names(iris)
model <- multinom(Species ~ ., data=train)
#@@3
# 100번 반복 학습
# 처음 오차 115.354290
# 최종 오차 2.158826
# weights:  18  --- 가중치(신경망을 기반으로 가중치 만들어짐)

names(model)
# [1] "n"             "nunits"       
# [3] "nconn"         "conn"         
# [5] "nsunits"       "decay"        
# [7] "entropy"       "softmax"      
# [9] "censored"      "value"        
# [11] "wts"           "convergence"  
# [13] "fitted.values" "residuals"    
# [15] "lev"           "call"         
# [17] "terms"         "weights"      
# [19] "deviance"      "rank"         
# [21] "lab"           "coefnames"    
# [23] "vcoefnames"    "xlevels"      
# [25] "edf"           "AIC"          

#▶ "fitted.values"
model$fitted.values
range(model$fitted.values)
# 6.365559e-86 1.000000e+00  :  0~1사이 확률값

str(model$fitted.values)
# num [1:105, 1:3] -> matrix

model$fitted.values[1,]
#       setosa   versicolor    virginica 
# 8.448062e-10 1.000000e+00 1.098859e-08   ++ = 1
#[해석] 가장 높은 확률인 "versicolor"으로 예측

train[1,]
#   Sepal.Length Sepal.Width Petal.Length Petal.Width    Species
#            6.9         3.1          4.9         1.5 versicolor
#[해석] 실제 관측치 "versicolor"

# <예측치> 
#(참고)
# type='response' : 0~1 확률 예측 -> sigmoid 함수(yes/no)  
# type='probs' : 0~1 확률 예측 -> softmax 함수(a, b, c) 

#비율 예측 
y_pred2 <- predict(model, test, type='probs')
y_pred2
y_pred2 <- ifelse(y_pred2[,1]>=0.5, 'setosa', ifelse(y_pred2[,2] >= 0.5, 'versicolor', 'virginica' ))


# 범주 예측 (type 생략)
y_pred <- predict(model, test)
y_pred
#  [1] setosa     setosa     setosa     setosa    
#  [5] setosa     setosa     setosa     setosa    
#  [9] setosa     setosa     setosa     versicolor
# [13] setosa     setosa     versicolor versicolor




# <관측치>
y_true <- test$Species
#  [1] setosa     setosa     setosa     setosa    
#  [5] setosa     setosa     setosa     setosa    
#  [9] setosa     setosa     setosa     setosa    
# [13] setosa     setosa     versicolor versicolor

# <교차 분할표>
tab <- table(y_true, y_pred)
#              y_pred
# y_true       setosa versicolor virginica
# setosa         13          1         0
# versicolor      0         17         0
# virginica       0          1        13

acc <- (tab[1,1]+tab[2,2]+tab[3,3])/nrow(test)
cat('분류정확도 = ', acc)
# 분류정확도 =  0.8545455
