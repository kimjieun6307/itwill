################################
## 제16-3장 XGBboost 연습문제 
################################

# 01. UniversalBank.csv 데이터셋을 이용하여 다음과 같이 XGBoost에 적용하여 분류하시오. 
# 조건1> 포물라 : formula <- Personal.Loan ~.
# 조건2> 모델 성능 평가
# 조건3> 중요변수 보기

# 대출 수락 or 거절 prediction
setwd("c:/ITWILL/2_Rwork/Part-IV")
Data = read.csv('UniversalBank.csv',  stringsAsFactors = F)
str(Data) # 'data.frame':	5000 obs. of  14 variables:
Data = Data[c(-1, -5)] # 1, 5번 칼럼 제외 


# Personal.Loan -> y변수(대출여부) 0: 거절, 1: 허락
str(Data) # 'data.frame':	5000 obs. of  12 variables:

# 1. data set 생성 
idx <- sample(nrow(Data), nrow(Data)*0.7)
train <- Data[idx, ]
test <- Data[-idx, ]
dim(train) # 3500   12
dim(test) # 1500  12

# 2. xgb.DMatrix 생성 : data(x):matrix, label(y):vecor 
train_mat <- as.matrix(train[-8]) # matrix
train_mat[1,]

# y변수 : vector 
train_y <- train$Personal.Loan
table(train_y)
# train_y
#    0    1 
# 3165  335 

# 3. model 생성 : xgboost matrix 객체 이용   
dtrain <- xgb.DMatrix(data=train_mat, label=train_y)

model <- xgboost(data = dtrain, max_depth = 2, eta = 1, nthread = 2, nrounds = 2, objective = "binary:logistic", verbose = 0)

# 4. prediction 
test_mat <- as.matrix(test[-8])
test_y <- test$Personal.Loan

pred<- predict(model, test_mat)

# 5. cut off 적용 = 0.5
y_pred <- ifelse(pred >= 0.5, 1, 0)
table(y_pred)
# y_pred
#    0    1 
# 1363  137 

# 6. confusion matrix
table(test_y)
# test_y
#    0    1 
# 1355  145

tab <- table(test_y, y_pred)
tab
#          y_pred
# test_y    0    1
#      0 1342   13
#      1   21  124

# 7. 모델 성능평가 : Accuracy
acc <- (tab[1,1]+ tab[2,2])/sum(tab)
acc # 0.9773333
# <해석> 약 97%의 분류정확율

# 8. 중요변수 보기(model 비교) 
import <- xgb.importance(colnames(train_mat), model = model)
#      Feature       Gain
# 1: Education 0.38907105 >> 교육수준
# 2:    Income 0.38444142 >> 수입
# 3:    Family 0.14533065 >> 가족수
# 4:     CCAvg 0.08115688 >> 평균 신용카드
xgb.plot.importance(importance_matrix = import)

# <해석> 중요변수 : Education, Income, Family, CCAvg