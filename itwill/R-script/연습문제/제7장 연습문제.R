#################################
## <제7장 연습문제>
################################# 

# 01. 본문에서 생성된 dataset2의 직급(position) 칼럼을 대상으로 
# 1급 -> 5급, 5급 -> 1급 형식으로
# 역코딩하여 position2 칼럼에 추가하시오.
table(dataset2$position)
dataset2$position2 <- 6 - dataset2$position
table(dataset2$position2)




# 02. dataset2의 resident 칼럼을 대상으로 NA 값을 제거한 후 
# dataset3 변수에 저장하시오.

# error
resident_na <- na.omit(dataset2$resident)
dataset3 <- dataset2
dataset3$resident_na <- resident_na

# **풀이**
dim(dataset2) # 232  11
dataset3 <- subset(dataset2, !is.na(resident))
dim(dataset3) # 217  13

# 검증 
dataset_ex <- subset(dataset2, !is.na(position))
str(dataset_ex)

# 03. dataset3의 gender 칼럼을 대상으로 1->"남자", 2->"여자" 형태로 
#코딩 변경하여 gender2 칼럼에 추가하고, 파이 차트로 결과를 확인하시오.
str(dataset3)

dataset3$gender2[dataset3$gender==1] <- "남자"
dataset3$gender2[dataset3$gender==2] <- "여자"

pie(table(dataset3$gender2))



# 04. 나이를 30세 이하 -> 1, 31~55 -> 2, 56이상 -> 3 으로 리코딩하여 
# age3 칼럼에 추가한 후 age, age2, age3 칼럼만 확인하시오.
dataset3$age3[dataset3$age <= 30] <- 1
dataset3$age3[dataset3$age >30 & dataset3$age <=55] <- 2
dataset3$age3[dataset3$age > 55 ] <- 3

dataset3[c('age', 'age2', 'age3')]


# 05. 정제된 data를 대상으로 작업 디렉터리(c:/Rwork/output)에 
# cleanData.csv 파일명으로 따옴표와 행 이름을 제거하여 저장하고, 
# new_data변수로 읽어오시오.

# (1) 정제된 데이터 저장
setwd("C:/ITWILL/2_Rwork/output")
write.csv(dataset3, "cleanData.csv", row.names=F, quote=F)

# (2) 저장된 파일 불러오기/확인
new_data <- read.csv(file.choose())
new_data

# 06. mtcars 데이터셋의 qsec(1/4마일 소요시간) 변수를 대상으로 
# 극단치(상위 0.3%)를 발견하고, 정제하여 
# mtcars_df 이름으로 서브셋을 생성하시오.

library(ggplot2)
str(mtcars) # 'data.frame':	32 obs. of  11 variables:

plot(mtcars$qsec)

# (1) 이상치 통계
boxplot(mtcars$qsec)$stats

# (2) 서브셋 생성 
mtcars_df <- subset(mtcars, mtcars$qsec>=14.5 & mtcars$qsec<=20.22 )

# (3) 정제 결과 확인 
plot(mtcars_df$qsec)
boxplot(mtcars_df$qsec)



# 07. user_data.csv와 return_data.csv 파일을 이용하여 각 고객별 
# 반품사유코드(return_code)를 대상으로 다음과 같이 파생변수를 추가하시오.
user_data <- read.csv("user_data.csv")
return_data <- read.csv("return_data.csv")
str(return_data)

# <조건1> 반품사유코드에 대한 파생변수 칼럼명 설명 
# 제품이상(1) : return_code1, 변심(2) : return_code2, 
# 원인불명(3) :> return_code3, 기타(4) : return_code4 
library(reshape2)
names(return_data)
table(return_data$return_code)
return_data_1 <- dcast(return_data, user_id ~ return_code)
names(return_data_1) <- c("user_id", "제품이상(1)", "변심(2)", "원인불명(3)","기타(4)")
return_data_1 %>% head()

# <조건2> 고객별 반품사유코드를 고객정보(user_data) 테이블에 추가(join)
library(dplyr)
user_return_data <- left_join(user_data, return_data_1, by="user_id")
head(user_return_data, 10)


summarise(user_return_data, sum(`제품이상(1)`, na.rm=T ))
