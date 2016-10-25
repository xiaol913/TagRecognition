import cv2
import numpy as np
from PIL import Image
#
# threshold = 140
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
#
# img = cv2.imread('brgtruecar.jpg', 0)
# img = cv2.bitwise_not(img)
# h, w = img.shape[:2]
# mask = np.zeros((h+5, w+5), np.uint8)
# mask = cv2.bitwise_not(mask)
#
# ball = img[30:46,30:250]
# mask[10:46,10:162] = ball

# cv2.imshow('123', ball)


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

img = cv2.imread('brgtruecar.jpg', 0)
img = cv2.resize(img, (256, 64), interpolation=cv2.INTER_NEAREST)
dst = cv2.convertScaleAbs(img, 0, 0.003)
ret, temp = cv2.threshold(dst, 0, 255, cv2.THRESH_OTSU)
square = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3))
square = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3))
temp = cv2.erode(temp, square, iterations=3)
temp = cv2.dilate(temp, square, iterations=3)
contours, heirs = cv2.findContours(temp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cv2.imshow('temp', temp)
for tours in contours:
    rc = cv2.boundingRect(tours)
    if rc[2] / rc[3] >= 2:
        cv2.rectangle(img, (rc[0], rc[1]), (rc[0] + rc[2], rc[1] + rc[3]), (255, 0, 255))
        ball = img[rc[1]:(rc[1] + rc[3]), rc[0]:(rc[0] + rc[2])]
        ball = cv2.resize(ball, (256, 64), interpolation=cv2.INTER_LINEAR)
        ball = cv2.bitwise_not(ball)
        # cv2.imshow('123', ball)
        cv2.imwrite('332211.jpg', ball)


# cv2.imshow('origin', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()