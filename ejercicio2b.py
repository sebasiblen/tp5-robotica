import cv2
import numpy as np

img = cv2.imread('cubo.jpg')
imgHSV= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

rojoA = np.array([8,255,255], np.uint8)
rojoB = np.array([0,100,20], np.uint8)

rojoA2 = np.array([179,255,255], np.uint8)
rojoB2 = np.array([175,100,20], np.uint8)

maskRojo1 = cv2.inRange(imgHSV, rojoB, rojoA)
maskRojo2 = cv2.inRange(imgHSV, rojoB2, rojoA2)

maskRed = cv2.add(maskRojo1, maskRojo2)

maskRedVis = cv2.bitwise_and(img, img, mask=maskRed)

cv2.imshow('Original', img)
cv2.imshow("maskRed", maskRojo1)
cv2.imshow('maskRojoVis', maskRedVis)

cv2.waitKey(0)
cv2.destroyAllWindows()