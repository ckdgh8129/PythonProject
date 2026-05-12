# contour 는 연결된 외곽선이다.
# edge가 경계선 이라면
# contour 는 경계선을 따라 연결된 객체의 외곽선 묶음 이다.

import cv2

img = cv2.imread('opencv_study/images/coin.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (11,11), 0)


_, thresh = cv2.threshold(
    blur, 150, 255, cv2.THRESH_BINARY_INV) #배경이 밝고 객체가 어두울때 반전

#contour를 하기전에 Canny 나 threshold로 경계영역 만들어야한다.

# 발견된 영역에서 가장 바깥쪽 외곽선만 찾는다.

# cv2.RETR_EXTERNAL - 동전의 가운데가 검은색으로 표시되도
            #바깥쪽 외곽만 사용한다.
# cv2.CHAIN_APPROX_SIMPLE - 외곽선을 저장할때 필요한 부분만 저장하기
# findContour ( 이미지값 , mode, method)
# mode매개변수에 들어갈 값
#       cv2.RETR_LIST - 모든 contour를 찾기
#       cv2.RETR_TREE - 모든 contour를 찾고 계층관계까지 저장
#       cv2.RETR_CCOMP - 2계층으로 저장
#                       (예- 도넛을 인식 하는경우 도넛 외곽과 가운데 구멍까지 만 저장)
# findContours함수의 두번째 반환값은 계층 정보가 반환된다.
# 두번째 반환 값으로  [next(같은계층  contour), pre(같은계층의 이전 contour), 
#                   first_child(안쪽계층의 첫번째 자식 contour),
#                   parent(현재 contour의 부모 contour)]

# findContours함수 3번째 인자 method
# cv2.CHAIN_APPROX_NONE - 외곽선의 모든 픽셀 좌표저장(정밀분석)
# cv2.CHAIN_APPROX_TC89_L1 - teh-chain 알고리즘 기반 - 더부드럽게 표시하기위한

contourts, hier = cv2.findContours(
    thresh,
    cv2.RETR_LIST,
    cv2.CHAIN_APPROX_SIMPLE
)

result = img.copy()

#drawContours(이미지, contours, 어떤 contour에 그리는가, 색상, 선 굵기)

cv2.drawContours(result, contourts, -1, (0,0,255), 2)

print("찾은 동전수 : ", len(contourts) )

cv2.imshow('coin', result)
cv2.imshow("bin",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

