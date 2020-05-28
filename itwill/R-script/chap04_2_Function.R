# chap04_2_Function

# 1. 사용자 정의 함수 

# 형식 )
# 함수명 <- function([인수]){
#   실행문
#   실행문
#   [return 값]
# }

# 1) 매개변수가 없는 함수
f1 <- function(){
  cat('f1 함수')
}

f1() #함수 호출 

# 2) 매개변수 있는 함수
f2 <- function(x){
  x2 <- x^2
  cat('x2 =', x2)
}
f2(10)

# 3) 리턴있는 함수
f3 <- function(x,y){
  add <- x+y
  return(add)
}
f3(10, 5)
#함수 호출 >> 반환값
add_re <- f3(10, 5)


tot_func <- function(x){
  tot <- sum(x)
  return(tot)
}

tot_re <- tot_func(num)
num <- 1:10
avg <- tot_re / length(num)

# 문) calc 함수를 정의하기
# 출력형식 : 100 + 20 = 120
#            100 - 20 = 80
#            100 * 20 = 2000
#            100 / 20 = 5

# 지은
calc <- function(x,y){
  cat(x, '+', y, '=', (x+y),'\n')
  cat(x, '-', y, '=', (x-y),'\n')
  cat(x, '*', y, '=', (x*y),'\n')
  cat(x, '/', y, '=', (x/y),'\n')
}
calc(100,20)

#강사님
calc <- function(x,y){
  add <- x+y
  sub <- x-y
  mul <- x*y
  div <- x/y
  cat(x, '+', y, '=', add,'\n')
  cat(x, '-', y, '=', sub,'\n')
  cat(x, '*', y, '=', mul,'\n')
  cat(x, '/', y, '=', div,'\n')
}
calc(100,20)

# 참고  : 다중인자 반환은 허용되지 않습니다
calc <- function(x,y){
  add <- x+y
  sub <- x-y
  mul <- x*y
  div <- x/y
  cat(x, '+', y, '=', add,'\n')
  cat(x, '-', y, '=', sub,'\n')
  cat(x, '*', y, '=', mul,'\n')
  cat(x, '/', y, '=', div,'\n')
  calc_df <- data.frame(add, sub, mul, div)
  return(calc_df)
}
# 함수 호출
df <- calc(100,20)
df

# 구구단의 단을 인수 받아서 구구단 출력하기
gugu <- function(dan){
  cat('***', dan, '단 ***','\n')
  for(i in 1:9){
    cat(dan, '*', i, '=', dan*i, '\n')
  }
}
gugu(2)
gugu(5)
gugu(12)

state <- function(fname, data){
  switch (fname,
    SUM = sum(data),
    AVG = mean(data),
    VAR = var(data),
    SD = sd(data))
}
data <- 1:10
state("SUM",data)
state("AVG",data)
state("VAR",data)
state("SD",data)


# 결측치(NA) 처리 함수
# x1. NA -> 제거
# x2. NA -> 평균
# x3. NA -> 0
na <- function(x){
  x1 <- na.omit(x)
  cat('x1 : ', x1, '\n')
  cat('x1 = ', mean(x1),'\n')
  x2 <- ifelse(is.na(x), mean(x, na.rm=T),x)
  cat('x2 : ', x2, '\n')
  cat('x2 = ',mean(x2),'\n')
  x3 <- ifelse(is.na(x), 0, x)
  cat('x3 : ', x3, '\n')
  cat('x3 = ', mean(x3),'\n')
}

na(x)

x <- c(10,5,NA, 4.2, 6.3, NA, 7.5, 8,10 )
x
length(x)
mean(x, na.rm=T)


###################################
### 몬테카를로 시뮬레이션 
###################################
# 현실적으로 불가능한 문제의 해답을 얻기 위해서 난수의 확률분포를 이용하여 
# 모의시험으로 근사적 해를 구하는 기법

# 동전 앞/뒤 난수 확률분포 함수 
coin <- function(n){
  r <- runif(n, min=0, max=1)
  #print(r) # n번 시행 
  
  result <- numeric()
  for (i in 1:n){
    if (r[i] <= 0.5)
      result[i] <- 0 # 앞면 
    else 
      result[i] <- 1 # 뒷면
  }
  return(result)
}


# 몬테카를로 시뮬레이션 
montaCoin <- function(n){
  cnt <- 0
  for(i in 1:n){
    cnt <- cnt + coin(1) # 동전 함수 호출 
  }
  result <- cnt / n
  return(result)
}

montaCoin(5)
montaCoin(1000)
montaCoin(10000)

# 중심 극한 정리

#####################################
# 2. R의 주요 내장함수

# 1) 기술통계함수 

vec <- 1:10          
min(vec)                   # 최소값
max(vec)                   # 최대값
range(vec)                  # 범위
mean(vec)                   # 평균
median(vec)                # 중위수
sum(vec)                   # 합계
prod(vec)                  # 데이터의 곱
1*2*3*4*5*6*7*8*9*10
summary(vec)               # 요약통계량 

n <- rnorm(1000)  # mean=0, sd=1
mean(n)
sd(n)

sd(rnorm(10))      # 표준편차 구하기
factorial(5) # 팩토리얼=120
sqrt(49) # 루트

#예시) 소프트웨어 발표 전/후 버그 수
install.packages('RSADBE')
library(RSADBE)
library(help="RSADBE")

data(Bug_Metrics_Software)
str(Bug_Metrics_Software)
# num [1:5, 1:5, 1:2]

Bug_Metrics_Software[,,1] # Before
Bug_Metrics_Software[,,2] # After

# 행단위 합계 : 소프트웨어 별 버그 수 합계
rowSums(Bug_Metrics_Software[,,1])

# 열단위 합계 : 버그 별 합계
colSums(Bug_Metrics_Software[,,1])

# 행단위 평균
rowMeans(Bug_Metrics_Software[,,1])

# 열단위 평균
colMeans(Bug_Metrics_Software[,,1])


# Before - After 값을 3면에 추가하기
bug<-Bug_Metrics_Software # 복제
bug.new <- array(bug, dim=c(5,5,3)) # 면 추가
dim(bug.new)

bug.new[,,3] <- bug[,,1] - bug[,,2] 


# 2) 반올림 관련 함수 
x <- c(1.5, 2.5, -1.3, 2.5)
mean(x)
round(mean(x)) # 1.3 -> 1
ceiling(mean(x)) # x보다 큰 정수 
floor(mean(x)) # 1보다 작은 정수 


# 3) 난수 생성과 확률분포

# (1) 정규분포를 따르는 난수 - 연속확률분포(실수형)
# 형식) rnorm(n, mean=0, sd=1)

n <- 1000
r <- rnorm(n, mean = 0, sd=1)  # 표준정규분포
r
mean(r)
sd(r)
hist(r)

# (2) 균등분포를 따르는 난수 - 연속확률분포(실수형)
# 형식) runif(n, min=, max=)
r2 <- runif(n, min=0, max=1)
r2
hist(r2)

# (3) 이항분포를 따르는 난수 - 이산확률분포(정수형)
# 형식) rbinom(n, size = , prob =  ) : size가 prob 확률만큼 n개 나오는 

set.seed(123) # seed값이 같으면 동일한 난수 출력됨. 
n <- 10
r3 <- rbinom(n, size = 1, prob = 0.5 ) # 1/2

r3 <- rbinom(n, size = 1, prob = 0.25) # 1/4

# (4) sample : 범위 내에서 임의 추출
sample(10:20, 5) ##[1] 18 20 19 14 12
sample(10:20, 5) ##[1] 17 19 16 11 10 --중복 추출안됨.

sample(c(10:20, 50:100),10) ##[1] 70 80 83 16 18 79 19 61 65 91

# 홀드아웃방식 :  학습용 train(70%)/검정용 test(30%) 데이터셋
dim(iris) # [1] 150   5

idx <- sample(nrow(iris), nrow(iris)*0.7)
range(idx) # [1]   4 150
idx # 행번호
length(idx)

train <- iris[idx,] # 학습용
test <- iris[-idx,] # 검정용
dim(train) # [1] 105   5
dim(test) # [1] 45  5

# 4) 행렬연산 내장함수
x <- matrix(1:12, nrow=4, byrow = T)
y <- matrix(1:6, nrow = 3)
dim(x)
dim(y)

x;y

z <- x %*% y # 두 행렬의 곱
z
dim(z)
10+22+36
60+66+72

# 행렬곱의 전제조건
# 1. x,y 모드 행렬
# 2. x(열), y(행) 일지 : 수일치
# 3. z <- x %*% y  >> dim(z) = x(행) y(열)



x<- matrix(rep(1:3, time=3), nrow=3)
y <- matrix(rep(1:3, each=3), nrow = 3)
z <- x %*% y
dim(x)
dim(y)
