# -*- coding: utf-8 -*-
"""
reshape vs resize
 - reshape : 모양 변경
 - resize : 크기 변경
  ex) images -> 120x150 규격화 -> model

image 규격화 : 실습
"""

from glob import glob # file 검색 패턴 사용(문자열 경로, *.jpg
from PIL import Image # image file read 할 수 있는 모듈
import numpy as np
import matplotlib.pyplot as plt

# 1개 image file open
# C:\ITWILL\4_Python-II\workspace
path = './chap04_Numpy'
file = path + '/images/test1.jpg'

img = Image.open(file) # image file read
type(img) # PIL.JpegImagePlugin.JpegImageFile

img.shape # AttributeError: 'JpegImageFile' object has no attribute 'shape'
np.shape(img) # (360, 540, 3)--(세로픽셀, 가로픽셀, 칼러) 
plt.imshow(img)

# (360, 540, 3) -> (120, 150, 3) 규격화 : resize
img_re = img.resize( (150, 120) ) #((가로(w), 세로(h)))--세로픽셀, 가로픽셀 위치 바꿔줘야 함
np.shape(img_re) # (120, 150, 3)
plt.imshow(img_re)

# PIL -> numpy : np.asarray()
type(img) # PIL.JpegImagePlugin.JpegImageFile
img_arr = np.asarray(img)
img_arr.shape # (360, 540, 3)
type(img_arr) # numpy.ndarray


# 여러장의 image resize 함수
def imageResize() : 
    img_h = 120 # 세로 픽셀
    img_w = 150 # 가로 픽셀
    
    image_resize = [] #규격화된 image 저장
    
    # glob : file 패턴
    for file in glob(path + '/images/'+'*.jpg') :
        # test1.jpg -> test2.jpg
        img = Image.open(file)
        print(np.shape(img))
        
        # PIL -> resize
        img = img.resize((img_w, img_h)) # w, h
        # PIL -> numpy
        img_data = np.asarray(img)
        
        # resize image save
        image_resize.append(img_data)
        print(file, ':', img_data.shape)
        
    # list -> numpy 
    return np.array(image_resize)

image_resize = imageResize()
'''
(360, 540, 3)
./chap04_Numpy/images\test1.jpg : (120, 150, 3)
(332, 250, 3)
./chap04_Numpy/images\test2.jpg : (120, 150, 3)
'''

image_resize.shape # (2, 120, 150, 3) --(size, h, w, color)
image_resize[0].shape # (120, 150, 3) --첫번째 이미지의 shape
image_resize[1].shape # (120, 150, 3) --두번째 이미지의 shape

# image 보기
plt.imshow(image_resize[1])
plt.imshow(image_resize[0])










