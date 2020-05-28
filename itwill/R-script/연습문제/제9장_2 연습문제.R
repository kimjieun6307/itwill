#################################
## <제9장-2 연습문제>
################################# 


# 01. 트럼프 연설문(trump.txt)과 오바마 연설문(obama.txt)을 대상으로 
# 빈도수가 2회 이상 단어를 대상으로 단어구름 시각화하시오.

library(tm)
library(wordcloud) 

trump <- file(file.choose(), encoding="UTF-8")
trump_data <- readLines(trump) 

exNouns <- function(x) { 
  paste(extractNoun(as.character(x)), collapse=" ")
}

trump_nouns <- sapply(trump_data, exNouns) 

myCorpus <- Corpus(VectorSource(trump_nouns))  

myCorpusPrepro <- tm_map(myCorpus, removePunctuation) 
myCorpusPrepro <- tm_map(myCorpusPrepro, removeNumbers) 
myCorpusPrepro <- tm_map(myCorpusPrepro, tolower) 
myCorpusPrepro <-tm_map(myCorpusPrepro, removeWords, stopwords('english')) 


myCorpusPrepro_term <- TermDocumentMatrix(myCorpusPrepro, 
                                          control=list(wordLengths=c(1,16))) 

myTerm_df <- as.data.frame(as.matrix(myCorpusPrepro_term)) 

wordResult <- sort(rowSums(myTerm_df), decreasing=TRUE) 
wordResult

myName <- names(wordResult) 
word.df <- data.frame(word=myName, freq=wordResult)

pal <- brewer.pal(12,"Paired")
wordcloud(word.df$word, word.df$freq, 
          scale=c(5,1), min.freq=2, random.order=F, 
          rot.per=.1, colors=pal)

############################################################

obama <- file(file.choose(), encoding="UTF-8")
obama_data <- readLines(obama)

myCorpus <- Corpus(VectorSource(obama_data))  

myCorpusPrepro <- tm_map(myCorpus, removePunctuation) 
myCorpusPrepro <- tm_map(myCorpusPrepro, removeNumbers) 
myCorpusPrepro <- tm_map(myCorpusPrepro, tolower) 
myCorpusPrepro <-tm_map(myCorpusPrepro, removeWords, stopwords('english')) 


myCorpusPrepro_term <- TermDocumentMatrix(myCorpusPrepro, 
                                          control=list(wordLengths=c(2,30))) 

myTerm_df <- as.data.frame(as.matrix(myCorpusPrepro_term)) 

wordResult <- sort(rowSums(myTerm_df), decreasing=TRUE) 
wordResult[1:10]

myName <- names(wordResult) 
word.df <- data.frame(word=myName, freq=wordResult)

pal <- brewer.pal(12,"Paired")
wordcloud(word.df$word, word.df$freq, 
          scale=c(5,1), min.freq=2, random.order=F, 
          rot.per=.1, colors=pal)




# 02. 공공데이터 사이트에서 관심분야 데이터 셋을 다운로드 받아서 빈도수가 5회 이상 단어를 이용하여 
#      단어 구름으로 시각화 하시오.
# 공공데이터 사이트 : www.data.go.kr


jupiter <- file(file.choose(), encoding="UTF-8")
jupiter_data <- readLines(jupiter) 

exNouns <- function(x) { 
  paste(extractNoun(as.character(x)), collapse=" ")
}

jupiter_nouns <- sapply(jupiter_data, exNouns) 

myCorpus <- Corpus(VectorSource(jupiter_nouns))  

myCorpusPrepro <- tm_map(myCorpus, removePunctuation) 
myCorpusPrepro <- tm_map(myCorpusPrepro, removeNumbers) 
myCorpusPrepro <- tm_map(myCorpusPrepro, tolower) 
myCorpusPrepro <-tm_map(myCorpusPrepro, removeWords, stopwords('english')) 


myCorpusPrepro_term <- TermDocumentMatrix(myCorpusPrepro, 
                                          control=list(wordLengths=c(4,20))) 

myTerm_df <- as.data.frame(as.matrix(myCorpusPrepro_term)) 

wordResult <- sort(rowSums(myTerm_df), decreasing=TRUE) 
wordResult[1:10]

myName <- names(wordResult) 
word.df <- data.frame(word=myName, freq=wordResult)

pal <- brewer.pal(12,"Paired")
windowsFonts(malgun=windowsFont("맑은 고딕"))

wordcloud(word.df$word, word.df$freq, 
          scale=c(5,1), min.freq=2, random.order=F, 
          rot.per=.1, colors=pal, family="malgun")





