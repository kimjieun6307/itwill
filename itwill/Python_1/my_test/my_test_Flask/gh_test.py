'''
import pandas as pd #as 별칭
import os
print(os.getcwd())
excel = pd.ExcelFile("C:\\ITWILL\\3_Python-I\\workspace\\my_test\\my_data\\의원검색.xlsx")
print(excel)

person = excel.parse('person')
print(person)
'''

import pandas as pd
from pandas import Series,DataFrame

data2016 = pd.read_csv("C:\\ITWILL\\3_Python-I\\workspace\\my_test\\my_data\\국회의원발의법률안2016.csv", encoding='ms949')
print(data2016.info())

person = pd.read_csv("C:\\ITWILL\\3_Python-I\\workspace\\my_test\\my_data\\국회의원인적사항.csv", encoding='ms949')
print(person.info())
name = person.이름
type(name)
len(name.unique())

