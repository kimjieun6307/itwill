# chap16_2_RandomForest

#@@7
##################################################
#randomForest
##################################################
# 결정트리(Decision tree)에서 파생된 모델 
# 랜덤포레스트는 앙상블 학습기법을 사용한 모델
# 앙상블 학습 : 새로운 데이터에 대해서 여러 개의 Tree로 학습한 다음, 
# 학습 결과들을 종합해서 예측하는 모델(PPT 참고)
# DT보다 성능 향상, 과적합 문제를 해결


# 랜덤포레스트 구성방법(2가지)
# 1. 결정 트리를 만들 때 데이터의 일부만을 복원 추출하여 트리 생성 
#  -> 데이터 일부만을 사용해 포레스트 구성 
# 2. 트리의 자식 노드를 나눌때 일부 변수만 적용하여 노드 분류
#  -> 변수 일부만을 사용해 포레스트 구성 
# [해설] 위 2가지 방법을 혼용하여 랜덤하게 Tree(학습데이터)를 구성한다.

# 새로운 데이터 예측 방법
# - 여러 개의 결정트리가 내놓은 예측 결과를 투표방식(voting) 방식으로 선택 


install.packages('randomForest')
library(randomForest) # randomForest()함수 제공 

##############################################################################
# < 분류 트리>
data(iris)

# 1. 랜덤 포레스트 모델 생성 
# 형식) randomForest(y ~ x, data, ntree, mtry)
model = randomForest(Species~., data=iris)  # 기본 : ntree=500, mtry=2
model
# Number of trees: 500
# No. of variables tried at each split: 2
#@@8

#--------------------------------------------------------------------------
# node 분할에 사용하는 x변수 개수 : ncol(iris)-1 = 4
mtry <- sqrt(4) # 범주형 : 2
p <-14
mtrt <- 1/3*p  # 연속형 : 4~5

#------------------------------------------------------------------------
#
# 2. 파라미터 조정 300개의 Tree와 4개의 변수 적용 모델 생성 
model = randomForest(Species~., data=iris, 
                     ntree=300, mtry=4, na.action=na.omit ) # 결측치 제거
model


# 3. 최적의 파리미터(ntree, mtry) 찾기
# - 최적의 분류모델 생성을 위한 파라미터 찾기

ntree <- c(400, 500, 600)
mtry <- c(2:4)

# 2개 vector이용 data frame 생성 
param <- data.frame(n=ntree, m=mtry)
param

for(i in param$n){ # 400,500,600
  cat('ntree = ', i, '\n')
  for(j in param$m){ # 2,3,4
    cat('mtry = ', j, '\n')
    model = randomForest(Species~., data=iris, 
                         ntree=i, mtry=j, 
                         na.action=na.omit )    
    print(model)
  }
}


# 4. 중요 변수 생성  
model3 = randomForest(Species ~ ., data=iris, 
                      ntree=500, mtry=2, 
                      importance = T,
                      na.action=na.omit )
model3 

importance(model3)
# MeanDecreaseAccuracy : 분류정확도 개선에 기여하는 변수 (값이 클수록 기여도가 높다.)
# MeanDecreaseGini : 노드 불순도(불확실성) 개선에 기여하는 변수 (값이 클수록 기여도가 높다.)
# 두 값이 클수록 y에 미치는 영향이 크다.
#@@9

varImpPlot(model3)
#@@10

# y의 설명력을 높이기 위해선 x변수 선택이 중요한데 imprtance()함수를 이용해서 변수 선택할수 있음.

##################################################################
# < 회귀 트리>

library(MASS)

data("Boston")
str(Boston)
# 'data.frame':	506 obs. of  14 variables:
#crim : 도시 1인당 범죄율 
#zn : 25,000 평방피트를 초과하는 거주지역 비율
#indus : 비상업지역이 점유하고 있는 토지 비율  
#chas : 찰스강에 대한 더미변수(1:강의 경계 위치, 0:아닌 경우)
#nox : 10ppm 당 농축 일산화질소 
#rm : 주택 1가구당 평균 방의 개수 
#age : 1940년 이전에 건축된 소유주택 비율 
#dis : 5개 보스턴 직업센터까지의 접근성 지수  
#rad : 고속도로 접근성 지수 
#tax : 10,000 달러 당 재산세율 
#ptratio : 도시별 학생/교사 비율 
#black : 자치 도시별 흑인 비율 
#lstat : 하위계층 비율 
#medv : 소유 주택가격 중앙값 (단위 : $1,000)

# y변수 = medv

ntree <- 500
p <- 13 # y변수를 제외한 나머지 변수
mtry <- 1/3*p
mtry # 4.333 >> 4 또는 5개

boston_model <- randomForest(medv~., data=Boston, ntree=ntree, mtry=5, importance=T)
boston_model
# Type of random forest: regression ---> 회귀분석
# Number of trees: 500
# No. of variables tried at each split: 5
# Mean of squared residuals: 9.996474  ---> 10% 오차 (표준화 안되서 0.0999674와 같은 소수점 아님.)
# % Var explained: 88.16  ---> 88% 예측 

boston_model$importance
# %IncMSE IncNodePurity
# crim     8.4331931     2248.8746
# zn       0.3072124      152.3136
# indus    4.9704725     2186.9387
# chas     0.6202243      160.4461
# nox     10.5418808     2661.4418
# rm      37.7073980    13962.6045
# age      3.4420077     1000.1974
# dis      7.0257588     2376.9154
# rad      1.1671869      259.4393
# tax      3.3366158     1112.6147
# ptratio  6.1637693     2314.4076
# black    1.5280997      672.7815
# lstat   61.6849206    12796.3098

importance(boston_model)

varImpPlot(boston_model)
#@@11


names(boston_model)
# [1] "call"            "type"           
# [3] "predicted"       "mse"            
# [5] "rsq"             "oob.times"      
# [7] "importance"      "importanceSD"   
# [9] "localImportance" "proximity"      
# [11] "ntree"           "mtry"           
# [13] "forest"          "coefs"          
# [15] "y"               "test"           
# [17] "inbag"           "terms"  

pred <- boston_model$predicted
ture <- boston_model$y

# 표준화(o)
err <- ture - pred
mse <- mean(err**2)
mse # 9.996474 (==  Mean of squared residuals: 9.996474) 
#<해석> 표준화 되어있지 않아서 모델 평가로 적합하지 않음. 
#       mse 값이 0에 가까울수록 적합한 모델임.

# 표준화(x)
cor(ture, pred) # 0.9412398 <해석> 94%의 예측력을 가진다고 볼수 있음.

# model 평가
# 분류tree : confusion matrix
# 회귀tree : MSE, cor


#####################################################################
### <분류 tree> titanic3.csv

titanic <- read.csv(file.choose())
str(titanic)

# y변수 : survived
# 제외 변수: c(3, 8, 10, 12, 13, 14)
titanic_data <- titanic[,-c(3, 8, 10, 12, 13, 14)]
dim(titanic_data) # 1309    8

titanic_data$survived <- factor(titanic_data$survived)
str(titanic_data$survived)
# Factor w/ 2 levels "0","1"

sqrt(7) # 2.645751 >>3 ---mtry
model <- randomForest(survived~., data=titanic_data, 
                      ntree=500, mtry=3, importance=T, na.action=na.omit)


model
# OOB estimate of  error rate: 19.9%
# Confusion matrix:
#     0   1 class.error
# 0 548  70   0.1132686
# 1 138 289   0.3231850

varImpPlot(model)
# 중요 변수 : sex, pclass, fare, age
#@@13

tab<-table(model$y, model$predicted)
tab
#     0   1
# 0 548  70
# 1 138 289
acc<-(tab[1,1]+tab[2,2])/sum(tab)
acc # 0.8009569

##############################################################
## entropy : 불확실성 척도
##############################################################
# - tree model에서 중요변수 선정 기준
# - entropy 값이 작으면 작을수록 불확실성 확률이 낮아진다.

# (ex) 동전 x1 : 앞면, x2 : 뒷면 >> 불확실성이 가장 높은 경우
# 1. 불확실성이 가장 높은 경우(0.5, 0.5)
x1 = 0.5
x2 = 0.5

e1 <- -x1* log2(x1) - x2*log2(x2)
exp(1) # 2.718282
e1 # 1

# 2. 불확실성이 낮은 경우 (0.9, 0.1)
x1 = 0.9
x2 = 0.1

e2 <- -x1* log2(x1) - x2*log2(x2)
e2 #  0.4689956

e2 <- -(x1* log2(x1) + x2*log2(x2)) # 같은 식






