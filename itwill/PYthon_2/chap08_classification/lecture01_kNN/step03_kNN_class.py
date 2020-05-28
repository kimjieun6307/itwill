# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:40:23 2020

@author: user
"""
# from module import function
from step01_kNN_data import data_set
import numpy as np

# dataset
know, not_know, cate = data_set()


class kNNClassify : 
    # 생성자, 멤버(메서드, 변수)
    def classify(self, know, not_know, cate, k=3) : 
        # 단계1 : 거리계산식
        diff = know - not_know 
        square_diff = diff**2
        sum_square_diff = square_diff.sum(axis = 1)
        distance = np.sqrt(sum_square_diff)
        
        # 단계 2 : 오름차순 정렬 -> index
        sortDist = distance.argsort()
        
        # 단계 3 : 최근접 이웃
        self.class_result = {} # 멤버 메서드
        for i in range(k) :
            key = cate[sortDist[i]]
            self.class_result[key] = self.class_result.get(key, 0)+1
            
    def vote(self) :
        vote_re = max(self.class_result)
        print('분류 결과 : ', vote_re)


# class 객체 생성 : 생성자 이용
knn = kNNClassify()
knn.classify(know, not_know, cate) # class_result 생성
knn.class_result # {'B': 2, 'A': 1}
knn.vote() # 분류 결과 :  B





















