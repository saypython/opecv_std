import cv2
import numpy as np
img = cv2.imread('img/face_c.jpg')
print(img.item(150,120,0))
img.itemset((150,120,0),255) #将（150,120,0）当前像素颜色改为255
print(img.item(150,120,0))
#print(img[:,:,0]) #img[:,:,1]=0将1（green通道的所有值）重置为0
#图像拷贝
cv2.imshow('window',img)
roi =img[0:100,0:100]
cv2.imshow('waitcopy',roi)
iniimg = img[200:300,200:300] = roi
#iniimg = roi
cv2.imshow('iniimg',iniimg)

cv2.imshow('window',img)
print(img.shape)
print(img.size)
print(img.dtype)
cv2.waitKey(0)==ord('q')
cv2.destroyAllWindows()

