import cv2
import numpy as np
from pytesseract import *
from PIL import Image

threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

img = cv2.imread('brgtruecar.jpg', 0)
# img = cv2.bitwise_not(img)
h, w = img.shape[:2]
mask = np.zeros((h+5, w+5), np.uint8)
mask = cv2.bitwise_not(mask)

ball = img[30:46,30:250]
# mask[10:46,10:162] = ball

cv2.imshow('123', ball)


# cv2.imwrite('newtag.jpg', mask)
# th, temp = cv2.threshold(ball, 220, 255, cv2.THRESH_BINARY_INV)

# im = Image.open('newtag.jpg')
# imgry = im.convert('L')
# out = im.point(table, '1')
# text = image_to_string(out)
# text = text.strip()
# text = text.upper()
#
# print text
# cv2.imshow('1', ball)

cv2.waitKey(0)
cv2.destroyAllWindows()