setwd("C:/ITWILL/4_Python-II/workspace/gongmo/data")
#df_plant1_24
df <- read.csv(file.choose())

str(df)

dim(df)

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


