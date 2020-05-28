# chap16_1_DecisionTree


library(rpart) # rpart() : 분류모델 생성 
install.packages("rpart.plot")
library(rpart.plot) # prp(), rpart.plot() : rpart 시각화
install.packages('rattle')
library('rattle') # fancyRpartPlot() : node 번호 시각화 


# 단계1. 실습데이터 생성 
data(iris)
names(iris)
# [1] "Sepal.Length" "Sepal.Width"  "Petal.Length" "Petal.Width" 
# [5] "Species"
set.seed(415)
idx = sample(1:nrow(iris), 0.7*nrow(iris))
train = iris[idx, ]
test = iris[-idx, ]
dim(train) # 105 5
dim(test) # 45  5

table(train$Species)

# 단계2. 분류모델 생성 
# rpart(y변수 ~ x변수, data) , y:범주형 x:연속형
model = rpart(Species~., data=train) # iris의 꽃의 종류(Species) 분류 
model
#@@4

# <해석> - 분류 모델은 아래의 해석이 중요
# 1) root 105 68 setosa (0.35238095 0.31428571 0.33333333) 
#   root node : 전체크기(105개), 68(setosa 제외), 가장 많은 비율 label setosa(105-68=37개)

#  2) Petal.Length< 2.45 37  0 setosa (1.00000000 0.00000000 0.00000000) *
#    left node : 분류조건 -> 분류대상 37개, 오분류 0개 : 가장 많은 비율 label(setosa) 
#    (각 레이블에 대한 분류 비율)  * --단노드(자식 없음)

#  3) Petal.Length>=2.45 68 33 virginica (0.00000000 0.48529412 0.51470588)  
#    right node : 분류조건 -> 68(전체개수), 33(오분류) 
#    : 가장 많은 비율을 차지하는 레이블 "virginica"의 개수(68-33=35개)


# 분류모델 시각화 - rpart.plot 패키지 제공 
prp(model) # 간단한 시각화   
#@@5
#@@6
rpart.plot(model) # rpart 모델 tree 출력
#@@7
fancyRpartPlot(model) # node 번호 출력(rattle 패키지 제공)
#@@8

####################################################
## 가지치기(cp : cut prune)
###################################################
# 트리의 가지치기 : 과적합 문제 해결법
# cp : 0 ~ 1, default = 0.05
# 0으로 갈수록 트리 규모커짐, 오류율 감소, 과적합 증가
model$cptable
#           CP nsplit  rel error     xerror       xstd
# 1 0.5147059      0 1.00000000 1.11764706 0.06737554
# 2 0.4558824      1 0.48529412 0.57352941 0.07281162
# 3 0.0100000      2 0.02941176 0.02941176 0.02059824
# <해석> 3번이 가장 작은 cp값이다. 오류율(rel error) 가장 작다.
#       cp 0.01에서 과적합 발생하면 cp 0.45(2번)으로 조정





# 단계3. 분류모델 평가  
pred <- predict(model, test) # 비율 예측 
#@@9
pred <- predict(model, test, type="class") # 분류 예측 
#@@10


# 1) 분류모델로 분류된 y변수 보기 
table(pred)
# setosa versicolor  virginica 
# 13         19         13 

# 2) 분류모델 성능 평가 
table(pred, test$Species)
# pred         setosa versicolor virginica
#   setosa         13          0         0
#   versicolor      0         16         3
#   virginica       0          1        12

# 분류 정확도
(13+16+12)/nrow(test)   # 0.9111111
#[해석] 91%의 분류 정확도를 갖는다.


##################################################
# Decision Tree 응용실습 : 암 진단 분류 분석
##################################################
# "wdbc_data.csv" : 유방암 진단결과 데이터 셋 분류

# 1. 데이터셋 가져오기 
wdbc <- read.csv('C:/ITWILL/2_Rwork/Part-IV/wdbc_data.csv', stringsAsFactors = FALSE)
str(wdbc)
# 'data.frame':	569 obs. of  32 variables:

# 2. 데이터 탐색 및 전처리 
wdbc <- wdbc[-1] # id 칼럼 제외(이상치) 
head(wdbc)
head(wdbc[, c('diagnosis')], 10) # 진단결과 : B -> '양성', M -> '악성'
# [1] "B" "B" "B" "B" "B" "B" "B" "M" "B" "B"

# 목표변수(y변수)를 factor형으로 변환 
# (stringsAsFactors = FALSE 옵션으로 데이터 가져왔기 때문에 형변환 작업 해줘야함.)
#  $ diagnosis        : chr  "B" "B" "B" "B" ... 
wdbc$diagnosis <- factor(wdbc$diagnosis, levels = c("B", "M"))
wdbc$diagnosis[1:10]
# [1] B B B B B B B M B B
# Levels: B M
# B(base)-->0 , M-->1

summary(wdbc)

# 3. 정규화  : 서로 다른 특징을 갖는 칼럼값 균등하게 적용 
normalize <- function(x){ # 정규화를 위한 함수 정의 
  return ((x - min(x)) / (max(x) - min(x)))
}

# wdbc[2:31] : x변수에 해당한 칼럼 대상 정규화 수행 
dim(wdbc) # 569  31
names(wdbc) # [1] "diagnosis"  

# y변수 칼럼(첫번째) 제외하고 함수 적용(lapply)
wdbc_x <- as.data.frame(lapply(wdbc[2:31], normalize)) 
wdbc_x
dim(wdbc_x) #  569  30
summary(wdbc_x) # 0 ~ 1 사이 정규화 
class(wdbc_x) # [1] "data.frame"
nrow(wdbc_x) # [1] 569

wdbc_df <- data.frame(wdbc$diagnosis, wdbc_x)
dim(wdbc_df) # 569  31
head(wdbc_df)

# 4. 훈련데이터와 검정데이터 생성 : 7 : 3 비율 
idx = sample(nrow(wdbc_df), 0.7*nrow(wdbc_df))
wdbc_train = wdbc_df[idx, ] # 훈련 데이터 
wdbc_test = wdbc_df[-idx, ] # 검정 데이터 


# 5. rpart 분류모델 생성 
wdbc_model <- rpart(wdbc.diagnosis~., data=wdbc_train)
wdbc_model

#<해석>
# 1) root 398 146 B (0.63316583 0.36683417)  
#  2) perimeter_worst< 0.2773544 247  11 B (0.95546559 0.04453441) *
#  3) perimeter_worst>=0.2773544 151  16 M (0.10596026 0.89403974)  
#   6) points_mean< 0.2371024 18   6 B (0.66666667 0.33333333) *
#   7) points_mean>=0.2371024 133   4 M (0.03007519 0.96992481) *

# 30개 변수 중에서 가장 중요한 변수는 "perimeter_worst"이고
# 두번째로 중요한 변수는 "points_mean" 이다.

rpart.plot(wdbc_model)
#@@1

# 6. 분류모델 평가  
# : 분류정확도 (예측치)

#-------------------------------------------------------
# type='class' : 범주 예측
pred <- predict(wdbc_model, wdbc_test, type = 'class')
head(pred)
true <- wdbc_test$wdbc.diagnosis

tab<-table(true, pred)
#     pred
# true  B  M
#    B 99  6
#    M 14 52


acc <- (tab[1,1]+tab[2,2])/sum(tab)
acc # 0.8830409
no_acc <- (tab[1,2]+tab[2,1])/sum(tab)
no_acc  # 0.1169591

no <- tab[1,1]/(tab[1,1]+tab[1,2]) 
no # 0.9428571
recall <- tab[2,2]/(tab[2,1]+tab[2,2])
recall # 0.7878788
precision <- tab[2,2]/(tab[1,2]+tab[2,2])
precision # 0.8965517
F1_score =2*((recall*precision)/(recall+precision))
F1_score  # 0.8387097

#----------------------------------------------------------
# type 생략 : 비율 예측 >> 더미 변수로 변환하는 작업 필요
pred <- predict(wdbc_model, wdbc_test)
pred
pred <- ifelse(pred[,1]>=0.5, 0, 1) # B(base)-->0 , M-->1
pred
true <- wdbc_test$wdbc.diagnosis

tab<-table(true, pred)
tab
#      pred
# true  0  1
#    B 99  6
#    M 14 52


##################################################################
# <교차 검정>
#@@2

# 단계1 : k겹 교차검정을 위한 샘플링
install.packages("cvTools")
library(cvTools)

?cvFolds
# cvFolds(n, K = 5, R = 1,
#         type = c("random", "consecutive", "interleaved"))

# k=3 : d1=50, d2=50, d3=50, 
cross <- cvFolds(n=nrow(iris), K=3, R=1, type="random" )
cross
# 3-fold CV:    
# Fold   Index
#  1      83
#  2     143
#  3     130
#  1      90
#  2      39
# .....
#<해석>
# Fold : dataset (d1, d2, d3 중 어디에 소속되어 있는지 알려줌)
# Index : row (iris 행번호)

str(cross)
# List of 5
# $ n      : num 150
# $ K      : num 3
# $ R      : num 1
# $ subsets: int [1:150, 1] 83 143 130 90 39 115 141 107 15 106 ...
# $ which  : int [1:150] 1 2 3 1 2 3 1 2 3 1 ...
# - attr(*, "class")= chr "cvFolds"
# <해석>
# subsets <- Index
# which <- Fold


# set1
d1 <- cross$subsets[cross$which==1, 1]
#<해석> subsets: int [1:150, 1] (150행 1열 구조이므로 행자리에 which==1조건으로 selet)

# set2 
d2 <- cross$subsets[cross$which==2, 1]
# set3
d3 <- cross$subsets[cross$which==3, 1]

length(d1) # 50
length(d2) # 50
length(d3) # 50

# 서로 균등하게 50개씩 dataset 균등분할

#-----------------------------------------------------------------------------
# <for문 이용해서 dataset 균등분할 만들기>
# : 위의 수기 과정을 자동화
K <- 1:3
R <- 1

for(r in R){ # set = 열 index
  for(k in K){ # k겹 =행 index
    idx <- cross$subsets[cross$which==k, r]
    cat('k= ',k, '\n')
    print(idx)
  }
}
#@@4

# < R=2 실습 >
cross <- cvFolds(n=nrow(iris), K=3, R=2, type="random" )
K <- 1:3
R <- 1:2

for(r in R){ # set = 열 index (2회)
  cat('R= ', r, '\n')
  for(k in K){ # k겹 =행 index (3회)
    idx <- cross$subsets[cross$which==k, r]
    cat('k= ',k, '\n')
    print(idx)
  }
}
#@@5
#------------------------------------------------------------------------------


K <- 1:3
R <- 1
ACC <- numeric()
for(r in R){ # set = 열 index (1회)
  # cat('R= ', r, '\n')
  for(k in K){ # k겹 =행 index (3회)
    idx <- cross$subsets[cross$which==k, r]
    # cat('k= ',k, '\n')
    # print(idx)
    test <- iris[idx,] # 검정용(50)
    train <- iris[-idx,] # 훈련용(100)
    model <-rpart(Species~ ., data=train)
    pred <- predict(model, test, type = 'class')
    tab <- table(test$Species, pred)
    ACC[k] <- (tab[1,1]+tab[2,2]+tab[3,3]) / sum(tab)
  }
}

ACC # 0.94 0.92 0.96
mean(ACC) # 0.94

#-------------------------------------------------------
#< 카운터 변수 이용 > : 정석 (결과 동일)
K <- 1:3
R <- 1
ACC <- numeric()
cnt <- 1
for(r in R){ # set = 열 index (1회)
  # cat('R= ', r, '\n')
  for(k in K){ # k겹 =행 index (3회)
    idx <- cross$subsets[cross$which==k, r]
    # cat('k= ',k, '\n')
    # print(idx)
    test <- iris[idx,] # 검정용(50)
    train <- iris[-idx,] # 훈련용(100)
    model <-rpart(Species~ ., data=train)
    pred <- predict(model, test, type = 'class')
    tab <- table(test$Species, pred)
    ACC[cnt] <- (tab[1,1]+tab[2,2]+tab[3,3]) / sum(tab)
    cnt <- cnt +1 # 카운트 변수
  }
}
ACC
mean(ACC)

#####################################################################
### titanic3.csv
####################################################################
# titanic3.csv 변수 설명
#'data.frame': 1309 obs. of 14 variables:
#1.pclass : 1, 2, 3등석 정보를 각각 1, 2, 3으로 저장
#2.survived : 생존 여부. survived(생존=1), dead(사망=0)
#3.name : 이름(제외)
#4.sex : 성별. female(여성), male(남성) :Factor
#5.age : 나이
#6.sibsp : 함께 탑승한 형제 또는 배우자의 수
#7.parch : 함께 탑승한 부모 또는 자녀의 수
#8.ticket : 티켓 번호(제외)
#9.fare : 티켓 요금
#10.cabin : 선실 번호(제외)
#11.embarked : 탑승한 곳. C(Cherbourg), Q(Queenstown), S(Southampton)
#12.boat     : (제외)Factor w/ 28 levels "","1","10","11",..: 13 4 1 1 1 14 3 1 28 1 ...
#13.body     : (제외)int  NA NA NA 135 NA NA NA NA NA 22 ...
#14.home.dest: (제외)

titanic <- read.csv(file.choose())
str(titanic)
# <조건1> 6개 변수 제외 -> subset 생성
# <조건2> survived : int(0:사망, 1:생존) -> factor변환 (0,1)
# <조건3> train vs test  -> 7:3
# <조건4> 가장 중요한 변수 ?
# <조건5> model 평가 : 분류정확도

# 제외 변수: c(3, 8, 10, 12, 13, 14)
titanic_data <- titanic[,-c(3, 8, 10, 12, 13, 14)]
head(titanic_data)
dim(titanic_data) # 1309    8

str(titanic_data$survived) #  int [1:1309] 1 1 0 0 0 1 1 0 1 0 ...
titanic_data$survived <- factor(titanic_data$survived, levels = c("0", "1"))
str(titanic_data$survived) #  Factor w/ 2 levels "0","1": 2 2 1 ...

idx <- sample(nrow(titanic_data), nrow(titanic_data)*0.7)
train <- titanic_data[idx, ]
test <- titanic_data[-idx, ]

model <- rpart(survived~., data=train)
model
# 1) root 916 351 0 (0.61681223 0.38318777)  
# 2) sex=male 596 118 0 (0.80201342 0.19798658)  
# 4) age>=3.5 578 105 0 (0.81833910 0.18166090) *
#   5) age< 3.5 18   5 1 (0.27777778 0.72222222) *
#   3) sex=female 320  87 1 (0.27187500 0.72812500)  
#   6) pclass>=2.5 147  69 0 (0.53061224 0.46938776)  
# 12) fare>=24.80835 14   2 0 (0.85714286 0.14285714) *
#   13) fare< 24.80835 133  66 1 (0.49624060 0.50375940)  
# 26) age>=27.5 28   7 0 (0.75000000 0.25000000) *
# ◈ 가장 중요한 변수 : sex >> age, pclass >> fare

rpart.plot(model)
#@@6

pred <- predict(model, test, type = 'class')
tab<-table(test$survived, pred)
tab
#   pred
#     0   1
# 0 219  25
# 1  52  97

acc<-(tab[1,1]+tab[2,2])/sum(tab)
acc # 0.8040712

