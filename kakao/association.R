
###################################################
# 연관분석(Association Analysis)
###################################################

# 연관성 규칙 분석을 위한 패키지
# install.packages("arules")
library(arules) #read.transactions()함수 제공


# 1. transaction 객체 생성(파일 이용)
setwd("C:/ITWILL/project/kakao_data")

# <실습> 중복 트랜잭션 객체 생성
# tran<- read.transactions("article.txt", format="basket", sep=" ")
tran<- read.transactions("article.csv", format="basket", sep=" ")

summary(tran)
#' transactions as itemMatrix in sparse format with
#' 3507098 rows (elements/itemsets/transactions) and
#' 505841 columns (items) and a density of 8.081055e-06 
#' 
#' most frequent items:
#'   @brunch_141     @brunch_151     @brunch_145   @tenbody_1305 @intlovesong_28 
#' 56782           35706           19891           17298           16017 
#' (Other) 
#' 14190372 
#' 
#' element (itemset/transaction) length distribution:
#'   sizes
#' 0       1       2       3       4       5       6       7       8       9 
#' 4998 1509387  538164  384138  214015  153436  130592   89713   71925   62665 
#' 10      11      12      13      14      15      16      17      18      19 
#' 47563   39791   34630   27895   23973   20653   17248   15014   12927   11376 
#' 20      21      22      23      24      25      26      27      28      29 
#' 9798    8585    7780    6722    5963    5172    4792    4209    3780    3335 
#' 30      31      32      33      34      35      36      37      38      39 
#' 3054    2647    2396    2162    1914    1846    1647    1464    1340    1216 
#' 40      41      42      43      44      45      46      47      48      49 
#' 1176    1080     946     901     769     781     743     655     649     569 
#' 50      51      52      53      54      55      56      57      58      59 
#' 503     455     408     415     373     319     318     287     301     259 
#' 60      61      62      63      64      65      66      67      68      69 
#' 253     225     207     201     213     164     167     181     148     149 
#' 70      71      72      73      74      75      76      77      78      79 
#' 155     129     126      98     133     112     109      86      87      85 
#' 80      81      82      83      84      85      86      87      88      89 
#' 81      83      68      82      69      55      57      51      48      42 
#' 90      91      92      93      94      95      96      97      98      99 
#' 61      46      49      36      33      45      36      44      39      45 
#' 100     101     102     103     104     105     106     107     108     109 
#' 39      35      32      35      31      25      26      24      20      33 
#' 110     111     112     113     114     115     116     117     118     119 
#' 27      23      20      22      29      13      14      24      21      16 
#' 120     121     122     123     124     125     126     127     128     129 
#' 15      14      18      12      16      13      14      12      12       5 
#' 130     131     132     133     134     135     136     137     138     139 
#' 14      11       9      11      10      11       9      11       8       6 
#' 140     141     142     143     144     145     146     147     148     149 
#' 12       6       6      10       9       9      12       9       5       6 
#' 150     151     152     153     154     155     156     157     158     159 
#' 10       5       2       7       9       7       3       1       2       6 
#' 160     161     162     163     164     165     166     167     168     169 
#' 7       6       7       4       2       3       2       4       2       4 
#' 170     171     172     173     174     175     176     177     178     179 
#' 4       1       3       3       1       2       5       3       5       4 
#' 180     181     182     183     184     185     186     187     188     189 
#' 6       3       3       4       4       1       3       5       3       1 
#' 190     191     193     194     195     196     197     198     199     200 
#' 5       1       1       4       3       1       5       4       3       2 
#' 201     202     203     204     205     206     207     209     210     211 
#' 3       8       1       1       2       3       2       2       1       1 
#' 212     213     214     216     217     219     220     221     222     224 
#' 1       2       1       5       2       2       2       3       2       2 
#' 225     226     227     228     230     231     232     233     235     238 
#' 2       1       3       5       2       3       1       2       4       1 
#' 239     240     241     242     243     244     246     248     249     250 
#' 1       1       1       2       1       2       4       2       1       1 
#' 251     252     253     255     256     257     260     261     262     263 
#' 2       1       3       4       3       1       2       1       1       1 
#' 265     266     272     277     280     281     282     283     285     286 
#' 1       1       2       1       1       1       2       1       2       1 
#' 287     288     291     294     295     301     305     306     307     309 
#' 2       3       1       1       2       1       2       2       1       1 
#' 320     322     324     325     332     335     336     337     340     343 
#' 1       1       1       1       1       1       1       1       1       1 
#' 351     353     354     361     365     372     380     382     388     397 
#' 1       1       1       1       1       1       1       1       1       1 
#' 433     451     523     591 
#' 1       1       1       1 
#' 
#' Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
#' 0.000   1.000   2.000   4.088   4.000 591.000 
#' 
#' includes extended item information - examples:
#'   labels
#' 1   #00700c454af49d5c9a36a13fcba01d0a_1
#' 2  #00700c454af49d5c9a36a13fcba01d0a_10
#' 3 #00700c454af49d5c9a36a13fcba01d0a_100





# 트랜잭션 보기
inspect(tran)
#' [3507097] {@rory_7}                              
#' [3507098] {@cliche-cliche_1,                     
#'   @cliche-cliche_5} 


# 규칙 발견
atran <- apriori(tran) # supp=0.1, conf=0.8와 동일함 
# Apriori
# 
# Parameter specification:
# confidence minval smax arem  aval originalSupport maxtime support minlen maxlen target   ext
#        0.8    0.1    1 none FALSE            TRUE       5     0.1      1     10  rules FALSE
# 
# Algorithmic control:
#   filter tree heap memopt load sort verbose
# 0.1 TRUE TRUE  FALSE TRUE    2    TRUE
# 
# Absolute minimum support count: 350709 
# 
# set item appearances ...[0 item(s)] done [0.00s].
# set transactions ...[505841 item(s), 3507098 transaction(s)] done [7.63s].
# sorting and recoding items ... [0 item(s)] done [0.11s].
# creating transaction tree ... done [0.09s].
# checking subsets of size 1 done [0.00s].
# writing ... [0 rule(s)] done [0.00s].
# creating S4 object  ... done [0.16s].

atran # set of 0 rules 
attributes(tran)
inspect(tran)

# 향상도(by="lift")가 높은 순서로 정렬 
inspect(sort(tran, by="lift"))
inspect(head(sort(tran, by="lift")))



##############################################
# 3. 연관규칙 시각화(Adult 데이터 셋 이용)
##############################################

# [data.frame 형식으로 보기] - 트랜잭션 데이터를 데이터프레임으로 변경 
astran<- as(tran, "data.frame") # data.frame형식으로 변경 
str(astran) #'data.frame':	3507098 obs. of  1 variable:
head(astran) # 칼럼 내용 보기 


#---------------------------------------------------------------
# 신뢰도 80%, 지지도 10%이 적용된 연관규칙 6137 발견   
#----------------------------------------------------------------
ar<- apriori(astran, parameter = list(supp=0.05, conf=0.7))
ar1<- apriori(astran, parameter = list(supp=0.2)) # 지도도 높임
ar2<- apriori(astran, parameter = list(supp=0.2, conf=0.95)) # 신뢰도 높임
ar3<- apriori(astran, parameter = list(supp=0.3, conf=0.95)) # 신뢰도 높임
ar4<- apriori(astran, parameter = list(supp=0.35, conf=0.95)) # 신뢰도 높임
ar5<- apriori(astran, parameter = list(supp=0.4, conf=0.95)) # 신뢰도 높임



chiyodad <- subset(ar, lhs %in% '@chiyodad_11')
chiyodad
inspect(chiyodad)



# 결과보기
inspect(head(ar5)) # 상위 6개 규칙 제공 -> inspect() 적용
#     lhs                       rhs                                   support confidence     lift count
# [1] {}                     => {capital-loss=None}                 0.9532779  0.9532779 1.000000 46560
# [2] {relationship=Husband} => {marital-status=Married-civ-spouse} 0.4034233  0.9993914 2.181164 19704
# [3] {relationship=Husband} => {sex=Male}                          0.4036485  0.9999493 1.495851 19715

# confidence(신뢰도) 기준 내림차순 정렬 상위 6개 출력
inspect(head(sort(ar5, decreasing=T, by="confidence")))
#     lhs                                    rhs                                   support confidence     lift count
# [1] {relationship=Husband}              => {sex=Male}                          0.4036485  0.9999493 1.495851 19715
# [2] {marital-status=Married-civ-spouse,                                                                           
# relationship=Husband}              => {sex=Male}                          0.4034028  0.9999492 1.495851 19703
# [3] {relationship=Husband}              => {marital-status=Married-civ-spouse} 0.4034233  0.9993914 2.181164 19704

# lift(향상도) 기준 내림차순 정렬 상위 6개 출력
inspect(head(sort(ar5, by="lift"))) 
#     lhs                                    rhs                                   support confidence     lift count
# [1] {marital-status=Married-civ-spouse,                                                                           
# sex=Male}                          => {relationship=Husband}              0.4034028  0.9901503 2.452877 19703
# [2] {relationship=Husband}              => {marital-status=Married-civ-spouse} 0.4034233  0.9993914 2.181164 19704
# [3] {relationship=Husband,                                                                                        
# sex=Male}                          => {marital-status=Married-civ-spouse} 0.4034028  0.9993913 2.181164 19703


## 연관성 규칙에 대한 데이터 시각화를 위한 패키지
#install.packages("arulesViz") 
library(arulesViz) # rules값 대상 그래프를 그리는 패키지

plot(ar3) # 지지도(support), 신뢰도(conf) , 향상도(lift)에 대한 산포도


plot(ar4, method="graph") #  연관규칙 네트워크 그래프
# 각 연관규칙 별로 연관성 있는 항목(item) 끼리 묶여서 네트워크 형태로 시각화


plot(ar5, method="graph") #36룰


# 룰이 너무 많으면 중심어를 기준으로 "subset"만들어서 연관분석가능
ar5_sub <- subset(ar5, lhs %in% 'workclass=Private') #lhs : 선행사건, rhs: 후행사건
ar5_sub # set of 9 rules 
plot(ar5_sub, method="graph")


#########################################
# 4. <<식료품점 파일 예제>> 
#########################################

library(arules)

# transactions 데이터 가져오기
data("Groceries")  # 식료품점 데이터 로딩
str(Groceries) 
# Formal class 'transactions' [package "arules"] with 3 slots
#<해석> transactions 객체구조, 3slots(data, itemInfo, itemsetInfo)
Groceries
# transactions in sparse format with
# 9835 transactions (rows) and  ---> 9835명의 거래 정보
# 169 items (columns) ---> 169 물건



# [data.frame 형 변환]
Groceries.df<- as(Groceries, "data.frame")
head(Groceries.df)
#                                                                  items
# 1              {citrus fruit,semi-finished bread,margarine,ready soups}
# 2                                        {tropical fruit,yogurt,coffee}
# 3                                                          {whole milk}
# 4                         {pip fruit,yogurt,cream cheese ,meat spreads}
# 5 {other vegetables,whole milk,condensed milk,long life bakery product}
# 6                      {whole milk,butter,yogurt,rice,abrasive cleaner}

summary(Groceries)
# most frequent items: (출현빈도 가장 높은)
# whole milk other vegetables       rolls/buns             soda 
#      2513             1903             1809             1715 
# yogurt          (Other) 
# 1372            34055 

#출현 빈도수 시각화 - 상위 20개 토픽
itemFrequencyPlot(Groceries, topN=20, type="absolute") 
#@@1

# 지지도 0.001, 신뢰도 0.8
rules <- apriori(Groceries, parameter=list(supp=0.001, conf=0.8))
inspect(rules) #410개 룰

# 규칙을 구성하는 왼쪽(LHS) -> 오른쪽(RHS)의 item 빈도수 보기  
plot(rules, method="grouped")
#@@2

# 최대 길이 3이내(maxlen=3)로 규칙 생성
rules <- apriori(Groceries, parameter=list(supp=0.001, conf=0.80, maxlen=3))
inspect(rules) # 29개 규칙(29 rule)

# 신뢰도(by="confidence") 기준 "내림차순(decreasing=T)"으로 규칙 정렬
rules <- sort(rules, decreasing=T, by="confidence")
inspect(rules) 

library(arulesViz) # rules값 대상 그래프를 그리는 패키지
plot(rules, method="graph", control=list(type="items"))
#@@3

#######################################
### 특정 item 서브셋 작성/시각화
#######################################
# ★특정 item : subset(rules 객체, rhs (or lhs) %in% '단어') 
#               subset(rules 객체, rhs (or lhs) %pin% '단어') 



# 오른쪽 item이 전지분유(whole milk)인 규칙만 서브셋으로 작성
wmilk <- subset(rules, rhs %in% 'whole milk') # lhs : 왼쪽 item
wmilk # set of 18 rules 
inspect(wmilk)
#@@4
plot(wmilk, method="graph") #  연관 네트워크 그래프

# 오른쪽 item이 other vegetables인 규칙만 서브셋으로 작성
oveg <- subset(rules, rhs %in% 'other vegetables') # lhs : 왼쪽 item
oveg # set of 10 rules 
inspect(oveg)
plot(oveg, method="graph") #  연관 네트워크 그래프

# 왼쪽 item이 'butter', 'yogurt' 둘중 하나 포함 => 2개 이상 일때 c() 묶어주면 됨.(or)
but_yog <- subset(rules, lhs %in% c('butter', 'yogurt'))
but_yog # set of 4 rules 
inspect(but_yog)
#     lhs                 rhs                support     confidence lift     count
# [1] {butter,jam}     => {whole milk}       0.001016777 0.8333333  3.261374 10   
# [2] {butter,rice}    => {whole milk}       0.001525165 0.8333333  3.261374 15   
# [3] {yogurt,rice}    => {other vegetables} 0.001931876 0.8260870  4.269346 19   
# [4] {yogurt,cereals} => {whole milk}       0.001728521 0.8095238  3.168192 17   

plot(but_yog, method = "graph")
