#################################
## <제14장 연습문제>
################################# 

# 01. 다음 mtcars 데이터셋을 대상으로 
# 연비효율(mpg), 실린더수(cyl), 엔진크기(disp), 마력(hp), 무게(wt) 변수를 
# 대상으로 서브셋을 작성하시오.
library(datasets)
data(mtcars)
head(mtcars)

mtcars_data <- data.frame(mtcars$mpg, mtcars$cyl, mtcars$disp, mtcars$hp, mtcars$wt)
head(mtcars_data)

# 02. 작성된 서브셋을 대상으로 상관분석을 수행하여 연비효율(mpg)과 가장 상관계수가 
# 높은 변수를 확인하시오. 
cor(mtcars_data)
#             mtcars.mpg mtcars.cyl mtcars.disp  mtcars.hp  mtcars.wt
# mtcars.mpg   1.0000000 -0.8521620  -0.8475514 -0.7761684 -0.8676594
# mtcars.cyl  -0.8521620  1.0000000   0.9020329  0.8324475  0.7824958
# mtcars.disp -0.8475514  0.9020329   1.0000000  0.7909486  0.8879799
# mtcars.hp   -0.7761684  0.8324475   0.7909486  1.0000000  0.6587479
# mtcars.wt   -0.8676594  0.7824958   0.8879799  0.6587479  1.0000000
#(해석)  연비효율(mpg)과 가장 상관계수가 높은 변수는 mtcars.wt(-0.8676594) 이다.

# 03. 연비효율과 가장 상관계수가 높은 변수와 산점도로 시각화하시오.
plot(mtcars$mpg, mtcars$wt)
#@@19









