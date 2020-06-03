setwd("C:/ITWILL/4_Python-II/workspace/gongmo/data")
#df_plant1_24
df <- read.csv(file.choose())

str(df)

dim(df) #173665  10

head(df)

table(df$X24hourloc)

summary(df)
boxplot(df$loc_tem)
boxplot(df$out_tem)
boxplot(df$loc_coil_temp)
boxplot(df$loc_hum)

model <- lm(loc_hum ~ loc_coil_temp, data = df)
plot(model)

install.packages("caret", dependencies=TRUE)
library(caret)
featurePlot(df[, 3:7], df$X24hourloc)


#df_plant1_24
df <- read.csv(file.choose())
head(df)

df<-df[,3:10]
dim(df) # 173665      8

str(df)

df_x <- df[, 1:5]
str(df_x)

df_y <- df['X24hourloc']
str(df_y)


pr<-princomp(df_x)
summary(pr)
pr$scores[,1:2]
print(pr)
plot(pr, type="l", sub = "Scree Plot")


pr2<-prcomp(df_x)
summary(pr2)
print(pr2)
plot(pr2, type="l", sub = "Scree Plot")





head(df_x)

table(complete.cases(df_x))

df<-data.frame(df_x, df_y)
str(df)
table(df$X24hourloc)

library(caret)
nearZeroVar(df, saveMetrics = T)







