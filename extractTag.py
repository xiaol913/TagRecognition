import cv2
from PIL import Image
import os

def extractTag(name):
    img = cv2.imread(name, 0)
    x = cv2.Sobel(img, cv2.CV_16S, 2, 0)
    dst = cv2.convertScaleAbs(x, 0, 0.00390625)
    ret, temp = cv2.threshold(dst, 0, 255, cv2.THRESH_OTSU)
    square = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 1))
    # cv2.imshow('1', temp)
    temp = cv2.dilate(temp, square, iterations=4)
    temp = cv2.erode(temp, square, iterations=4)
    temp = cv2.dilate(temp, square, iterations=3)
    square = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3))
    temp = cv2.erode(temp, square, iterations=1)
    temp = cv2.dilate(temp, square, iterations=3)
    # cv2.imshow('123', temp)
    contours, heirs = cv2.findContours(temp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for tours in contours:
        rc = cv2.boundingRect(tours)
        if rc[2] / rc[3] >= 2:
            if 50 < rc[3]:
                cv2.rectangle(img, (rc[0], rc[1]), (rc[0] + rc[2], rc[1] + rc[3]), (255, 0, 255))
                ball = img[rc[1]:(rc[1] + rc[3]), rc[0]:(rc[0] + rc[2])]
                cv2.imwrite('tag'+ name, ball)

    # cv2.imshow('1234', img)
    return

def grayImg(name):
    img = Image.open('tag'+name)
    imgry = img.convert('L')
    out = imgry.point(table, '1')
    out.save('brg'+ name)
    os.remove('tag'+name)
    return


threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

extractTag('truecar.jpg')
grayImg('truecar.jpg')
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
