####################################
## 제16-2장 RandomForest 연습문제 
####################################

# 01. 400개의 Tree와 4개의 분류변수를 파라미터로 지정하여 모델을 생성하고, 
#       분류정확도를 구하시오.
#  조건> 1,2,22,23 칼럼을 제외하여 데이터 셋 구성 

weatherAUS = read.csv(file.choose()) # weatherAUS.csv 

weatherAUS = weatherAUS[ ,c(-1,-2, -22, -23)]
str(weatherAUS)
# 'data.frame':	36881 obs. of  20 variables:

# y변수 : RainTomorrow (범주형)

sqrt(19) # 4.358899 >> 4 or 5
model <- randomForest(RainTomorrow~., data=weatherAUS, 
                      ntree=400, mtry=4, importance=T, na.action=na.omit)
model
# Type of random forest: classification
# Number of trees: 400
# No. of variables tried at each split: 4
# 
# OOB estimate of  error rate: 14.06%  ---> 오차 14% 정도
# Confusion matrix:
#        No  Yes class.error
# No  12587  839  0.06249069
# Yes  1605 2347  0.40612348

names(model)
# [1] "call"            "type"           
# [3] "predicted"       "err.rate"       
# [5] "confusion"       "votes"          
# [7] "oob.times"       "classes"        
# [9] "importance"      "importanceSD"   
# [11] "localImportance" "proximity"      
# [13] "ntree"           "mtry"           
# [15] "forest"          "y"              
# [17] "test"            "inbag"          
# [19] "terms"           "na.action" 

pred <- model$predicted
true <- model$y 

tab <- table(true, pred)
tab
#        pred
# true     No   Yes
#   No  12587   839
#   Yes  1605  2347

acc <- (tab[1,1]+ tab[2,2]) / sum(tab)
acc #  0.8593624

# 02. 변수의 중요도 평가를 통해서 가장 중요한 변수를 확인하고, 시각화 하시오. 

importance(model)
# MeanDecreaseGini상위 4변수 select
# Humidity3pm           985.4648
# Sunshine              650.8168
# WindDir9am            413.1843
# WindGustDir           397.5425

varImpPlot(model)
#@@12




