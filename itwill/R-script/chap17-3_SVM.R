# chap17-3_SVM

##################################################
#Support Vector Machine 
##################################################
# SVM 알고리즘 - 두 범주를 직선으로 분류(이진분류) 
# 선형분리 - 2개의 집합을 직선으로 분리(초평면 분리) 
# 초평면(Separating Hyperplane) : 2차원 이상 공간에서 평면 
# 가상의 직선을 중심으로 거리를 계산하여 직사각형 형태로 영역 확장
# -> 가장 가까운 점이 만날때 까지 영역  확장 

# 바이오인포매틱스의 유전자 데이터 분류 
# 용도 : 인간의 얼굴, 문자, 숫자 인식(이미지 데이터 패턴 인식) 
# 예) 스캐너로 스캔된 문서 이미지를 문자로 인식 


###############################################
####### e1071 패키지 
###############################################
# 관련 패키지(e1071, kernlab, klaR 등) 4개 중 e1071 가장 많이 사용함 

library(e1071)  

# 1. SVM 기본 개념 익히기 - Support Vector, Margin
df = data.frame(
  x1 = c(1,2,1,2,4,5,6),
  x2 = c(8,7,5,6,1,3,2),
  y=factor(c(1,1,1,1,0,0,0))
)
df


# 2. svm 모델 생성 
# 형식) svm(y ~ x, data, type, kernel) 
?svm
model_svm = svm(y ~ ., data = df, na.action =na.omit)
model_svm

# default 속성 :  kernel="radial"
# kernel : 비선형(non linear) 관계를 선형적(linear)으로 변환하는 역할 
# kernel 종류 : linear, polynomial, radial, sigmoid
# cost = 1 : 오분류 조절 속성(값이 큰 경우 -> 오분류 감소, 과적합 증가)
# gamma = if (is.vector(x)) 1 else 1 / ncol(x) : 결정경계 모양 조절 속성 
# gamma = 1/(x변수 개수) = 1/2=0.5 (값이 큰 경우 -> 공간이 작아지고 오분류 감소)

# Call:
# svm(formula = y ~ ., data = df, na.action = na.omit)
# Parameters:
# SVM-Type:  C-classification   ---범주형
# SVM-Kernel:  radial 
# cost:  1  ---오분류
# Number of Support Vectors:  6


# svm 모델 시각화 
par(mfrow=c(1,1))
plot(df$x1, df$x2, col=df$y)
#@@1
X11()
plot(model_svm, df) # 분류 Factor levels에 의해서 2개 분류 
#@@2

pred <- predict(model_svm, df)
pred
# 1 2 3 4 5 6 7   --- index
# 1 1 1 1 0 0 0   --- 예측치
# Levels: 0 1


# 3. kernel="linear" 변경 : 선형 svm
model_svm2 = svm(y~., data=df,  kernel="linear")
model_svm2
# Call:
# svm(formula = y ~ ., data = df, kernel = "linear") 
# Parameters:
#   SVM-Type:  C-classification 
# SVM-Kernel:  linear 
# cost:  1  --- 오분류 조절 속성(선형분류(linear) 일때 cost =1)
# Number of Support Vectors:  2

summary(model_svm2)
#@@3

predict(model_svm2, df)
# 1 2 3 4 5 6 7 
# 1 1 1 1 0 0 0 
# Levels: 0 1


############################
# iris 데이터 실습 
############################

# 1. 데이터셋 생성 
data(iris)
set.seed(415) # random 결과를 동일하게 지
idx = sample(1:nrow(iris), 0.7*nrow(iris))
training = iris[idx, ]
testing = iris[-idx, ]
training
testing
dim(training) # 105
dim(testing) # 45


# 2. 분류모델 생성 : kenel 생략(radial)=> 비선형 svm
model_svm = svm(Species ~ ., data = training) # na.action =na.omit
summary(model_svm)
#@@4

# 선형 svm
model_svm2 = svm(Species ~ ., data = training,
                kernel='linear') # na.action =na.omit
summary(model_svm2)

# 3. 분류모델 성능 평가(testing set 적용 예측값 생성)  
pred <- predict(model_svm, testing)

pred2 <- predict(model_svm2, testing)

# 혼돈 matrix 작성 
table(pred, testing$Species)
# pred         setosa versicolor virginica
# setosa         13          0         0
# versicolor      0         17         3  ---3개 오분류
# virginica       0          0        12

# 분류정확도
42/45 # 0.9333333

table(pred2, testing$Species)
# pred2        setosa versicolor virginica
# setosa         13          0         0
# versicolor      0         16         1
# virginica       0          1        14

# 분류정확도
43/45 # 0.9555556

# <해석> 
# 선형분류(kernel=linear) 했을때 조금 더 효과적인 분석 방법이다.

#############################################
## svm model tuning : tune.svm()
#############################################
# - tuning : 가장 최적의 속성값을 찾아서 최적의 model 생성

# 10^-3 ~ 10^3
params <- c(0.001, 0.01, 0.1, 1, 10, 100, 1000) 
length(params)

tuning <- tune.svm(Species ~ ., data = training,
         gamma=params, cost = params)
tuning
# Parameter tuning of ‘svm’:
# - sampling method: 10-fold cross validation 
# - best parameters:
# gamma cost
# 0.01 1000
# - best performance: 0.02909091 

best_model = svm(Species ~ ., data = training,
                 gamma=0.01, cost=1000)

best_pred = predict(best_model, testing)

table(best_pred, testing$Species)
# best_pred    setosa versicolor virginica
# setosa         13          0         0
# versicolor      0         16         0
# virginica       0          1        15

44/45 # 0.9777778 분류 정확도



#-----------------------------------------------------------------

##################################################
# Support Vector Machine 문제 : spamfiltering
##################################################
# 단계1. 실습 데이터 가져오기
load(file.choose()) # sms_data_total.RData
ls() #"test_sms",  "train_sms" 객체 올라왔는지 확인

# 단계2. 데이터 탐색 
dim(train_sms) # train 데이터 : 4180   74
dim(test_sms) # test 데이터 :  1394   74
names(train_sms)
table(train_sms$type) # sms 메시지 유형 
table(test_sms$type)

# 단계3. 분류모델 생성 : 기본 파라미터 사용 
model_sms <- svm(type ~ ., data = train_sms)
model_sms
summary(model_sms)

# 단계4. 분류모델 평가 : test_sms
pred <- predict(model_sms, test_sms)


# 단계5. 분류정확도  : table()
tab <- table(pred, test_sms$type)
# pred    ham spam
#   ham  1187  178
#   spam    1   28
acc<- (tab[1,1]+tab[2,2])/sum(tab)
acc # 0.8715925

# 단계6. 분류모델 수정 : linear kernel 방식 적용(radial과 linear 방식 비교) 
model_sms2 <- svm(type ~ ., data = train_sms, kernel='linear')

pred2 <- predict(model_sms2, test_sms)

tab2 <- table(pred2, test_sms$type)
# pred2   ham spam
#   ham  1170  112
#   spam   18   94

acc2 <- (tab2[1,1] + tab2[2,2])/sum(tab2)
acc2 # 0.9067432
# <해석> 비선형 분류정확도 87%, 선형 분류정확도 91%
# 선형 분류 모델이 좀더 효과적인 분석 방법이다.


#######################################
### 스캔된 이미지 문자 인식 
#######################################
# 1. 파일 가져오기 
letterdata = read.csv(file.choose())	#letterdata.csv
str(letterdata) # 'data.frame':	20000 obs. of  17 variables:
# y : letter, x : 나머지 16

# 2. 데이터 셋 생성 
set.seed(415)
idx = sample(1:nrow(letterdata), 0.7*nrow(letterdata))
training_letter = letterdata[idx, ]
testing_letter  = letterdata[-idx, ]

# 3. NA 제거 
training_letter2 = na.omit(training_letter)
testing_letter2 = na.omit(testing_letter)

# 4. 분류모델 생성 : 비선형 svm
model_letter <- svm(letter~., data = training_letter2)

# 5. 분류모델 평가 
pred_letter <- predict(model_letter, testing_letter2)

# 혼돈 matrix 
table(pred_letter, testing_letter2$letter)
#@@5

# 범주가 맣은 경우 관계식을 이용해서 분류 정확도 구함.
result <- (pred_letter == testing_letter2$letter)
table(result)
# FALSE  TRUE 
# 319  5681 

prop.table(table(result))
# result
# FALSE       TRUE 
# 0.05316667 0.94683333
