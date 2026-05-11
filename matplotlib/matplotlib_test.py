"""
125 번 png와 json 파일을 사용하여 다음을 만들어 보세요

이미지 안에서 차량의 크기가 가장 큰 차와 크기가 세번째로 큰 차를 바운딩 박스로 표시해주세요
가장큰 차의 바운딩 박스 테두리  색은 red  세번째로 큰 차의 바운딩 박스 테두리색은
yellow

"""

import matplotlib.pyplot as plt
import numpy as np
import json
from PIL import Image
import matplotlib.patches as patches

with open("18396708_frame_125.json",'r',encoding='utf-8') as f:
    data = json.load(f)

vehicles = []
for ann in data['frames']['annotations']:
    code = ann['category']['code']
    if code != 'vehicle':
        continue
    label = ann['label']
    area = label['width'] * label['height']
    vehicles.append((area, label['x'], label['y'], label['width'], label['height']))


vehicles.sort(key=lambda v: v[0], reverse=True)

img = plt.imread('18396708_frame_125.png')
plt.imshow(img)
ax = plt.gca()

car = [(vehicles[0], 'red'), (vehicles[2], 'yellow')]

for (area, x, y, w, h), color in car:
    box = patches.Rectangle(
        (x, y), w, h,
        fill=False,
        edgecolor=color,
        linewidth=2
        )
    ax.add_patch(box)

plt.show()

