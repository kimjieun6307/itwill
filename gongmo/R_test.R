# df_plant1_24.csv
df <- read.csv(file.choose())

str(df)
dim(df) #173665  10

df<-df[,3:10]
dim(df) # 173665  8









