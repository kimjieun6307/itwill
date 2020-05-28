#################################
## <제8장 연습문제>
################################# 

#01. 다음 조건에 맞게 airquality 데이터 셋의 Ozone과 Wind 변수를 대상으로  
# 다음과 같이 산점도로 시각화 하시오.

#조건1) y축 : Ozone 변수, x축 : Wind 변수 
#조건2) Month 변수를 factor형으로 변경  
#조건3) Month 변수를 이용하여 5개 격자를 갖는 산점도 그래프 그리기

head(airquality)
str(airquality)

dotplot(Ozone~Wind, airquality)
# &&& 1
dotplot(Ozone~Wind|factor(Month), airquality)
# &&& 2

xyplot(Ozone ~ Wind, data=airquality) 
# &&& 3
xyplot(Ozone ~ Wind | factor(Month), data=airquality)
# &&& 4

airquality_factor <- transform(airquality, Month=factor(Month))

dotplot(Ozone~Wind|factor(Month), airquality_factor)
xyplot(Ozone ~ Wind | factor(Month), data=airquality_factor)



# 02. 서울지역 4년제 대학교 위치 정보(Part-II/university.csv) 파일을 이용하여 레이어 형식으로 시각화 하시오.

# 조건1) 지도 중심 지역 SEOUL, zoom=11
# 조건2) 위도(LAT), 경도(LON)를 이용하여 학교의 포인트 표시
# 조건3) 각 학교명으로 텍스트 표시
# 조건4) 완성된 지도를 "university.png"로 저장하기(width=10.24,height=7.68) 

library(ggmap)

university <- read.csv(file.choose())
str(university)
head(university)

seoul <- c(left = 126.77, bottom = 37.40, 
           right = 127.17, top = 37.70)
uni_map <- get_stamenmap(seoul, zoom=11,  maptype='watercolor')
uni_lay1 <- ggmap(uni_map)
uni_lay2 <-uni_lay1 + geom_point(data=university, aes(x=LON, y=LAT, 
                                color='학교명'))

uni_lay2
uni_lay3 <- uni_lay2 + geom_text(data=university, 
                                 aes(x=LON+0.01, y=LAT+0.05, label='학교명'))
                                 
uni_lay3

names(university) <- c('school', 'lat', 'lon')
university
uni_lay3 <- uni_lay2 + geom_text(data=university, 
                                 aes(x=lon+0.01, y=lat+0.05, label='school'))

uni_lay3

uni_lay3 <- uni_lay2 + geom_text(data=university, 
                                 aes(x=lon+0.01, y=lat, label=school))


ggsave("university.png", width=10.24,height=7.68)
