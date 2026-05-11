#open source Computer vision library
#컴퓨터 비전 - 비전 AI 

#이미지 -  사람이다. , 파랑색이다. 하늘색이다. 멍멍이다.
#       컴퓨터는 픽셀 숫자들의 모음 으로 보고있다.

# opencv로 이미지나 영상을 불러오기
# yolo에게 전달하여 객체 탐지
# 탐지 결과를 토대로 이미지나 영상에 opencv로 표시하기
# opencv - RGB(X), BGR(O)
# arr = np.array( [ [ [0,50,100],[150,200,255] ] ] )
# 영상 - opencv 열기 -> 프레임 한장 열기 -> 이미지 처리 -> 다음프레임 읽기
# -> 이미지 처리 
# 앞으로 할거
# 이미지 필터, 객체 외곽선 찾기
# 움직임 감지, 영상 저장, 객체 탐지 결과 시각화

# 이미지 numpy 배열 이다. 
# 영상은 이미지 여러장이다.
# 프레임 하나는 이미지 한장이다. fps( frame pres per second )
# opencv는 배열을 읽고 변경하고, 분석하고 그려주고, 저장

import cv2

img = cv2.imread('opencv_study/images/cat.png')

# cv2.imshow('이미지창 제목', 표시할 이미지)
# cv2.imshow('cat', img)

# print( type(img) ) #numpy 배열 타입
# print( img.shape ) #세로, 가로, 색상정보- 3은 rgb 
#색상정보 - 1 은 흑백, 4는 투명도포함 ( BGRA,RGBA )
# (183, 275 , 1) - 픽셀하나에 숫자 1개 
# (183, 275 , 3) - 픽셀하나에 숫자 3개 ( B,G,R )
# (183, 275 , 4) - 픽셀하나에 숫자 4개 ( R,G,B,A )
#                   A는 알파( 투명도- 0(투명)~255(불투명))

# print( img[100][100])
copy_img = img.copy() #원본 데이터를 변경하지 말고 복사본으로 

cut = copy_img[20:120, 130:230]
cv2.imwrite('opencv_study/images/cut_cat.png', cut)
cv2.imshow('cat', cut)
cv2.waitKey(0)





# copy_img[100:200, 100:200] = [0,0,255]
# cv2.imshow('cat', img)
# # 이미지 저장 .imwrite( '저장할 파일명', 저장객체)
# cv2.imwrite('opencv_study/images/copy_cat.png', copy_img)
# cv2.waitKey(0)

# h, w = img.shape[:2]
# center_x, center_y = w // 2, h // 2
# print(center_x, center_y)

# # copy_img[center_y-25: center_y+25, center_x-25: center_x+25] = [134,229,127]
# cv2.rectangle(copy_img, (center_x-25, center_y-25), (center_x+25, center_y+25), (127,229,134), -1)
# cv2.imshow('cat', copy_img)

# cv2.imwrite('opencv_study/images/copy_cat.png', copy_img)
# cv2.waitKey(0)












# pexels
# pixabay
# mixkit

