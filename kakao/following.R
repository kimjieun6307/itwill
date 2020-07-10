library(arules) #read.transactions()함수 제공

setwd("C:/ITWILL/project/kakao_data")

tran<- read.transactions("following_list.csv", format="basket", sep=",")
summary(tran)
# transactions as itemMatrix in sparse format with
# 310759 rows (elements/itemsets/transactions) and
# 132446 columns (items) and a density of 7.550247e-06 
# 
# most frequent items:
#   [@brunch]                         [] 
# 117144                       7268 
# ['@seochogirl', '@brunch']  ['@readme999', '@brunch'] 
# 1087                        864 
# ['@tenbody', '@brunch']                    (Other) 
# 768                     183628 
# 
# element (itemset/transaction) length distribution:
#   sizes
# 1 
# 310759 
# 
# Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
# 1       1       1       1       1       1 
# 
# includes extended item information - examples:
#   labels
# 1 ['@008hood', '@banggl', '@gh-kim', '@may-day', '@aou', '@junglelife', '@greenpeacekorea', '@seoulsale', '@toosim', '@julieted17', '@traininglab', '@theedit', '@pomnyun', '@brunchqxk5', '@brunch']
# 2                                                                                                                                                                             ['@008hood', '@brunch']
# 3                                                                                                                                                                  ['@00books', '@miyath', '@brunch']

inspect(tran)


