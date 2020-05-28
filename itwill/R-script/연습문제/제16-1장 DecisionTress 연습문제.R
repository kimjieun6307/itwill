#####################################
## 제16-1장 DecisionTress 연습문제 
#####################################

library(rpart) # rpart() : 분류모델 생성
library(rpart.plot) # prp(), rpart.plot() : rpart 시각화
library(rattle) # fancyRpartPlot() : node 번호 시각화 

# 01. Spam 메시지 데이터 셋을 이용하여 DT 분류모델을 생성하고.
# 정분류율, 오분류율, 정확률을 구하시오. 

# 실습 데이터 가져오기
sms_data = read.csv(file.choose()) # sms_spam_tm.csv
dim(sms_data) # [1] 5558(row) 6824(word)
# y=(type), x=6823(word)
sms_data$sms_type # 정답 y변수

table(sms_data$sms_type)
# ham spam 
# 4811  747 

# 1. train과 test 데이터 셋 생성 (7:3)
idx <- sample(nrow(sms_data), nrow(sms_data)*0.7)
train <- sms_data[idx,]
test <- sms_data[-idx,]

# 2. model 생성 - train_sms
model <- rpart(sms_type~., data=train)
rpart.plot(model)

# 3. 예측치 생성 - test_sms
pred <- predict(model, test, type="class")
ture <- test$sms_type
  
tab <- table(ture, pred)
#         pred
# ture    ham spam
#  ham  1431   22
#  spam   73  142

# 4. 분류정확도 : 정분류율, 오분류율, 정확률, 재현율 
acc <- (tab[1,1]+tab[2,2])/sum(tab)
acc   # 0.9430456 : 정분류율 94%

no_acc <- (tab[1,2]+tab[2,1])/sum(tab)
no_acc   # 0.05695444 : 오분류율 6%

no <- tab[1,1]/(tab[1,1]+tab[1,2]) 
no    # 0.9848589 

recall <- tab[2,2]/(tab[2,1]+tab[2,2])
recall     # 0.6604651 : 재현율 66%

precision <- tab[2,2]/(tab[1,2]+tab[2,2])
precision    #  0.8658537  : 정확율 87%

F1_score =2*((recall*precision)/(recall+precision))
F1_score    #  0.7493404
#[해석] 종합적으로 분석했을때 75% 예측율을 갖는다.



###############################################################
# 02. weather 데이터를 이용하여 다음과 같은 단계별로 의사결정 트리 방식으로 분류분석을 수행하시오. 

# 조건1) y변수 : RainTomorrow, x변수 : Date(1)와 RainToday(14) 변수 제외한 나머지 변수로 분류모델 생성 
# 조건2) 모델의 시각화를 통해서 y에 가장 영향을 미치는 x변수 확인 
# 조건3) 비가 올 확률이 50% 이상이면 ‘Yes Rain’, 50% 미만이면 ‘No Rain’으로 범주화

# 단계1 : 데이터 가져오기
library(rpart) # model 생성 
library(rpart.plot) # 분류트리 시각화 
library(rattle)

weather = read.csv(file.choose(), header=TRUE) # weather.csv
str(weather)

# 단계2 : 데이터 샘플링
weather.df <- weather[, c(-1,-14)]
idx <- sample(1:nrow(weather.df), nrow(weather.df)*0.7)

weather_train <- weather.df[idx, ]
weather_test <- weather.df[-idx, ]

dim(weather_train) # 256 13
dim(weather_test) # 110 13



# 단계3 : 분류모델 생성
model <- rpart(RainTomorrow~., data=weather_train)
model
# 단계4 : 분류모델 시각화 - 중요변수 확인 
prp(model)
rpart.plot(model)
fancyRpartPlot(model)
# 중요변수 : Humidity

# 단계5 : 예측 확률 범주화('Yes Rain', 'No Rain') 
pred <- predict(model, weather_test, type='class')
pred

# 단계6 : 혼돈 matrix(교차분할표) 생성 및 분류 정확도 구하기
ture <- weather_test$RainTomorrow
tab <- table(ture,pred)
#       pred
# ture  No Yes
#   No  76  13
#   Yes 14   7

acc <- (tab[1,1]+tab[2,2])/nrow(weather_test)  
acc #  0.7545455
no_acc <- (tab[1,2]+tab[2,1])/nrow(weather_test)
no_acc #  0.2454545
no <- tab[1,1]/(tab[1,1]+tab[1,2])
no #0.8539326
recall <- tab[2,2]/(tab[2,1]+tab[2,2])
recall # 0.3333333
precision <- tab[2,2]/(tab[1,2]+tab[2,2])
precision #0.35
F1_score =2*((recall*precision)/(recall+precision))
F1_score  #0.3414634

####################################################
# 범주화
 pred1 <- predict(model, weather_test, type="response")
#Error in match.arg(type) : 
#  'arg' should be one of “vector”, “prob”, “class”, “matrix”

pred1 <- predict(model, weather_test) # 기본 type='prob'
str(pred1) 
# num [1:110, 1:2] 0.967 1 0.25 0.967 0.967 ...
# - attr(*, "dimnames")=List of 2
# ..$ : chr [1:110] "1" "2" "3" "6" ...
# ..$ : chr [1:2] "No" "Yes"

cpred <- ifelse(pred1[,1] >0.5, 'No Rain', ifelse(pred1[,2] >=0.5,'Yes Rain', 'error'))
cpred

#-------------------------------------------------------
cpred <- ifelse(pred1[,1]>=0.5, 'No Rain', 'Yes Rain')
cpred

ture <- weather_test$RainTomorrow
tab2 <- table(ture,cpred)
#      cpred
# ture  No Rain Yes Rain
#   No       76       13
#   Yes      14        7

cpred2 <- ifelse(pred1[,2]>=0.5, 'Yes Rain', 'No Rain')
cpred2
tab3 <- table(ture,cpred2)
#       cpred2
# ture  No Rain Yes Rain
#   No       76       13
#   Yes      14        7

###############################################################
a <- predict(model, weather_test, type="vector")
a
str(a)

