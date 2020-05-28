##########################
## 제17-3장 SVM 연습문제 
##########################

# 문1) 기상데이터를 다음과 같이 SVM에 적용하여 분류하시오. 
# 조건1> 포물라 적용 : RainTomorrow ~ .  
# 조건2> kernel='radial', kernel='linear' 각 model 생성 및 평가 비교 

# 1. 파일 가져오기 
weatherAUS = read.csv(file.choose()) #weatherAUS.csv
weatherAUS = weatherAUS[ ,c(-1,-2, -22, -23)] # 칼럼 제외 
str(weatherAUS) # 'data.frame':	36881 obs. of  20 variables:

# 2. 데이터 셋 생성 
set.seed(415)
idx = sample(1:nrow(weatherAUS), 0.7*nrow(weatherAUS))
training_w = weatherAUS[idx, ]
testing_w  = weatherAUS[-idx, ]

dim(training_w)
dim(testing_w)

training_w1<- na.omit(training_w)
testing_w1 <- na.omit(testing_w)

# 3. 분류모델 생성 : kernel='radial', kernel='linear' 
model_w <- svm(RainTomorrow~., data = training_w1)

model_w2 <- svm(RainTomorrow~., data = training_w1, kernel='linear')


# 4. 분류모델 평가 
pred_w <- predict(model_w, testing_w1)

pred_w2 <- predict(model_w2, testing_w1)

tab_w <- table(pred_w, testing_w1$RainTomorrow)
tab_w
# pred_w   No  Yes
#    No  3894  601
#   Yes  179  619
acc_w <- (tab_w[1,1]+tab_w[2,2])/sum(tab_w) 
acc_w # 0.8526356


tab_w2 <- table(pred_w2, testing_w1$RainTomorrow)
tab_w2

acc_w2 <- (tab_w2[1,1]+tab_w2[2,2])/sum(tab_w2) 
acc_w2 #0.8454563


# 문2) 문1에서 생성한 모델을 tuning하여 최적의 모델을 생성하시오.
a<-c(0.001, 0.01, 0.1, 1, 10, 100, 1000)
tuning_w <- tune.svm(RainTomorrow~., data = training_w1,
                     gamma = a, cost = a)
tuning_w


tuning_w2 <- tune.svm(RainTomorrow~., data = training_w1, kernel='linear',
                     gamma = a, cost = a)
tuning_w2
