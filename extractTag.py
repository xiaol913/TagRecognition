import cv2
from PIL import Image
import numpy as np
import os
import sys
import re

def extractTag(name):
    img = cv2.imread(name, 0)
    x = cv2.Sobel(img, cv2.CV_16S, 2, 0)
    dst = cv2.convertScaleAbs(x, 0, 0.00390625)
    ret, temp = cv2.threshold(dst, 0, 255, cv2.THRESH_OTSU)
    square = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 1))
    temp = cv2.dilate(temp, square, iterations=4)
    temp = cv2.erode(temp, square, iterations=4)
    temp = cv2.dilate(temp, square, iterations=3)
    square = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3))
    temp = cv2.erode(temp, square, iterations=1)
    temp = cv2.dilate(temp, square, iterations=3)
    contours, heirs = cv2.findContours(temp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for tours in contours:
        rc = cv2.boundingRect(tours)
        if rc[2] / rc[3] >= 2:
            if 50 < rc[3]:
                cv2.rectangle(img, (rc[0], rc[1]), (rc[0] + rc[2], rc[1] + rc[3]), (255, 0, 255))
                ball = img[rc[1]:(rc[1] + rc[3]), rc[0]:(rc[0] + rc[2])]
                name = '_' + name
                cv2.imwrite('./temp/' + name, ball)

    grayTag(name)


def grayTag(name):
    img = Image.open('./temp/' + name)
    img = img.convert('L')
    out = img.point(table, '1')
    os.remove('./temp/' + name)
    out.save('./temp/' + name)
    RemoveBorder(name)


def RemoveBorder(name):
    img = cv2.imread('./temp/' + name, 0)
    h, w = img.shape[:2]
    tagROI = img[15:h - 15, 10:w - 10]
    mask = np.zeros((h, w), np.uint8)
    mask = cv2.bitwise_not(mask)
    mask[15:h - 15, 10:w - 10] = tagROI
    os.remove('./temp/' + name)
    name = '#of' + name
    cv2.imwrite('./temp/' + name, mask)
    ReadNumber(name)


def ReadNumber(name):
    imgName, imgExt = os.path.splitext(name)
    name = ' ./temp/' + name
    resultFile = ' Out' + imgName
    cmd = 'tesseract' + name + resultFile + ' -l eng'
    os.popen(cmd)
    name = 'Out' + imgName
    RepNumber(name, imgName)


def RepNumber(name, imgName):
    rep = {'D': '0', 'I': '1', 'Z': '2', 'S': '8'}
    name = name + '.txt'
    txtfile = open(name)
    txt = txtfile.readline()
    txtfile.close()
    for r in rep:
        text = txt.replace(r, rep[r])

    txtfile = open(name, 'w')
    mgName1, imgName = re.split(r'[_]', imgName)
    text = 'The ' + imgName + ' tag number is ' + text
    txtfile.write(text)
    txtfile.close()
    return




threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

if __name__ == "__main__":
    extractTag(sys.argv[1])

