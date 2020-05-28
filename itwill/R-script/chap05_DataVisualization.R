# chap05_DataVisualization

# 차트 데이터 생성
chart_data <- c(305,450, 320, 460, 330, 480, 380, 520) 
names(chart_data) <- c("2016 1분기","2017 1분기","2016 2분기","2017 2분기","2016 3분기","2017 3분기","2016 4분기","2017 4분기")
str(chart_data)
chart_data

max(chart_data)

# 1. 이산변수 시각화
# - 정수단위로 나누어지는 수(자녀수, 판매수)

# (1) 막대차트
# 세로막대차트
barplot(chart_data, ylim=c(0,600), 
        main = "2016년 vs 2017년 판매현황",
        col = rainbow(8))

# 가로 막대 차트
barplot(chart_data, xlim=c(0,600), horiz = T, 
        main = "2016년 vs 2017년 판매현황",
        col = rainbow(8))


# 1행 2열 구조
par(mfrow=c(1,2))
VADeaths
str(VADeaths)

row_names <- row.names(VADeaths)
col_names <- colnames(VADeaths)

max(VADeaths)

# beside = FALSE, horiz = FALSE
barplot(VADeaths, beside = F, horiz = F, 
        main="버지니아 사망비율", col=rainbow(4))

# beside = TRUE, horiz = FALSE
barplot(VADeaths, beside = T, horiz = F, 
        main="버지니아 사망비율", col=rainbow(4))

par(mfrow=c(1,1))

# 범례추가(직전에 그린 차트에 범례추가)
legend(x=4, y=200, legend =row_names,
       fill = rainbow(5))


# (2) 점 차트
dotchart(chart_data, 
         color=c("Blue","red"), 
         lcolor="black", 
         pch=1:2,  # 포인트 모양(1-동그라미, 2-세모)
         labels=names(chart_data), # Y축 이름
         xlab="매출액", 
         main="분기별 판매현황 점 차트 시각화", 
         cex=1.2) # 크기(기본=1)

# (3) 파이 차트 시각화
pie(chart_data, labels = names(chart_data), 
    border='blue', col=rainbow(8), cex=1.2)

# 차트에 제목 추가(직전에 그린 차트에)
title("2014~2015년도 분기별 매출현황")

############################################
table(iris$Species)
pie(table(iris$Species),
    col=rainbow(3),
    main="iris 꽃의 종 빈도수")

##########################################

# 2. 연속 변수 시각화
# - 시간, 길이 등이 연속성을 갖는 변수

# 1)상자 그래프 시각화 - summary 요약통계량 시각화
summary(VADeaths)

# 참고-사분위수
quantile(VADeaths[,1])


boxplot(VADeaths)

# 2) 히스토그램 시각화
range(iris$Sepal.Width) #  2.0 ~ 4.4 >> xlim 크기 정하기

hist(iris$Sepal.Width, 
     xlab="iris$Sepal.Width", 
     col="mistyrose",   # mistyrose : 흐릿한 장미색
     main="iris 꽃받침 넓이 histogram", 
     xlim=c(2.0, 4.5)) 

# 밀도(freq = F)
par(mfrow=c(1,2)) 

hist(iris$Sepal.Width, 
     xlab="iris$Sepal.Width", 
     col="green", 
     freq = F,
     main="iris 꽃받침 넓이 histogram", 
     xlim=c(2.0, 4.5))

# 밀도분포 곡선(freq = F 일때 lines(density())
par(mfrow=c(1,1)) 

hist(iris$Sepal.Width, 
     xlab="iris$Sepal.Width", 
     col="green", 
     freq = F,
     main="iris 꽃받침 넓이 histogram", 
     xlim=c(2.0, 4.5))

lines(density(iris$Sepal.Width), col="red")

n <- 10000
x <- rnorm(n, mean = 0, sd=1)
hist(x,freq = F)
lines(density(x), col="green")

# 3) 산점도 시각화
x <- runif(n=15, min = 1, max=100)
plot(x) # x -> Y축 , index -> X축

y <- runif(n=15, min = 1, max=100)

# x, y = 연속형
plot(x,y) 
plot(y~x) # plot(x,y) 와 같음.

# col 속성 = 범주형
head(iris, 10)
plot(iris$Sepal.Length, iris$Petal.Length, 
     col=iris$Species)


par(mfrow=c(2,2)) # 2행 2열 차트 그리기 

price<-runif(10, min=1, max=100)

plot(price, type="l") # 유형 : 실선 
plot(price, type="o") # 유형 : 원형과 실선(원형 통과) 
plot(price, type="h") # 직선 
plot(price, type="s") # 꺾은선


plot(price, type="o", pch=5) # 빈 사각형 
plot(price, type="o", pch=15)# 채워진 마름모 
plot(price, type="o", pch=20, 
     col="blue") #color 지정 
plot(price, type="o", pch=20, 
     col="orange", cex=1.5) #character expension(확대) 
plot(price, type="o", pch=20, 
     col="green", cex=2.0, lwd=3) #lwd : line width


# 만능차트
methods(plot)

# plot.ts : 시계열 자료
WWWusage
plot(WWWusage) # 추세선

# plot.lm* : 회귀모델
install.packages("UsingR")
library(UsingR)
library(help="UsingR")

# 유전학자 갈콘 : 회귀 용어 제안 / (회귀:평균으로 되돌아 간다)
data(galton) 
str(galton)

model <- lm(child~parent, data=galton) #(y~x):y-영향을 받는 변수, x-영향을 주는 변수
plot(model)

# 4) 산점도 행렬 : 변수 간의 비교 / pairs()
pairs(iris[-5])

# 꽃의 종별 산점도 행렬 : pairs(iris[row, col])
table(iris$Species) # setosa versicolor  virginica 
pairs(iris[iris$Species=='setosa', 1:4])
pairs(iris[iris$Species=='virginica', 1:4])


#파일로 차트 저장하기 
setwd("C:/ITWILL/2_Rwork/output") # 폴더 지정 
jpeg("iris.jpg", width=720, height=480) # 픽셀 지정 가능 
plot(iris$Sepal.Length, iris$Petal.Length, col=iris$Species) 
title(main="iris 데이터 테이블 산포도 차트") 
dev.off()  # 장치 종료


#########################
### 3차원 산점도 
#########################
install.packages('scatterplot3d')
library(scatterplot3d)

str(iris)
# 꽃의 종류별 분류 
iris_setosa = iris[iris$Species == 'setosa',]
iris_versicolor = iris[iris$Species == 'versicolor',]
iris_virginica = iris[iris$Species == 'virginica',]

# scatterplot3d(밑변, 오른쪽변, 왼쪽변, type='n') # type='n' : 기본 산점도 제외 
d3 <- scatterplot3d(iris$Petal.Length, iris$Sepal.Length, iris$Sepal.Width, type='n')

d3$points3d(iris_setosa$Petal.Length, iris_setosa$Sepal.Length,
            iris_setosa$Sepal.Width, bg='orange', pch=21)

d3$points3d(iris_versicolor$Petal.Length, iris_versicolor$Sepal.Length,
            iris_versicolor$Sepal.Width, bg='blue', pch=23)

d3$points3d(iris_virginica$Petal.Length, iris_virginica$Sepal.Length,
            iris_virginica$Sepal.Width, bg='green', pch=25)










