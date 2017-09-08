import cv2
import numpy
import os
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)

grayImage = flatNumpyArray.reshape(300,400)
cv2.imwrite('img/RandomGray.png',grayImage)

bgrImage = flatNumpyArray.reshape(100,400,3)
cv2.imwrite('img/RandomColor.png',bgrImage)

img = numpy.random.randint(0,256,120000).reshape(300,400)
cv2.imshow('window',img)
cv2.waitKey(0)
#resgape创建数组
#randint创建随机数