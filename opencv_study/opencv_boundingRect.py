import cv2
img = cv2.imread('opencv_study/images/cars.png')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (9,9), 0)


_, thresh = cv2.threshold(
    blur,100,255, cv2.THRESH_BINARY_INV
)


contourts, hier = cv2.findContours(
    thresh,
    cv2.RETR_LIST,
    cv2.CHAIN_APPROX_SIMPLE
)

result = img.copy()

for cnt in contourts:
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(
        result,
        (x,y),
        (x+w,y+h),
        (0,0,255),2
    )

cv2.imshow('result', result)    
cv2.waitKey(0)
cv2.destroyAllWindows()
