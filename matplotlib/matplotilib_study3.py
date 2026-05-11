import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.patches as patches
import json

# img = Image.open("18396603_frame_20.png")

# json 파일 읽어서 사람 위치 찾기
with open("18396603_frame_20.json","r",encoding='utf-8') as f:
    data = json.load(f)


annotations = data['frames']['annotations']

colors = ('red', 'green', 'blue', 'yellow',
          'lime','magenta','cyan','purple')
idx = 0
pos = list()

for ann in annotations:
    code = ann['category']['code']
    if  'vehicle' != code:
        continue

    label = ann['label']
    pos.append (((label['x'], label['y'],
           label['width'], label['height']),
            colors[idx]))
    idx+=1

print(pos)
img = plt.imread('18396603_frame_20.png')


plt.imshow(img)

#이미지 좌표 가져오기
ax = plt.gca()

for (x,y,w,h),color in pos:
#박스 좌표 설정
# x, y, width, height = pos

# 사각형 박스 만들기
    box = patches.Rectangle(
        (x,y), #시작 좌표
        w, # 너비 크기
        h, #높이 크기
        fill=False, #박스 내부 색 채우기 여부
        edgecolor=color, #테두리 색상
        linewidth=2 # 테두리 굵기
    )
    ax.add_patch(box)
    # 바운딩 박스위에 텍스트 넣기
    plt.text(x,y-10,'object', color = 'red',
             fontsize=10,
             bbox=dict( facecolor='white', edgecolor='red',pad=1))
# plt.axis("off")
plt.show()