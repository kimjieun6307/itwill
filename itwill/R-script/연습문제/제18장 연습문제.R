#################################
## <제18장 연습문제>
################################# 

# 01. iris 데이터 셋의 1~4번째 변수를 대상으로 유클리드 거리 매트릭스를 구하여 
# idist에 저장한 후 계층적 클러스터링을 적용하여 결과를 시각화 하시오.

iris_data <-iris[1:4] # 4개변수 전체


#단계1. 유클리드 거리 계산
idist <- dist(iris_data)

#단계2. 계층형 군집분석(클러스터링)
ihclust<-hclust(idist)

#단계3. 분류결과를 대상으로 음수값을 제거하여 덴드로그램 시각화
plot(ihclust, hang = -1)

#단계4. 그룹수를 4개로 지정하고 그룹별로 테두리 표시
rect.hclust(ihclust, k=4, border = "red")

ghc <- cutree(ihclust, k=4)
table(ghc)
#  1  2  3  4 
# 50 60 28 12 

#------------------------------------------------------------------------------

# 02. 다음과 같은 조건을 이용하여 각 단계별로 "비계층적 군집분석"을 수행하시오.

# 조건1) 대상 파일 : product_sales.csv
# 조건2) 변수 설명 : tot_price : 총구매액, buy_count : 구매횟수, 
#                    visit_count : 매장방문횟수, avg_price : 평균구매액

setwd("c:/ITWILL/2_Rwork/Part-IV")
sales <- read.csv("product_sales.csv", header=TRUE)
head(sales) 


# 단계1: 비계층적 군집분석 : 3개 군집으로 군집화 kmeans()
sales_km<-kmeans(sales, 3) #centers=3
table(sales_km$cluster)

# 단계2: 원형데이터에 군집수 추가
sales$cluster <- sales_km$cluster
head(sales)

# 단계3 : tot_price 변수와 가장 상관계수가 높은 변수와 군집분석 시각화
cor(sales[,-5], method="pearson") # method="pearson" 생략가능
#              tot_price visit_count   buy_count  avg_price
# tot_price    1.00000000   0.8179536 -0.01305105  0.8717542
# visit_count  0.81795363   1.0000000 -0.23061166  0.9627571
# buy_count   -0.01305105  -0.2306117  1.00000000 -0.2785045
# avg_price    0.87175416   0.9627571 -0.27850452  1.0000000
# <해석> tot_price 변수와 가장 상관계수가 높은 변수 : avg_price

plot(sales$avg_price, sales$tot_price, col=sales$cluster)
#@@12

# 단계4. 군집의 중심점 표시
points(sales_km$centers[,c("avg_price", "tot_price")], col=c(3,2,1), pch=8, cex=5)
# > sales_km$centers
# tot_price visit_count buy_count avg_price
# 1  5.901613    1.433871  2.754839  4.393548
# 2  6.850000    2.071053  3.071053  5.742105
# 3  5.006000    0.244000  3.284000  1.464000

#@@13


