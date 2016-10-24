import Image
import cv2
import numpy as np
from pylab import *
import glob
import os


i = 0
for files in glob.glob('cartag.jpg'):
    image = cv2.imread('cartag.jpg')
    h,w = image.shape[:2]
    # 灰度化
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    grayIPimage = cv2.GetImage(cv2.fromarray(gray))
    sobel  = cv2.CreateImage((w, h),cv2.IPL_DEPTH_16S, 1)  #创建一张深度为16位有符号（-65536~65535）的的图像区域保持处理结果
    cv2.Sobel(grayIPimage,sobel,2,0,7)         # 进行x方向的sobel检测
    temp  = cv2.CreateImage(cv.GetSize(sobel),cv2.IPL_DEPTH_8U, 1)       #图像格式转换回8位深度已进行下一步处理
    cv2.ConvertScale(sobel, temp,0.00390625, 0)
    cv2.Threshold(temp, temp, 0, 255, cv2.THRESH_OTSU)
    kernal = cv2.CreateStructuringElementEx(3,1, 1, 0, 0)
    cv2.Dilate(temp, temp,kernal,2)
    cv2.Erode(temp, temp,kernal,4)
    cv2.Dilate(temp, temp,kernal,2)
#     cv.ShowImage('1', temp)
    kernal = cv2.CreateStructuringElementEx(1,3, 0, 1, 0)
    cv2.Erode(temp, temp,kernal,1)
    cv2.Dilate(temp, temp,kernal,3)
#     cv.ShowImage('2', temp)
    temp = np.asarray(cv2.GetMat(temp))
    contours, heirs  = cv2.findContours(temp,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for tours in contours:
        rc = cv2.boundingRect(tours)
        if rc[2]/rc[3] >= 2:
            #rc[0] 表示图像左上角的纵坐标，rc[1] 表示图像左上角的横坐标，rc[2] 表示图像的宽度，rc[3] 表示图像的高度，
            cv2.rectangle(image, (rc[0],rc[1]),(rc[0]+rc[2],rc[1]+rc[3]),(255,0,255))
            imageIp = cv2.GetImage(cv2.fromarray(image))
            cv2.SetImageROI(imageIp, rc)
            imageCopy = cv2.CreateImage((rc[2], rc[3]),cv2.IPL_DEPTH_8U, 3)
            cv2.Copy(imageIp, imageCopy)
            cv2.ResetImageROI(imageIp)
            cv2.SaveImage('D:/pic/result/' + str(i) + '.jpg',imageCopy)
            i = i +1
# cv2.imshow("黑底白字",image)
cv2.waitKey(0)      #暂停用于显示图片