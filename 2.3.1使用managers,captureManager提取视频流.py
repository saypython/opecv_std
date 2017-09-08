import cv2
import numpy
import time

class CaptureManager(object):
    def __int__(self,capture,previewWindowManager = None,
                shouleMirrorPreview = False):
        self.previewWindowManager = previewWindowManager
        self.shouleMirrorPreview = shouleMirrorPreview
        self.__capture = capture
        self.__channel = 0
        self.__enteredFrame = False
        self.__frame = None
        self.__imageFilename = None
        self.__videoFilename = None
        self.__videoEncoding = None
        self.__videoWriter = None
        self.__startTime = None
        self.__framesElapsed = numpy.long(0)
        self.__fpsEstimate = None

        @property
        def channel(self):
            return  self._channel

        @channel.setter
        def channel(self,value):
            if self._channel != value:
                self._channel = value
                self._frame = None

        @property
        def frame(self):
            if self._enteredFrame and self._frame is None:
                _,self._frame = self.capture.retrieve()
                return self._frame

        @property
        def isWritingImage(self):
            return  self._imageFilename is not None

        @property
        def isWritingVideo(self):
            return  self._videoFilename is not None

        def enterFrame(self):
            if self._capture is not None:
                self.enteredFrame = self._capture.grab()

        def exitFrame(self):
            if self._frame is None:
                self._enteredFrame = False
                return
            if self._framesElapsed == 0:
                self._startTime = time.time()
            else:
                timeElapsed = time.time() - self._startTime
            self._fpsEstimate = self._framesElapsed / timeElapsed
        self._framesElapsed +=1

        if self.previewWindowManager is not None:
            if self.shouleMirrorPreview:
                mirroredFrame = numpy.fliplr(self._frame).copy()
                self.previewWindowManager.show(mirroredFrame)
            else:
                self.previewWindowManager.show(self.frame)

            if self.isWritingImage:
                cv2.imageFilename = None
                self._writevideoFrame()
                self._frame = None
                self._enterdFrame = False

        def writeImage(self,filename):
            self._imageFilename = filename

        def startWritingVideo(
                self,filename,
                encoding = cv2.VideoWriter_fourcc('I','4','2','0')):
            self._videoFilename = filename
            self._videoEncoding = encoding

        def stopWritingVideo(self):
            self._videoFilename = None
            self._videoEncoding = None
            self._videoWriter = None

        def _writeVideoFrame(self):
            if not self.isWritingVideo:
                return
            if self._videowriter is None:
                fps = self._capture.get(cv2.CAP_PROP_FPS)
                if fps == 0.0:
                    if self._framesElapsed< 20:
                        return
                    else:
                        fps = self._fpsEstimeate
                size = (int(self.capture.get(
                            cv2.CAP_PROP_FRAME_WIDTH
                        )),int(self.capture.get(
                            cv2.CAP_PROP_FRAME_HEIGHT
                        )))
                self._videoWriter = cv2.VideoWriter(
                    self._videoFilename,self._videoENcoding,
                    fps,size)
                self._videoWriter.write(self._frame)






