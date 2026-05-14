import cv2
import numpy as np

img = cv2.imread('opencv_study/images/image.png')

fr = cv2.resize(img, ( 680,480 ))

hsv = cv2.cvtColor(fr, cv2.COLOR_BGR2HSV)

lower_red1 = np.array( [0,100,100] )
up_red1 = np.array( [10,255,255] )

lower_red2 = np.array( [150,100,100] )
up_red2 = np.array( [180,255,255] )

mask1 = cv2.inRange(hsv, lower_red1, up_red1)
mask2 = cv2.inRange(hsv, lower_red2, up_red2)

mask = mask1 + mask2

kernel = np.ones((5,5), np.uint8)

mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)

mask = cv2.dilate(mask, kernel, iterations=1)

color_layer = np.zeros_like(fr)
color_layer[:,:] = (0,255,0)

colred_object = cv2.bitwise_and(color_layer, color_layer, mask=mask)

background = cv2.bitwise_and(fr, fr, mask=cv2.bitwise_not(mask))

result = cv2.add(colred_object, background)



cv2.imshow('surfer', result)
cv2.imshow('surfer', fr)
cv2.imshow('surfer', hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()
