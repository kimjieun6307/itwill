# -*- coding: utf-8 -*-
"""
Decision Tredd 모델
★ 중요 변수 선정
 - 중요변수 선정 기준 : GINI, Entropy => 작을수록 불확실성이 낮다
 - GINI : 불확실성을 개선하는데 기여하는 척도
 - Entropy :  불확실성을 나타내는 척도
"""

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris, load_wine # dataset
from sklearn.tree import DecisionTreeClassifier # tree model
from sklearn.metrics import accuracy_score, confusion_matrix

# tree 시각화 관련
from sklearn.tree.export import export_text
from sklearn import tree


iris=load_iris()
iris.target_names # ['setosa', 'versicolor', 'virginica']

x = iris.data
y = iris.target

x.shape # (150, 4)


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)


help(DecisionTreeClassifier)
'''
criterion : {"gini", "entropy"}, default="gini" 
max_depth : int, default=None # 트리 깊이=> 크면클수록 분류정확도 좋은(but, 오버피팅)
min_samples_split : int or float, default=2 # 가지치기
'''

dtc = DecisionTreeClassifier(criterion='gini',random_state=123, max_depth=3)
model = dtc.fit(x_train, y_train)

# 트리모델 시각화
tree.plot_tree(model)
#@@1

print(export_text(model))
'''
|--- feature_2 <= 2.45  : 3번 칼럼 분류조건(왼쪽노드)
|   |--- class: 0     -> 'setosa' 100% 분류
|--- feature_2 >  2.45  : 3번 칼럼 분류조건(오른쪽노드) 
|   |--- feature_2 <= 4.75
|   |   |--- class: 1
|   |--- feature_2 >  4.75
|   |   |--- feature_3 <= 1.75
|   |   |   |--- class: 1
|   |   |--- feature_3 >  1.75
|   |   |   |--- class: 2
'''

names=iris.feature_names
'''
['sepal length (cm)',
 'sepal width (cm)',
 'petal length (cm)',
 'petal width (cm)']
'''
print(export_text(model, names))
'''
|--- petal length (cm) <= 2.45
|   |--- class: 0
|--- petal length (cm) >  2.45
|   |--- petal length (cm) <= 4.75
|   |   |--- class: 1
|   |--- petal length (cm) >  4.75
|   |   |--- petal width (cm) <= 1.75
|   |   |   |--- class: 1
|   |   |--- petal width (cm) >  1.75
|   |   |   |--- class: 2
'''

y_pred = model.predict(x_test)
y_true = y_test

acc = accuracy_score(y_true, y_pred)
acc # 0.977777777777777

con_mat = confusion_matrix(y_true, y_pred)
con_mat
'''
array([[15,  0,  0],
       [ 0, 15,  0],
       [ 0,  1, 14]], dtype=int64)
'''


# criterion='entropy'
dtc2 = DecisionTreeClassifier(criterion='entropy',random_state=123, max_depth=2)
model2 = dtc2.fit(x_train, y_train)

tree.plot_tree(model2)
#@@2


y_pred2 = model2.predict(x_test)
y_true = y_test

acc = accuracy_score(y_true, y_pred2)
acc # 0.9555555555555556

con_mat = confusion_matrix(y_true, y_pred2)
con_mat
'''
array([[15,  0,  0],
       [ 0, 14,  1],
       [ 0,  1, 14]], dtype=int64)
'''


# max_depth 생략 
#  => 깊은수록 분류정확도 높지만 과접합 될 가능성 있음
dtc3 = DecisionTreeClassifier(criterion='entropy',random_state=123)
model3 = dtc3.fit(x_train, y_train)

tree.plot_tree(model3)
#@@3

y_pred3 = model3.predict(x_test)
y_true = y_test

acc = accuracy_score(y_true, y_pred3)
acc # 0.9555555555555556

con_mat = confusion_matrix(y_true, y_pred3)
con_mat
'''array([[15,  0,  0],
       [ 0, 14,  1],
       [ 0,  1, 14]], dtype=int64)
'''


##########################
## model overfitting
##########################

wine = load_wine()

x_name = wine.feature_names
'''
['alcohol',
 'malic_acid',
 'ash',
 'alcalinity_of_ash',
 'magnesium',
 'total_phenols',
 'flavanoids',
 'nonflavanoid_phenols',
 'proanthocyanins',
 'color_intensity',
 'hue',
 'od280/od315_of_diluted_wines',
 'proline']
'''

x= wine.data
y=wine.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=123)

dtc = DecisionTreeClassifier() # default
model = dtc.fit(x_train, y_train)

train_score = model.score(x_train, y_train)
train_score  #  1.0

test_score = model.score(x_test, y_test)
test_score # 0.9629629629629629


tree.plot_tree(model) # max_depth = 5
#@@6

# max_depth=3
dtc2 = DecisionTreeClassifier(max_depth=3)
model2 = dtc2.fit(x_train, y_train)

train_score2 = model2.score(x_train, y_train)
train_score2  #  0.9838709677419355

test_score2 = model2.score(x_test, y_test)
test_score2  #  0.9629629629629629

tree.plot_tree(model2)

# Graphviz(Tree model 시각화 소프트웨어) 다운로드
#@@7
from sklearn.tree import DecisionTreeClassifier, export_graphviz

export_graphviz(model2, out_file='DT_tree_graph.dot', 
                feature_names=x_name, max_depth=3, class_names=True)
#@@8
# => 만들어진 파일(DT_tree_graph.dot) 보여주는 툴 다운받아서 의사결정나무 시각화




