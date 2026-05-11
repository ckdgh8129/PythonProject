import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import json


with open ('012_000000.json',"r",encoding="utf-8") as f:
    data = json.load(f)

annotations = [
                a for a in data['annotations']
                if "category_name" in a]

# 데이터 프레임 으로 저장하기
df = pd.DataFrame(annotations)
count = df ['category_name'].value_counts()
print("트럭",count['truck'])


# 차량들의 너비 값 출력
car_width = df["bbox"].apply(lambda x:x[1][0])
print(car_width)

# 문제 너비가 가장 큰 차량을 찾으시오. 이미지에 바운딩 박스 표시하기

# car_max_width = df['width'].idxmax()
# car = df.loc[car_max_width]


# 문제 각 차량별 너비를 구하여 그래프로 출력해보세요

