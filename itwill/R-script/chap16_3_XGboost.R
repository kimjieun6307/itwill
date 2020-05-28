# chap16_3_XGboost

# xgboost vs randomForest
# - xgboost : boosting 방식 
# - randomForest : bagging 방식 

# 1. package install
install.packages("xgboost")
library(xgboost)
library(help="xgboost")
# 인덱스:
# agaricus.test     Test part from Mushroom Data Set
# agaricus.train    Training part from Mushroom Data Set
#<참고> 실습용 data set

# 2. dataset load/search
data(agaricus.train)
data(agaricus.test)

train <- agaricus.train
test <- agaricus.test

str(train)
#List of 2  ---list 자료구조 key 2개(data, label)
# $ data : 6 slots --- x변수:2차원(matrix)[6513  126]
#         (@ i @ p @ Dim  @ Dimnames @ x @ factors) 
# $ label: num [1:6513] 1 0 0 ... : 1차원(vector) --- y변수

train$data@Dim # 6513  126  : 2차원(matrix)
# <참고> class -> object
# java, python : object.member
# R : object@member(slots) 
# R은 변수명에 '.' 을 쓰기때문에 객체에서 멤버를 호출할 때 '@' 사용함. 

train$data
#@@1
train$label
#@@2
table(train$label)
# 0    1 
# 3373 3140 


str(test)
# $ data : x변수 - 2차원(matrix)[1611  126]
# $ label: y변수 - 1차원(vector) num [1:1611]


# 3. xgboost matrix 생성 : 객체 정보 확인  
# xgb.DMatrix(data=x, label=y)
dtrain <- xgb.DMatrix(data = train$data, label = train$label) # x:data, y:label
dtrain 

?xgboost
#We will train decision tree model using the following parameters:

# •objective = "binary:logistic": we will train a binary classification model ;
# "binary:logistic" : y변수 이항 

# •max_depth = 2: the trees won't be deep, because our case is very simple ;
# tree 구조가 간단한 경우 : 2

# •nthread = 2: the number of cpu threads we are going to use;
# cpu 사용 수 : 2 (하드웨어가 받침이 될때 늘릴수 있음)

# •nrounds = 2: there will be two passes on the data, the second one will enhance the model by further reducing the difference between ground truth and prediction.
# 실제값과 예측값의 차이를 줄이기 위한 반복학습 횟수 

# •eta = 1 : eta control the learning rate 
# 학습률을 제어하는 변수(Default: 0.3) 
# 숫자가 낮을 수록 모델의 복잡도가 높아지고, 컴퓨팅 파워가 더많이 소요 <-> 1이면 속도 빠름 
# 부스팅 과정을보다 일반화하여 오버 피팅을 방지하는 데 사용

# •verbose = 0 : no message
# 0이면 no message, 1이면 성능에 대한 정보 인쇄, 2이면 몇 가지 추가 정보 인쇄

# 4. model 생성 
#: xgboost matrix 객체 이용(xgb.DMatrix()->dtrain 변수명으로 만듬)   
xgb_model <- xgboost(data = dtrain, max_depth = 2, eta = 1, nthread = 2, nrounds = 2, objective = "binary:logistic", verbose = 0)

# 5.  학습된 model의 변수(feature) 중요도/영향력 보기 
import <- xgb.importance(colnames(train$data), model = xgb_model)
import
#                    Feature       Gain     Cover Frequency
# 1:               odor=none 0.67615471 0.4978746       0.4
# 2:         stalk-root=club 0.17135375 0.1920543       0.2
# 3:       stalk-root=rooted 0.12317236 0.1638750       0.2
# 4: spore-print-color=green 0.02931918 0.1461960       0.2
# <해석> Gain 값을 통해 중요변수 확인가능 : 가장 중요 0.676 -> odor=none

colnames(train$data)
#@@3

xgb.plot.importance(importance_matrix = import)
#@@4

# 6. 예측치
pred <- predict(xgb_model, test$data)
range(pred) # 0.01072847 0.92392391

y_pred <- ifelse(pred >=0.5, 1, 0)
y_ture <- test$label
table(y_ture)
# 0   1 
# 835 776 

tab <- table(y_ture, y_pred)
tab
#         y_pred
# y_ture   0   1
#      0 813  22
#      1  13 763

# 7. 모델 평가
# 1) 분류정확도
acc <- (tab[1,1] + tab[2,2])/sum(tab)
cat('분류정확도 = ', acc)
# 분류정확도 =  0.9782744 : 1에 가까울 수록 좋은 모델

# 2) 평균 오차
# as.numeric() : T/F -> 숫자형 변환(1,0)
mean_err <- mean(as.numeric(pred>=0.5) != y_ture)
cat('평균 오차 = ', mean_err)
# 평균 오차 =  0.02172564 : 0에 가까울 수록 좋은 모델


# 8. model save & load
# 하나의 모델을 파일로 저장

# 1) model file save
setwd("c:/ITWILL/2_Rwork/output")
xgb.save(xgb_model, 'xgboost.model') # (obj, 'file')
#@@5

# 메모리 지우기
rm(list = ls())
#@@6

# 2) model load(memory loading)
xgb_model2 <- xgb.load('xgboost.model')
#@@7

pred2 <- predict(xgb_model2, test$data)
range(pred2) # 0.01072847 0.92392391


##################################################
## iris dataset : y 이항분류 (3항인데 2항으로 변경해서)
###########################################
iris_df <- iris   # 복제본

# 1. y변수 -> binary (Species : num)
iris_df$Species <- ifelse(iris_df$Species =='setosa', 0,1)
str(iris_df)
# $ Species     : num  >> 변경 확인

# 2. dataset 생성
idx <- sample(nrow(iris_df), nrow(iris_df)*0.7)
train <- iris_df[idx,]
test <- iris_df[-idx,]

# ★< x : matrix , y : vector >★
train_x <- train[,-5]
train_y <- train$Species
dim(train_x) #  105   4
str(train_x) # 'data.frame':	105 obs. of  4 variables:
train_x <- as.matrix(train_x)    # train_x <- as.matrix(train[,-5])
str(train_x) # num [1:105, 1:4]  >> matrix
str(train_y) # num [1:105]   >> vector

# 3. DMatrix 생성 
dtrain <- xgb.DMatrix(data = train_x, label = train_y) # x:data, y:label
dtrain

# 4. xgboost model 생성
xgb_iris_model <- xgboost(data = dtrain, max_depth = 2, eta = 1, nthread = 2, nrounds = 2, objective = "binary:logistic", verbose = 0)
xgb_iris_model

# 5.  학습된 model의 변수(feature) 중요도/영향력 보기
import <- xgb.importance(colnames(train_x), model = xgb_iris_model)
import
#         Feature Gain Cover Frequency
# 1: Petal.Length    1     1         1
#<해석> 3개 x변수 중에 가장 중요한 변수는 Petal.Length 이다.

xgb.plot.importance(importance_matrix = import)

# 6. 예측치
# x : matrix , y : vector
test_x <- as.matrix(test[,-5])
test_y <- test$Species

pred <- predict(xgb_iris_model, test_x)
range(pred) # 0.06295418 0.94906563

y_pred <- ifelse(pred>=0.5 , 1, 0)

tab <- table(test_y, y_pred)
tab
#        y_pred
# test_y  0  1
#      0 19  0
#      1  0 26

acc <- (tab[1,1]+ tab[2,2]) / length(test_y)
acc # 1 >> 분류정확도 100%

##################################################
## iris dataset : y 다항분류 (3항)
##################################################

?xgboost
# objective 속성
# objective = "reg:squarederror" : y 연속형(default)
# objective = "binary:logistic" : y 이항분류
# objective = "multi:softmax", num_class= n : y 다항(n)분류 
# >> Class is represented by a number and should be from 0 to num_class - 1.
# 다항분류의 첫번째 class = 0 로 해야 함.



iris_df <- iris   # 복제본

# 1. y변수 -> multi (Species(3) : num 0~2)
table(iris_df$Species) #  setosa versicolor  virginica 
iris_df$Species <- ifelse(iris_df$Species =='setosa', 0,ifelse(iris_df$Species =='versicolor', 1, 2))
table(iris_df$Species) #  0  1  2 
str(iris_df) # Species     : num

# 2. data set
idx <- sample(nrow(iris_df),nrow(iris_df)*0.8)
train  <- iris_df[idx,]
test  <- iris_df[-idx,]

#. xgb.DMatrix 생성
train_x <- as.matrix(train[,-5])
train_y <- train$Species

dmatrix <- xgb.DMatrix(data = train_x, label = train_y)

# 4. xgboost 모델 생성(objective = "multi:softmax", num_class=3)
xgb_iris_model2 <- xgboost(data = dmatrix, max_depth = 2, eta = 0.5, nthread = 2, 
                           nrounds = 2, objective = "multi:softmax", num_class=3, verbose = 0)

xgb_iris_model2


# 5. prediction
test_x <- as.matrix(test[,-5])
test_y <- test$Species

pred <- predict(xgb_iris_model2, test_x)
pred

# cut off생략
tab <- table(test_y, pred)
acc <- (tab[1,1]+tab[2,2]+tab[3,3])/sum(tab)
acc # 1

mean_err <-mean(pred != test_y)
mean_err #  0

# 5.  학습된 model의 변수(feature) 중요도/영향력 보기
import <- xgb.importance(colnames(train_x), model = xgb_iris_model2)
import
#         Feature     Gain
# 1: Petal.Length 0.812848
# 2:  Petal.Width 0.187152

xgb.plot.importance(importance_matrix = import)

##################################################
## iris dataset : y 연속형
##################################################
# objective = "reg:squarederror" : y 연속형(default)

# 1. train / test
idx <- sample(nrow(iris), nrow(iris)*0.7)
train <- iris[idx,]
test <- iris[-idx,]


# 2. xgboost model 
# y : 1번 칼럼
# x : 2~4번 칼럼
train_x <- as.matrix(train[c(2:4)])
dim(train_x) # 105   3
train_y <- train$Sepal.Length

dmatrix <- xgb.DMatrix(data=train_x, label=train_y)
model <- xgboost(data = dmatrix,  max_depth = 2, nthread = 2, 
                 nrounds = 3, verbose = 0)
model
# evaluation_log:
# iter train_rmse
#   1   3.895070
#   2   2.766184
#   3   1.976959

import <- xgb.importance(colnames(train_x), model = model)
import
#        Feature Gain Cover Frequency
# 1: Petal.Length    1     1         1
xgb.plot.importance(importance_matrix = import)

test_x<- as.matrix(test[c(2:4)])
test_y <- test$Sepal.Length

pred <- predict(model, test_x)

err <- test_y - pred
mean(err**2) # 3.153356

cor(test_y, pred) # 0.8061224
