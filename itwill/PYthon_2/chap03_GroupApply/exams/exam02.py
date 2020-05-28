'''
문2) weatherAUS.csv 데이터셋을 이용하여 다음 단계를 해결하시오.
   <단계1> 지역(Location)별 빈도수 구하기
     사용 함수 : value_counts()
     
   <단계2> 2개 칼럼(Location과  RainToday) -> DF 전체 칼럼 그룹화
     사용 함수 : groupby()
   <단계3> 그룹화 객체를 대상으로 평균 구하기   
                                  MinTemp    MaxTemp  ...    Temp3pm    RISK_MM
    Location      RainToday                        ...                      
    Adelaide      No         13.340847  24.313011  ...  22.917576   0.927778
                  Yes        11.426263  17.780402  ...  16.484422   3.426667
    Albany        No         13.433688  21.001590  ...  19.294128   1.488339
                  Yes        11.560593  17.345763  ...  15.878723   4.282627
                  
   <단계4> 그룹화 결과를 대상으로 테이블 형식으로 변경 
     사용 함수 : size().unstack()
    <<출력 결과>>
     RainToday          No  Yes
     Location                  
     Adelaide          661  199
     Albany            566  236
     Albury            615  169
     AliceSprings      693   99
     BadgerysCreek     596  158
     Ballarat          586  223
     Bendigo           658  153 
          : 
   <단계5> 단계4의 결과를 대상으로 가로막대 누적형 차트 그리기
'''
import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv("weatherAUS.csv")
weather.info()

# <단계1> 지역(Location)별 빈도수 구하기
Location = weather['Location']
# Location_counts() - error
Location.value_counts()
'''
Canberra            1085
Sydney               971
Melbourne            904
Perth                899
Hobart               893
Brisbane             887
Adelaide             887
...

'''

weather.groupby('Location').size()
'''
Adelaide             887
Albany               802
Albury               795
AliceSprings         792
BadgerysCreek        788
Ballarat             813
Bendigo              811
...

'''

grp = weather.groupby(['Location', 'RainToday'])
grp.mean()
'''
                         MinTemp    MaxTemp  ...    Temp3pm   RISK_MM
Location    RainToday                        ...                     
Adelaide    No         13.340847  24.313011  ...  22.917576  0.927778
            Yes        11.426263  17.780402  ...  16.484422  3.426667
Albany      No         13.433688  21.001590  ...  19.294128  1.488339
            Yes        11.560593  17.345763  ...  15.878723  4.282627
Albury      No          9.859283  24.100493  ...  22.981789  1.263816
                         ...        ...  ...        ...       ...
Witchcliffe Yes        10.238614  17.568317  ...  15.618812  5.864356
Wollongong  No         14.960440  21.688419  ...  20.099069  1.997363
            Yes        14.817778  20.053889  ...  18.818539  8.737079
Woomera     No         13.565385  26.901994  ...  25.491738  0.313960
            Yes        12.393220  22.220339  ...  20.548276  1.932203
'''

grp_cross = grp.size().unstack()
'''
RainToday          No  Yes
Location                  
Adelaide          661  199
Albany            566  236
Albury            615  169
AliceSprings      693   99
BadgerysCreek     596  158
Ballarat          586  223
Bendigo           658  153
Brisbane          665  218
Cairns            543  262
...

'''

grp_cross.plot(kind='barh', stacked=True)
