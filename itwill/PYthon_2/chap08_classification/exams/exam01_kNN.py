'''
문) 다음과 같은 3개의 범주를 갖는 6개의 데이터 셋을 대상으로 kNN 알고리즘을 적용하여 
      특정 품목을 분류하시오.
   (단계1 : 함수 구현  -> 단계2 : 클래스 구현)  
      
    <조건1> 데이터 셋  
    -------------------------
          품목     단맛 아삭거림 분류범주
    -------------------------
    grape   8   5     과일
    fish    2   3     단백질 
    carrot  7   10    채소
    orange  7   3     과일 
    celery  3   8     채소
    cheese  1   1     단백질 
    ------------------------
    
   <조건2> 분류 대상과 k값은 키보드 입력  
   
  <<출력 예시 1>> k=3인 경우
  -----------------------------------
    단맛 입력(1~10) : 8
    아삭거림 입력(1~10) : 4
  k값 입력(1 or 3) : 3
  -----------------------------------
  calssCount: {'과일': 2, '단백질': 1}
   분류결과: 과일
  -----------------------------------
  
  <<출력 예시 2>> k=1인 경우
  -----------------------------------
   단맛 입력(1~10) : 2
   아삭거림 입력(1~10) :3
  k값 입력(1 or 3) : 1
  -----------------------------------
  calssCount: {'단백질': 1}
   분류결과 : 단백질
  -----------------------------------
'''

grape = [8, 5]
fish = [2, 3]
carrot = [7, 10]
orange = [7, 3]
celery = [3, 8]
cheese = [1, 1]
class_category = ['과일', '단백질', '채소', '과일', '채소', '단백질']

import numpy as np

know = np.array([grape, fish, carrot, orange, celery, cheese])
cate = np.array(class_category)

while True : 
    
    a=int(input("단맛 입력(1~10) : "))
    if a == 0 :
        print('반복 종료')
        break
    b=int(input("아삭거림 입력(1~10) :"))
    k=int(input("k값 입력(1 or 3) : "))
    
    c=[a, b]
    not_know = np.array([c])
    
    def knn_classify(know, not_know, cate, k) :
        # 단계1 : 거리계산식
        diff = know - not_know 
        square_diff = diff**2
        sum_square_diff = square_diff.sum(axis = 1)
        distance = np.sqrt(sum_square_diff)
        
        # 단계 2 : 오름차순 정렬 -> index
        sortDist = distance.argsort()
        
        # 단계 3 : 최근접 이웃(k=3)
        class_result = {}
        for i in range(k) :
            key = cate[sortDist[i]]
            class_result[key] = class_result.get(key, 0)+1 # 카테고리 빈도수 계산
        
        return class_result
            
    import operator
    # 함수 결과 확인
    class_result = knn_classify(know, not_know, cate, k)
    print('calssCount : ', class_result) 
    #print('분류결과 : ', max(class_result.iteritems(), key = operator.itemgetter(1))[0])
    print('분류결과 : ', max(class_result , key=class_result.get))


