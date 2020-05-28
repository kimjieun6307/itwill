##################################
###  Part-I ~ Part-III 총정리  ###
##################################

setwd("C:/ITWILL/2_Rwork/Part-IV")
election <- read.csv("election_2012.csv") # 2012년도 미국 대통령 선거 후원금 현황 
str(election) # 'data.frame':	1001731 obs. of  16 variables:
# 2.cand_id : 대선후보자
# 3.cand_nm : 대선 후보자 이름
# 4.contbr_nm  : 후원자 이름 
# 9.contbr_occupation : 후원자 직업군 
# 10.contb_receipt_amt : 후원금


### 전처리 ###
# [문제1] 위 7개 칼럼으로 data.frame 생성 clean_election2 변수에 저장하시오.
clean_election2 <- election[c('cand_id','cand_nm','contbr_nm','contbr_occupation','contb_receipt_amt')]
head(clean_election2)

# [문제2] 직업군 칼럼을 대상으로 NA를 포함하는 관측치를 제외하여 clean_election2 변수에 저장하시오.
# <조건> 전처리 전과 후 관측치 수의 차이는? 
#   힌트) subset(), is.na() 함수 이용 
length(clean_election2$contbr_occupation) # 1001731

clean_election2 <- subset(clean_election2, !is.na(contbr_occupation))
length(clean_election2$contbr_occupation)  # 1001603


# [문제3] 5만개 관측치만 샘플링하여 clean_election2 변수에 저장하시오.
#  힌트) sample() 함수 이용
dim(clean_election2) #  1001603       5

idx <- sample(nrow(clean_election2), 50000)
clean_election2 <- clean_election2[idx, ]
dim(clean_election2) #  50000     5

# [문제4] 'Romney, Mitt'와 'Obama, Barack' 후보자별 서브셋을 작성하여 romney, obama 변수에 저장하시오
romney <- subset(clean_election2, cand_nm =="Romney, Mitt")

obama <- subset(clean_election2, cand_nm =='Obama, Barack')


# [문제5] romney, obama 변수를 대상으로 병합하여 obama_romney 변수에 저장하시오.
# 힌트) rbind()
obama_romney <- rbind(romney, obama)


## 교차분석 ## 

# [문제6] 후원자의 직업군과 대통령 당선 유무에 따라서 다음과 같이 파생변수를 만드시오.
# <조건1> 대상 변수 : obama_romney

# <조건2> 다음과 같은 후원자의 직업군을 job1, job2, job3로 리코딩하여 contbr_occupation2 칼럼 저장 
# job1 : INVESTOR - 투자자, EXECUTIVE - 경영진, PRESIDENT  - 회장 
# job2 : LAWYER - 변호사, PHYSICIAN  - 내과의사, ATTORNEY   - 변호사
# job3 : RETIRED  - 퇴직자, HOMEMAKER  - 주부

# job1 리코딩 
obama_romney$contbr_occupation2[obama_romney$contbr_occupation=='INVESTOR'] <- 'job1'
obama_romney$contbr_occupation2[obama_romney$contbr_occupation=='EXECUTIVE'] <- 'job1'
obama_romney$contbr_occupation2[obama_romney$contbr_occupation=='PRESIDENT'] <- 'job1'

obama_romney$contbr_occupation2[obama_romney$contbr_occupation=='LAWYER'] <- 'job2'
obama_romney$contbr_occupation2[obama_romney$contbr_occupation=='PHYSICIAN'] <- 'job2'
obama_romney$contbr_occupation2[obama_romney$contbr_occupation=='ATTORNEY'] <- 'job2'

obama_romney$contbr_occupation2[obama_romney$contbr_occupation=='RETIRED'] <- 'job3'
obama_romney$contbr_occupation2[obama_romney$contbr_occupation=='HOMEMAKER'] <- 'job3'


# <조건3> contbr_occupation2 칼럼에 NA를 포함한 관측( 제거 후 서브셋 작성(obama_romney2 저장)  
obama_romney2 <- subset(obama_romney, !is.na(contbr_occupation2))

# <조건4> obama_romney2 변수를 대상으로 cand_nm 칼럼이 'Obama, Barack'이면 '당선', 
#               'Romney, Mitt'이면 '낙선'으로 파생변수를 생성하여 cand_pass 칼럼 추가
obama_romney2$cand_pass[obama_romney2$cand_nm =='Obama, Barack'] <- '당선'
obama_romney2$cand_pass[obama_romney2$cand_nm =='Romney, Mitt'] <- '낙선'


# [문제7]  [문제6]에서 만든 파생변수(직업유형과 당선유무)를 이용하여 교차분할표를 작성하시오.  

table(obama_romney2$contbr_occupation2, obama_romney2$cand_pass)


## chisquare 검정 ##

# [문제8] 후원자의 직업군과 대통령 당선 유무 여부와 관련성이 있는가를 검정하시오.
# <조건1> 대상 변수 : obama_romney2
# <조건2> 귀무가설과 대립가설 수립 
# <조건3> 변수 모델링 : x변수(contbr_occupation2), y변수(cand_pass)
# <조건4> 검정결과 해석

# 귀무가설 : 직업의 유형과 대통령 당선과 관련성이 없다.
# 대립가설 : 직업의 유형과 대통령 당선과 관련성이 있다.
x <- obama_romney2$contbr_occupation2
y <- obama_romney2$cand_pass

chisq.test(x, y)
# X-squared = 224.12, df = 2, p-value < 2.2e-16
# p < 0.05 : 귀무가설 기각
#(해석) 직업의 유형과 대통령 당선과 관련성이 있다.

## lattice 패키지 ## 

# [문제9] lattice 패키지의 densityplot()함수를 이용하여 후원자의 직업유형별로 다음과 같이 후원금을 시각화하시오.
# <조건1> 대상 변수 : obama_romney2
# <조건2> 후원금이 300달러 ~ 3000달러 사이의 관측치 선정 -> obama_romney3 변수 저장  
# <조건3> obama_romney3 변수 대상 밀도그래프 시각화(x축 : 후원금, 조건 : 당선유무, 그룹 : 직업유형) 

library(lattice)

obama_romney3 <- subset(obama_romney2, contb_receipt_amt>=300 & contb_receipt_amt<=3000)

densityplot(~contb_receipt_amt | factor(cand_pass), 
            data=obama_romney3, groups = contbr_occupation2, 
            plot.points=T, auto.key = T) 


## 평균차이 검정 ## 

# [문제10] romney와 obama 후보자를 대상으로 후원자의 직업군이 'RETIRED'인 후원금에 차이가 있는지 검정하시오.
# <조건1> 대상 변수 : obama_romney3
# <조건2> 두집단 평균차이 검정
View(obama_romney3)

romney <- subset(obama_romney3, obama_romney3$cand_nm=="Romney, Mitt" & contbr_occupation=='RETIRED')
obama <- subset(obama_romney3, obama_romney3$cand_nm=="Obama, Barack" & contbr_occupation=='RETIRED')

romney_amt <- romney$contb_receipt_amt
obama_amt <- obama$contb_receipt_amt

var.test(romney_amt, obama_amt) 
# df = 797, p-value = 5.153e-07

wilcox.test(romney_amt, obama_amt)
# W = 212570, p-value < 2.2e-16
# p < 0.05 : 귀무가설 기각
# (해석)romney와 obama 후보자를 대상으로 후원자의 직업군이 'RETIRED'인 후원금에 차이가 있다.



