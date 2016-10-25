import cv2
import numpy as np

img = cv2.imread('brgtruecar.jpg', 0)
h, w = img.shape[:2]
tagROI = img[15:h-15, 10:w-10]
mask = np.zeros((h, w), np.uint8)
mask = cv2.bitwise_not(mask)
mask[15:h-15, 10:w-10] = tagROI
cv2.imwrite('098.jpg', mask)
