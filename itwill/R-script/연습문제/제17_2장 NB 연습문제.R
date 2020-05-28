##########################
## 제2-2장 NB 연습문제 
##########################


# 문) Spam 메시지 데이터 셋을 이용하여 NB 분류모델을 생성하고,
# 분류정확도와 F 측정치를 구하시오. 

# 실습 데이터 가져오기(TM에서 전처리한 데이터)
setwd("C:/ITWILL/2_Rwork/Part-IV")
sms_data <- read.csv('sms_spam_tm.csv')
#@@5
dim(sms_data) # [1] 5558(row) 6824(word) - 6157
str(sms_data)


# X 칼럼 제외 
sms_data.df <- sms_data[-1] # 행번호 제외 
head(sms_data.df)
str(sms_data.df) # 5558 obs. of  6823 variables:

sms_data.df$sms_type # y변수

# 1. train과 test 데이터 셋 생성 (7:3)
idx <- sample(nrow(sms_data.df), nrow(sms_data.df)*0.7)
train <- sms_data.df[idx, ]
test <- sms_data.df[-idx, ]
dim(train)
dim(test)

# 2. model 생성 - train_sms
model <- naiveBayes(sms_type ~., data = train)
model

# 3. 예측치 생성 - test_sms
pred <- predict(model, test)
pred


# 4. 정분류율(Accuracy)
tab <- table(test$sms_type, pred)
tab
#      pred
#       ham spam
# ham  1444   11
# spam   27  186

acc<-(tab[1,1]+tab[2,2])/sum(tab)
acc # 0.9772182

# 5. F measure(f1 score)
recall <- tab[2,2]/sum(tab[2,])
recall # 0.8732394

precision <- tab[2,2]/sum(tab[,2])
precision #  0.9441624

F1_score =2*((recall*precision)/(recall+precision))
F1_score  # 0.9073171
# 대략 91%의 정확도를 갖는다. 비교적 높은 정확도를 보여주는 모델임.


#########################################################################
# 실습 데이터 가져오기(TM에서 전처리한 데이터)
setwd("C:/ITWILL/2_Rwork/Part-IV")
sms_dtm_data <- read.csv('sms_dtm_df.csv')

dim(sms_dtm_data) 
str(sms_dtm_data)

# 1. train과 test 데이터 셋 생성 (7:3)
idx <-sample(nrow(sms_dtm_data), nrow(sms_dtm_data)*0.7)
train_dtm <- sms_dtm_data[idx,]
test_dtm <- sms_dtm_data[-idx,]

# 2. model 생성 - train_sms
model <- naiveBayes(sms_data.type ~., data=sms_dtm_data)

# 3. 예측치 생성 - test_sms
dtm_pred <- predict(model, test_dtm)

# 4. 정분류율(Accuracy)
tab <- table(test_dtm$sms_data.type, dtm_pred)
tab
#      dtm_pred
#       ham spam
# ham  1409   31
# spam   12  216

# 5. F measure(f1 score)
acc <- (tab[2,2]+tab[1,1])/sum(tab)
acc # 0.9742206
recall <- tab[2,2] / sum(tab[2,])
recall # 0.9473684
decision <- tab[2,2]/sum(tab[,2])
decision #  0.8744939
f1 <- ((recall*decision)/(recall+decision))*2
f1 # 0.9094737

