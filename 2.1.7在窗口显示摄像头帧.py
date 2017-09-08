import cv2
clicked = False
def onMouse(event,x,y,flags,param):
    global clicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True

cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow',onMouse)

print('showing camera feed . click windw or press any key to stop')
success,frame = cameraCapture.read()
while success and cv2.waitKey(5) == 255 and not clicked:
    cv2.imshow('MyWindow',frame)
    success,frame = cameraCapture.read()

cv2.destroyWindow('MyWindow')
cameraCapture.release()

# cap=cv2.VideoCapture(0)
# while(1):
#     ret,frame=cap.read()
#     cv2.imshow('frame',frame)
#     k = cv2.waitKey(5)
#     if k==27:
#         break
# print(k)
# cv2.destroyAllWindows()

print(cv2.waitKey(0))