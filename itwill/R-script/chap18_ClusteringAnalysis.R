# chap18_ClusteringAnalysis(1)

###################################################
# 군집분석(Clustering)
###################################################
# 고객DB   ->  알고리즘 -> 군집
# 알고리즘을 통해서(패턴으로) 근거리 모형으로 군집형성 - 규칙(rule)
# 변수에 의해서 그룹핑되다.
# 변수 적용 : 상품카테고리, 구매금액, 총거래금액

# 유사성 거리에 의한 유사객체를 묶어준다.
# 거리를 측정하여 집단의 이질성과 동질성을 평가하고, 이를 통해서 
# 군집을 형성한다..
# 유사성 거리 : 유클리드 거리
# y변수가 없는 데이터 마이닝 기법
# 예) 몸, 키 관점에서 묶음 -> 3개 군집 <- 3개 군집의 특징 요약
# 주요 알고리즘 : hierarchical, k-means

# 그룹화를 통한 예측(그룹 특성 차이 분석-고객집단 이해)

# 1. 유클리드 거리
# 유클리드 거리(Euclidean distance)는 두 점 사이의 거리를 계산하는 
# 방법으로 이 거리를 이용하여 유클리드 공간을 정의한다.

# (1) matrix 생성
x <- matrix(1:9, nrow=3, by=T) 


# (2) matrix 대상 유클리드 거리 생성 함수
# 형식) dist(x, method="euclidean") -> x : numeric matrix, data frame
dist <- dist(x, method="euclidean") # method 생략가능
dist
#           1         2
# 2  5.196152          
# 3 10.392305  5.196152
#<해석> 1행과 2행의 거리 5,196152 / 1행과 3행 거리 10,392305
#       2행과 3행 거리 5,196152


# (3) 유클리드 거리 계산 식
# 관측대상 p와 q의 대응하는 변량값의 차의 제곱의 합에 sqrt 적용
sqrt(sum((x[1,]-x[2,])**2)) #  5.196152  ---> dist(x)함수 값과 동일
sqrt(sum((x[1,]-x[3,])**2)) # 10.3923

#------------------------------------------------------------------

# 2. 계층적 군집분석(탐색적 분석)
# - 계층적 군집분석(Hierarchical Clustering)
# - 거리가 가장 가까운 대상부터 결합하여 나무모양의 
#   계층구조를 상향식(Bottom-up)으로 만들어가면서 군집을 형성 

# (1) 군집분석(Clustering)분석을 위한 패키지 설치
install.packages("cluster") # hclust() : 계층적 클러스터 함수 제공
library(cluster) # 일반적으로 3~10개 그룹핑이 적정

# (2) 데이터 셋 생성
r <- runif(15, min = 1, max = 50)
x <- matrix(r, nrow=5, by=T) 
x
#          [,1]     [,2]     [,3]
# [1,] 25.09302 10.82797 19.40195
# [2,] 37.68731 12.79780 13.10693
# [3,] 16.66040 29.51943 14.36246
# [4,] 28.87503  5.69022 20.89039
# [5,] 19.72782 13.85944 25.81579

# (3) matrix 대상 유클리드 거리 생성 함수
dist <- dist(x, method="euclidean") # method 생략가능
dist
#           1         2         3         4
# 2 14.217014                              
# 3 21.115784 26.894610                    
# 4  6.550991 13.738857 27.561609          
# 5  8.894525 22.026923 19.642381 13.216169
#<해석> 1번째 관측치 기준으로 가장 가까운 관측치는 4번째(6,550991)이다.
mean(x[1,]) # 18.44098
mean(x[4,]) # 18.48521
#<해석> 평균이 유사함.

# (4) 유클리드 거리 matrix를 이용한 클러스터링
hc <- hclust(dist) # 클러스터링 적용
hc
# Call:
# hclust(d = dist)
# Cluster method   : complete 
# Distance         : euclidean 
# Number of objects: 5  ---> 5개 객체 사용

help(hclust)
plot(hc) # 클러스터 플로팅(Dendrogram) -> 1과2 군집(클러스터) 형성
#@@1 (덴드로 그램)-유클리드 거리를 기반으로 한다.


#<실습> 중1학년 신체검사 결과 군집분석
#---------------------------------------------
body <- read.csv("c:/ITWILL/2_Rwork/Part-IV/bodycheck.csv")
names(body)
# [1] "번호"  "악력"  "신장"  "체중"  "안경유무"
str(body) #'data.frame':	15 obs. of  5 variables:
idist <- dist(body)
idist
#@@2
hc <- hclust(idist)

plot(hc, hang=-1) # 음수값 제외
#@@3


# 3개 그룹 선정, 선 색 지정
rect.hclust(hc, k=3, border="red") # 3개 그룹 선정, 선 색 지정
#@@4

# 각 그룹별 서브셋 만들기
g1<- subset(body, 번호==15| 번호==1| 번호==4| 번호==8 | 번호==10)
g2<- subset(body, 번호==11| 번호==3| 번호==5| 번호==6 | 번호==14)
g3<- subset(body, 번호==2| 번호==9| 번호==7| 번호==12 | 번호==13)

# 각 그룹별 특징
summary(g1)
# 번호           악력           신장            체중         안경유무
# Min.   : 1.0   Min.   :23.0   Min.   :142.0   Min.   :32.0   Min.   :1  
# 1st Qu.: 4.0   1st Qu.:25.0   1st Qu.:146.0   1st Qu.:34.0   1st Qu.:1  
# Median : 8.0   Median :25.0   Median :152.0   Median :38.0   Median :1  
# Mean   : 7.6   Mean   :25.6   Mean   :149.8   Mean   :36.6   Mean   :1  
# 3rd Qu.:10.0   3rd Qu.:27.0   3rd Qu.:153.0   3rd Qu.:39.0   3rd Qu.:1  
# Max.   :15.0   Max.   :28.0   Max.   :156.0   Max.   :40.0   Max.   :1  
#  <해석>-----신장 : 142~156, 안경유무(1)
summary(g2) # 신장 : 155~168, 안경유무(1, 2)
summary(g3) # 신장 : 154~169, 안경유무(2)

# ★군집수는 분석가가 정해서 각 군집의 특징을 해석하면 됨★

#--------------------------------------------------------------------------

# 3. 계층형 군집분석에 그룹수 지정
# iris의 계층형군집결과에 그룹수를 지정하여 그룹수 만큼 
# 잘라서 iris의 1번째(Sepal.Length)와 3번째(Petal.Length) 변수를 
# 대상으로 클러스터별 변수의 평균 구하기 

# 1) 유클리드 거리 계산 
str(iris) # 'data.frame':	150 obs. of  5 variables:
idist<- dist(iris[1:4]) # dist(iris[, -5]) ---# 계산식 수행하려면 연속형 변수로 되어 있어야 함.(범주형 제외)

# 2) 계층형 군집분석(클러스터링)
hc <- hclust(idist)
hc
# Cluster method   : complete 
# Distance         : euclidean 
# Number of objects: 1
plot(hc, hang=-1)
rect.hclust(hc, k=3, border="red") # 3개 그룹수 
#@@5

# 3) 그룹수 만들기 : cutree()함수 -> 지정된 그룹수 만큼 자르기
# 형식) cutree(계층형군집결과, k=그룹수) -> 그룹수 만큼 자름
ghc<- cutree(hc, k=3) # stats 패키지 제공

ghc #  150개(그룹을 의미하는 숫자(1~3) 출력)
#   [1] 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#  [24] 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#  [47] 1 1 1 1 2 2 2 3 2 3 2 3 2 3 3 3 3 2 3 2 3 3 2
#  [70] 3 2 3 2 2 2 2 2 2 2 3 3 3 3 2 3 2 2 2 3 3 3 2
#  [93] 3 3 3 3 3 2 3 3 2 2 2 2 2 2 3 2 2 2 2 2 2 2 2
# [116] 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# [139] 2 2 2 2 2 2 2 2 2 2 2 2

# 4) iris에서 ghc 컬럼 추가
iris$ghc <- ghc
table(iris$ghc) # ghc 빈도수
#  1  2  3 
# 50 72 28
head(iris,60) # ghc 칼럼 확인 
#@@6

# 5) 그룹별 요약통계량 구하기
g1 <- subset(iris, ghc==1)
summary(g1[1:4]) 
#  Sepal.Length  Mean   :5.006 / Petal.Length Mean   :1.462

g2 <- subset(iris, ghc==2)
summary(g2[1:4]) 
# Sepal.Length   Mean   :6.546 / Petal.Length Mean   :5.274 

g3 <- subset(iris, ghc==3)
summary(g3[1:4]) 
# Sepal.Length   Mean   :5.532 / Petal.Length Mean   :3.961 

#------------------------------------------------------------------

# 4. 비계층적 군집분석(확인적 분석)
# - 군집 수를 알고 있는 경우 이용하는 군집분석 방법

# 군집분석 종류 : 계층적 군집분석(탐색적), 비계층적 군집분석(확인적) 

# 1) data set 준비 
library(ggplot2)
data(diamonds)

nrow(diamonds) # [1] 53940
View(diamonds)
str(diamonds) # Classes ‘tbl_df’, ‘tbl’ and 'data.frame':	53940 obs. of  10 variables:

t <- sample(nrow(diamonds),1000) # 1000개 샘플링 

test <- diamonds[t, ] # 1000개 표본 추출
dim(test) # [1] 1000 10

head(test) # 검정 데이터
mydia <- test[c("price","carat", "depth", "table")] # 4개 칼럼만 선정
head(mydia)

# 2) 계층적 군집분석(탐색적 분석)
result <- hclust(dist(mydia), method="average") # 평균거리 이용 
result
# Cluster method   : average 
# Distance         : euclidean 
# Number of objects: 1000

# [작성] 군집 방법(Cluster method) 
# method = "complete" : 완전결합기준(최대거리 이용) <- default(생략 시)
# method = "single" : 단순결합기준(최소거리 이용) 
# method = "average" : 평균결합기준(평균거리 이용) 

plot(result, hang=-1) # hang : -1 이하 값 제거
#@@7

# 3) 비계층적 군집분석(확인적 분석) - kmeans()함수 이용
# - 확인적 군집분석 : 군집의 수를 알고 있는 경우
result2 <- kmeans(mydia, 3)
result2 
# K-means clustering with 3 clusters of sizes 307, 115, 578 - 클러스터별 군집수 
# Cluster means: 클러스터별 칼럼의 평균 

names(result2) # cluster 칼럼 확인 
#@@8
result2$cluster # 각 케이스에 대한 소속 군집수(1,2,3)
table(result2$cluster)
#   1   2   3 
# 307 115 578 

result2$centers  # 각 군집별 중앙값(Cluster means)
#       price     carat    depth    table
# 1  5269.003 1.0771661 61.93094 57.89088
# 2 11989.887 1.5917391 61.68522 57.87826
# 3  1407.891 0.4834256 61.73010 57.05709

# 4) 원형데이터에 군집수 추가
mydia$cluster <- result2$cluster
head(mydia) # cluster 칼럼 확인 
#   price carat depth table cluster
#   <int> <dbl> <dbl> <dbl>   <int>
# 1  8214  1.51  62.8    59       1
# 2  5189  1.08  62.6    57       1
# 3  4654  1.12  61.6    58       1
# 4  5546  1     60.5    60       1
# 5   764  0.4   61.5    56       3
# 6  4836  1.01  63.7    60       1

# 5) 변수 간의 상관성 보기 
plot(mydia[,-5]) # cluster 제외
#@@9
cor(mydia[,-5], method="pearson") # 상관계수 보기 
#           price     carat      depth      table
# price 1.0000000 0.9212910  0.0275522  0.1581566
# carat 0.9212910 1.0000000  0.0641868  0.2074748
# depth 0.0275522 0.0641868  1.0000000 -0.3128470
# table 0.1581566 0.2074748 -0.3128470  1.0000000
#<해석> 상관관계가 가장 높음 price와 carat을 x축과 y축으로 해서 산점도 시각화 
# 반응변수 : price <- 설명변수 : carat(양의 영향) > table(양의 영향) > depth(음의 영향)

library(corrgram) # 상관성 시각화 
corrgram(mydia[,-5]) # 색상 적용 - 동일 색상으로 그룹화 표시
corrgram(mydia[,-5], upper.panel=panel.conf) # 수치(상관계수) 추가(위쪽)


# 6) 비계층적 군집시각화 --- 상관관계가 가장 높음 price(y축)와 carat(x축)으로 산점도 시각화 
plot(mydia$carat, mydia$price)
plot(mydia$carat, mydia$price, col=mydia$cluster)
# mydia$cluster 변수로 색상 지정(1,2,3)
#<해석>군집이 제대로 만들어 졌는지 시각화로 확인
#@@10

# 중심점 표시 추가
result2$centers # Cluster means 값을 갖는 컬럼 

# 각 그룹의 중심점에 포인트 추가 
points(result2$centers[,c("carat", "price")], col=c(3,1,2), pch=8, cex=5)
# names(result2) -> centers 칼럼 확인 
# col : color, pch : 중심점 문자, cex : 중심점 문자 크기
# pch(plotting character), cex(character expansion)
#@@11

####################################################
## 군집수 결정방법
####################################################
install.packages("NbClust")
library(NbClust)

data("iris")
iris_mat <- as.matrix(iris[-5])
dim(iris_mat)

?NbClust
#NbClust(data = NULL, diss = NULL, distance = "euclidean", min.nc = 2, max.nc = 15, method = NULL, index = "all", alphaBeale = 0.1) 

nc <- NbClust(iris_mat, distance = "euclidean", min.nc = 2, max.nc = 15, method = "complete")
nc
#* According to the majority rule, the best number of clusters is  3 
#@@14

names(nc)
# [1] "All.index"          "All.CriticalValues"
# [3] "Best.nc"            "Best.partition"  

table(nc$Best.nc[1,])
# 0  1  2  3  4  6 15  ---> 클러스트
# 2  1  2 13  5  1  2 
#<해석> 가장 높은 빈도수(13) -> 3개 클러스트가 가장 최적이다.



