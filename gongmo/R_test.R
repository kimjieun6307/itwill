# df_plant1_24.csv
df <- read.csv(file.choose())

str(df)
dim(df) #173665  10

df<-df[,3:10]
dim(df) # 173665  8

df_x <- df[, 1:5]
str(df_x)

df_y <- df['X24hourloc']
str(df_y)

table(complete.cases(df_x))
#  TRUE 
# 173665 


pr2<-prcomp(df_x)
summary(pr2)
# Importance of components:
#                           PC1     PC2     PC3     PC4     PC5
# Standard deviation     22.0865 16.2408 5.91516 1.21039 0.56533
# Proportion of Variance  0.6188  0.3346 0.04438 0.00186 0.00041
# Cumulative Proportion   0.6188  0.9534 0.99774 0.99959 1.00000

print(pr2)
# Standard deviations (1, .., p=5):
# [1] 22.0864505 16.2407912  5.9151553  1.2103903  0.5653336

# Rotation (n x k) = (5 x 5):
#                 PC1        PC2        PC3        PC4        PC5
# loc_tem       0.2908761  0.4758637  0.1667701 -0.2844316 -0.7617291
# out_tem       0.2915518  0.5325358 -0.1768469 -0.4997680  0.5919124
# loc_coil_temp 0.3042512  0.4607545  0.2453475  0.7791805  0.1667901
# loc_hum       0.5569921 -0.2132480 -0.7656429  0.1832065 -0.1565614
# out_hum       0.6538958 -0.4818609  0.5426864 -0.1692450  0.1306830

plot(pr2, type="l", sub = "Scree Plot")

df<-data.frame(df_x, df_y)
str(df)
# 'data.frame':	173665 obs. of  6 variables:
# $ loc_tem      : num  16 14 13 13 16 18 17 16 15 14 ...
# $ out_tem      : num  9 7 6 18 18 17 12 11 10 10 ...
# $ loc_coil_temp: num  11 10 10 10 10 14 14 12 12 10 ...
# $ loc_hum      : num  24 28 33 33 28 24 28 38 41 41 ...
# $ out_hum      : num  42 59 56 30 20 23 52 55 57 54 ...
# $ X24hourloc   : num  0 0 0 0 0 0 0 0 0 0 ...


table(df$X24hourloc)
#     0      1 
# 172282   1383 

nearZeroVar(df, saveMetrics = T)
#                freqRatio percentUnique zeroVar   nzv
# loc_tem         1.133523   0.845305617   FALSE FALSE
# out_tem         1.083333   0.933406271   FALSE FALSE
# loc_coil_temp   1.002770   0.645495638   FALSE FALSE
# loc_hum         1.023697   1.432643308   FALSE FALSE
# out_hum         1.005882   1.497135289   FALSE FALSE
# X24hourloc    124.571222   0.001151643   FALSE  TRUE






