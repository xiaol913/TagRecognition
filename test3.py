import cv2
import numpy as np
import os
import re

# img = cv2.imread('brgtruecar.jpg', 0)
# h, w = img.shape[:2]
# tagROI = img[15:h-15, 10:w-10]
# mask = np.zeros((h, w), np.uint8)
# mask = cv2.bitwise_not(mask)
# mask[15:h-15, 10:w-10] = tagROI
# cv2.imwrite('098.jpg', mask)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# name = '#_tag_truecar.jpg'
#
# imgName, imgExt = os.path.splitext(name)
# name = ' ./' + name
# resultFile = ' Outof' + imgName
# cmd = 'tesseract' + name + resultFile + ' -l eng'
# # os.popen(cmd)
# print cmd

name = 'Out#of_truecar.txt'
imgName, imgExt = os.path.splitext(name)
imgName1, imgName2 = re.split(r'[_]', imgName)
print imgName2

# rep = {'D': '0', 'I': '1', 'Z': '2', 'S': '8'}
# txtfile = open(name)
# txt = txtfile.readline()
# txtfile.close()
# for r in rep:
#     text = txt.replace(r, rep[r])
#
# txtfile = open(name, 'w')
# text = 'The ' + imgName + ' tag number is ' + text
# txtfile.write(text)
# txtfile.close()