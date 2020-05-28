# -*- coding: utf-8 -*-
"""
문) tree_data.csv 파일의 변수를 이용하여 아래 조건으로 DecisionTree model를 생성하고,
    의사결정 tree 그래프를 시각화하시오.
    
 <변수 선택>   
 x변수 : iq수치, 나이, 수입, 사업가유무, 학위유무
 y변수 : 흡연유무
 
 <그래프 저장 파일명> : smoking_tree_graph.dot
"""

import pandas as pd

tree_data = pd.read_csv("C:/ITWILL/4_Python-II/data/tree_data.csv")
print(tree_data.info())
'''
iq         6 non-null int64 - iq수치
age        6 non-null int64 - 나이
income     6 non-null int64 - 수입
owner      6 non-null int64 - 사업가 유무
unidegree  6 non-null int64 - 학위 유무
smoking    6 non-null int64 - 흡연 유무
'''

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

x = tree_data.iloc[:,:5]
x
y = tree_data.iloc[:,5]
y

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)


dt = DecisionTreeClassifier()
model = dt.fit(x, y)

pred = model.predict(x)
acc=accuracy_score(y, pred)
acc # 1.0

tree.plot_tree(model)
#@@12

x_col = x.columns
x_col[2] #  'income'
x_col[1] # 'age'

export_graphviz(model, out_file='smoking_tree_graph.dot', feature_names=x_col)
#@@13

dt = DecisionTreeClassifier(criterion='entropy')
model = dt.fit(x, y)

pred = model.predict(x)
acc=accuracy_score(y, pred)
acc

tree.plot_tree(model)
#@@14

export_graphviz(model, out_file='smoking_tree_graph2.dot', feature_names=x_col)
#@@15
