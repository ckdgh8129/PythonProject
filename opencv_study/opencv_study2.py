# AI가 영상분석을 하는데 먼저 전처리 한다.
# 전처리는 크기변경, 흑백변환, 노이즈 제거, 강조 처리 등.

import cv2

# img = cv2.imread('opencv_study/images/surfer.png')

#변경 이후에 show
#흑백 변환 - cv2.COLOR_BGR2GRAY
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('surfer', gray)
# print(gray.shape)
# print( gray[100][100] )

# cv2.waitKey(0)

#크기 변경하기

# # cv2.resize(대상, (가로, 세로) )
# small = cv2.resize( img , (152,83) )
# cv2.imshow('surfer', small)
# print(small.shape)
# cv2.waitKey(0)

# # 이미지 뒤집기(반전)
# flip = cv2.flip(img, 1)
# # 1-좌우 반전, 0- 상하반전, -1 - 상하좌우반전
# cv2.imshow('surfer', flip)
# print(flip.shape)
# cv2.waitKey(0)

# #블러처리 - 이미지를 흐리게 만드는것
# #노이즈 감소의 목적
# blur = cv2.GaussianBlur(img, (5,5), 0)
# #(5,5) 의 값을 크게주면 더더 흐려진다.

# cv2.imshow('blur', blur)
# print(blur.shape)
# cv2.waitKey(0)

# # 경계 - threshold
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# _, thresh = cv2.threshold(
#     gray, 127, 255, cv2.THRESH_BINARY)
# _, thresh_rev = cv2.threshold(
#     gray , 127, 255, cv2.THRESH_BINARY_INV)

# cv2.imshow('gray', gray)
# cv2.imshow("bin",thresh)
# cv2.imshow("inv", thresh_rev)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#사진의 크기는 가로길이 320으로 비율 유지해서 변경하고
#흑백변환하고, 멍멍이가 잘 보일수 있도록 경계설정하여
# dog_result.png 로 저장

img = cv2.imread('opencv_study/images/dog.png')

copy_img = img.copy()

print(copy_img.shape)
small = cv2.resize( copy_img , (320,240))

gray = cv2.cvtColor(small , cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(
    gray, 170, 255, cv2.THRESH_BINARY)

cv2.imshow('small', small)
cv2.imshow('dog', gray)
cv2.imshow("bin",thresh)
cv2.imwrite('opencv_study/images/dog_result.png', thresh)
cv2.waitKey(0)