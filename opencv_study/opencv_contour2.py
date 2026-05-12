import cv2

img = cv2.imread('opencv_study/images/cars.png')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (9,9), 0)

_, thresh = cv2.threshold(
    blur,100,255, cv2.THRESH_BINARY_INV
)


contours, _ = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)

contourts, hier = cv2.findContours(
    thresh,
    cv2.RETR_LIST,
    cv2.CHAIN_APPROX_SIMPLE
)

result = img.copy()
count = 0


for contour in contours:
    area = cv2.contourArea(contour)
    if area >200:
        count += 1 

print("찾은 자동차수 : ", len(contours))
cv2.imshow('img1', img)
cv2.imshow('img', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()