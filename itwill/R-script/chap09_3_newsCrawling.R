# chap09_3_newsCrawling

# &&& 그림 9-3-1

# https://media.daum.net/
# <a href="url"> 기사 내용 </a>


# 1. 패키지 설치
install.packages('httr') # 원격 url 요청
library(httr)

install.packages('XML') # tag -> html 파싱
library(XML)

# 2. url 요청 (https://media.daum.net 요청)
url <- "https://media.daum.net"
web <- GET(url) # 소스 받아옴
# &&& 그림_소스

web
# Response [https://media.daum.net]
# Date: 2020-03-18 06:46
# Status: 200
# Content-Type: text/html;charset=UTF-8
# Size: 81.4 kB

# 3. html 파싱(text -> html)
help("htmlTreeParse")
# htmlTreeParse(file, ignoreBlanks=TRUE, handlers=NULL, replaceEntities=FALSE,
#               asText=FALSE, trim=TRUE, validate=FALSE, getDTD=TRUE,
#               isURL=FALSE, asTree = FALSE, addAttributeNamespaces = FALSE,
#               useInternalNodes = FALSE, isSchema = FALSE,
#               fullNamespaceInfo = FALSE, encoding = character(),
#               useDotNames = length(grep("^\\.", names(handlers))) > 0,
#               xinclude = TRUE, addFinalizer = TRUE, error = htmlErrorHandler,
#               isHTML = TRUE, options = integer(), parentFirst = FALSE)


html <- htmlTreeParse(web, useInternalNodes = T, trim=TRUE, encoding = "utf-8")

# trim=TRUE : 앞뒤 공백 제거
# &&& 그림 9-3-2

html
# &&& 그림 9-3-4


root_node <- xmlRoot(html)

# 4. tag 자료 수집 : "//tag[@속성='값']"
news <- xpathSApply(root_node,"//a[@ class='link_txt']", xmlValue)
# &&& 그림 9-3-3
news

news2 <- news[1:59]
news2
# &&& 그림 9-3-5

# 5. news 전처리
news_sent = gsub('[[\n\r\t]]', '', news2) #이스케이프 제거
news_sent = gsub('[[:punct:]]', '', news_sent) #문장부호 제거(문장부호->공백으로 교체)
news_sent = gsub('[[:cntrl:]]', '', news_sent) #특수문자 제거
news_sent = gsub('[[a-z]]', '', news_sent) #영문 제거(소문자)
news_sent = gsub('[[A-Z]]', '', news_sent) #영문 제거(대문자)
news_sent = gsub('\\s+', ' ', news_sent) #2개이상 공백 -> 1개 공백

news_sent
# &&& 그림 9-3-6

# 6. file save
setwd("C:/ITWILL/2_Rwork/output")

# 행 번호와 텍스트 저장
write.csv(news_sent, 'news_data.csv', row.names = T, quote = F)

news_data <- read.csv('news_data.csv')
head(news_data)

colnames(news_data) <- c('no', 'news_txt')
head(news_data)

news_txt <- news_data$news_txt
news_txt

# 7. 토픽분석 -> 단어 구름 시각화(1day)
library(KoNLP) 
library(tm) 
library(wordcloud)


# 신규 단어
user_dic <- data.frame(term=c("팬데믹", "코로나1", "타다"), tag='ncn')
buildDictionary(ext_dic='sejong', user_dic = user_dic)


exNouns <- function(x) { 
  paste(extractNoun(as.character(x)), collapse=" ")
}
news_nouns <- sapply(news_txt, exNouns) 
news_nouns

news_Corpus <- Corpus(VectorSource(news_nouns))  
# 전처리는 앞서 이미 함.
# - 참고 -
# news_sent = gsub('[[\n\r\t]]', '', news2) #이스케이프 제거
# news_sent = gsub('[[:punct:]]', '', news_sent) #문장부호 제거(문장부호->공백으로 교체)
# news_sent = gsub('[[:cntrl:]]', '', news_sent) #특수문자 제거
# news_sent = gsub('[[a-z]]', '', news_sent) #영문 제거(소문자)
# news_sent = gsub('[[A-Z]]', '', news_sent) #영문 제거(대문자)
# news_sent = gsub('\\s+', ' ', news_sent) #2개이상 공백 -> 1개 공백


news_CorpusPrepro_term <- TermDocumentMatrix(news_Corpus,
                                control=list(wordLengths=c(4,20))) 

news_Term_df <- as.data.frame(as.matrix(news_CorpusPrepro_term)) 

news_Result <- sort(rowSums(news_Term_df), decreasing=TRUE) 
news_Result[1:10]

news_Name <- names(news_Result) 
news.df <- data.frame(word=news_Name, freq=news_Result)

pal <- brewer.pal(12,"Paired")
windowsFonts(malgun=windowsFont("맑은 고딕"))

x11()
wordcloud(news.df$word, news.df$freq, 
          scale=c(5,1), min.freq=2, random.order=F, 
          rot.per=.1, colors=pal, family="malgun")
# &&& 그림-구름


