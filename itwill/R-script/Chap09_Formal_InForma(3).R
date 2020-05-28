# Chap09_Formal_InForma(3)

# 분석 절차
# 1단계 : 토픽분석(단어의 빈도수)
# 2단계 : 연관어 분석(관련 단어 분석) 
# 3단계 : 감성 분석(단어의 긍정/부정 분석) <-- ★

#############################################
# 단계3 - 감성 분석(단어의 긍정/부정 분석) 
#  - 시각화 : 파랑/빨강 -> 불만고객 시각화
#############################################

# 1. 데이터 가져오기() 
setwd("C:/ITWILL/2_Rwork/Part-II")

data<-read.csv("reviews.csv") 
head(data,2) #-- 영문
dim(data) # 100   2
View(data)
str(data)


# 2. 단어 사전에 단어추가

# 긍정어/부정어 영어 사전 가져오기
posDic <- readLines("posDic.txt")
negDic <- readLines("negDic.txt")
length(posDic) # 2006
length(negDic) # 4783


# 긍정어/부정어 단어 추가 
posDic.final <-c(posDic, 'victor')
negDic.final <-c(negDic, 'vanquished')


# 3. 감성 분석 함수 정의-sentimental

# (1) 문자열 처리를 위한 패키지 로딩 
install.packages('plyr')
library(plyr) # laply()함수 제공
library(stringr) # str_split()함수 제공(>> list 형태로 반환)

# laply() : list + apply
a <- list(a=1:5)
a # key : value
# $a
# [1] 1 2 3 4 5

x <- function(a, b){
  
}
x(10, 20)


laply(a, function(x, y, z){ # a->x, 10->y, 20->z
  return(x+y+z)
}, 10, 20)
# 1  2  3  4  5 
# 31 32 33 34 35


# (2) 감성분석을 위한 함수 정의
sentimental = function(sentences, posDic, negDic){
  
  scores = laply(sentences, function(sentence, posDic, negDic) {
    
    # 1. 문장 전처리 : gsub('패턴', '교체', 문장)
    sentence = gsub('[[:punct:]]', '', sentence) #문장부호 제거(문장부호->공백으로 교체)
    sentence = gsub('[[:cntrl:]]', '', sentence) #특수문자 제거
    sentence = gsub('\\d+', '', sentence) # 숫자 제거
    sentence = tolower(sentence) # 모두 소문자로 변경(단어가 모두 소문자 임)
    
    # 2. 문장 -> 단어
    word.list = str_split(sentence, '\\s+') # 공백(s) 기준으로 단어 생성 -> \\s+ : 공백 정규식, +(1개 이상) 
    words = unlist(word.list) # unlist() : list를 vector 객체로 구조변경
    
    # 단어 vs 사전 -> 긍정어/부정어
    pos.matches = match(words, posDic) # words의 단어를 posDic에서 matching
    neg.matches = match(words, negDic)
    
    # 매칭된 단어 추출
    pos.matches = !is.na(pos.matches) # NA 제거, 위치(숫자)만 추출
    neg.matches = !is.na(neg.matches)
    
    # 점수 = 긍정단어 점수 - 부정단어 점수
    score = sum(pos.matches) - sum(neg.matches) # 긍정 - 부정    
    return(score)
  }, posDic, negDic) # inner function
  
  scores.df = data.frame(score=scores, text=sentences)
  return(scores.df)
} # outer function

# 4. 감성 분석 : 두번째 변수(review) 전체 레코드 대상 감성분석
# 위 단계에서 만든 함수 sentimental(sentences, posDic, negDic)
result<-sentimental(data[,2], posDic.final, negDic.final)
result
View(result)
names(result) # "score" "text" 
dim(result) # 100   2
head(result, 2)
View(result$text)
result$score # 100 줄 단위로 긍정어/부정어 사전을 적용한 점수 합계

# score값을 대상으로 color 칼럼 추가
result$color[result$score >=1] <- "blue"
result$color[result$score ==0] <- "green"
result$color[result$score < 0] <- "red"

# 감성분석 결과 차트보기
plot(result$score, col=result$color) # 산포도 색생 적용
barplot(result$score, col=result$color, main ="감성분석 결과화면") # 막대차트


# 5. 단어의 긍정/부정 분석 

# (1) 감성분석 빈도수 
table(result$color)

# (2) score 칼럼 리코딩 
result$remark[result$score >=1] <- "긍정"
result$remark[result$score ==0] <- "중립"
result$remark[result$score < 0] <- "부정"

sentiment_result<- table(result$remark)
sentiment_result

# (3) 제목, 색상, 원크기
pie(sentiment_result, main="감성분석 결과", 
    col=c("blue","red","green")) # ->  1.2
