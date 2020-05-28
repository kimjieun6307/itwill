#################################
## <제12장 연습문제>
################################# 

# 01. 교육수준(education)과 흡연율(smoking) 간의 관련성을 분석하기 위한 연구가설을 수립하고, 
# 이를 토대로 가설을 검정하시오.[독립성 검정]

#귀무가설 : 교육수준과 흡연율 간의 관련이 없다.
#연구가설 : 교육수준과 흡연율 간은 관련이 있다.

#<단계 1> 파일 가져오기
setwd("C:/ITWILL/2_Rwork/Part-III")
smoke <- read.csv("smoke.csv", header=TRUE)
# 변수 보기
head(smoke) # education, smoking 변수
names(smoke)

#<단계 2> 코딩 변경 - 변수 리코딩 <- 가독성 제공    
# education(독립변수) : 1:대졸, 2:고졸, 3:중졸 
# smoking(종속변수): 1:과다흡연, 2:보통흡연, 3:비흡연
table(smoke$education)
table(smoke$smoking)

smoke$education2[smoke$education==1] <- "1:대졸"
smoke$education2[smoke$education==2] <- "2:고졸"
smoke$education2[smoke$education==3] <- "3:중졸"

smoke$smoking2[smoke$smoking==1] <- "1:과다흡연"
smoke$smoking2[smoke$smoking==2] <- "2:보통흡연"
smoke$smoking2[smoke$smoking==3] <- "3:비흡연"


#<단계 3> 교차분할표 작성    
table(smoke$education2, smoke$smoking2)
# 1:과다흡연 2:보통흡연 3:비흡연
# 1:대졸         51         92       68
# 2:고졸         22         21        9
# 3:중졸         43         28       21

CrossTable(smoke$education2, smoke$smoking2, chisq = TRUE)

#<단계 4> 독립성 검정
chisq.test(smoke$education2, smoke$smoking2)
# X-squared = 18.911, df = 4, p-value = 0.0008183

#<단계 5> 검정결과 해석
# (해석) p-value = 0.0008183 < 0.05(알파) : 귀무가설 기각
# (결론) 교육수준과 흡연율 간의 관련성이 있다.



# 02. 나이(age3)와 직위(position) 간의 관련성을 단계별로 분석하시오. [독립성 검정]
#[단계 1] 파일 가져오기
data <- read.csv("cleanData.csv", header=TRUE)
head(data)

#[단계 2] 변수 선택
x <- data$position
y <- data$age3 

#[단계 3] 산점도를 이용한 변수간의 관련성 보기 - plot(x,y) 함수 이용
plot(x,y)
plot(x,y, abline(lm(y~x)), main='나이와 직위에 대한 산점도')

#[단계 4] 독립성 검정
CrossTable(x=x, y=y, chisq = T)
#Chi^2 =  287.8957     d.f. =  8     p =  1.548058e-57 

#[단계 5] 검정결과 해석
# 귀무가설 : 나이(age3)와 직위(position) 간의 관련성이 없다.
# (해석)  p =  1.548058e-57 < 0.05 -- 귀무가설 기각
# (결론) 나이(age3)와 직위(position) 간의 관련성이 있다.


# 03. 직업유형에 따른 응답정도에 차이가 있는가를 단계별로 검정하시오.[동질성 검정]

#[단계 1] 파일 가져오기
response <- read.csv("response.csv", header=TRUE)
head(response) # 변수 보기

# [단계 2] 코딩 변경 
# job 칼럼 코딩 변경 : 1:학생, 2:직장인, 3:주부 
# response 칼럼 코딩 변경 : 1:무응답, 2:낮음, 3:높음
response$job1[response$job==1] <- "1:학생"
response$job1[response$job==2] <- "2:직장인"
response$job1[response$job==3] <- "3:주부"

response$response2[response$response==1] <- "1:무응답"
response$response2[response$response==2] <- "2:낮음"
response$response2[response$response==3] <- "3:높음"


# [단계 3] 교차분할표 작성
table(response$job1, response$response2)
#           1:무응답 2:낮음 3:높음
# 1:학생         25     37      8
# 2:직장인       10     62     53
# 3:주부          5     41     59

# [단계 4] 동질성 검정  
chisq.test(response$job1, response$response2)
# X-squared = 58.208, df = 4, p-value = 6.901e-12

# [단계 5] 검정결과 해석
# 귀무가설 : 직업유형에 따른 응답정도에 차이가 없다.
# (해석) p-value = 6.901e-12 < 0.05 -- 귀무가설 기각
# (결론) 직업유형에 따른 응답정도에 차이가 있다.


