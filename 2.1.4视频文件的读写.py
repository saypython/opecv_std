import cv2
videoCapture = cv2.VideoCapture('img/minions.avi')#视频数据准备
fps = videoCapture.get(cv2.CAP_PROP_FPS)#FPS参数准备
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))#size参数准备
videoWriter = cv2.VideoWriter(
    'img/minions1.avi',cv2.VideoWriter_fourcc('X','V','I','D'),fps,size
)#编码器准备
success,frame = videoCapture.read()#读视频的帧
while success:#如果读取成功
    videoWriter.write(frame)#写入
    success,frame = videoCapture.read()#继续读下一帧