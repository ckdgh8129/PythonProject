import numpy as np
import matplotlib.pyplot as plt

# img = np.array([
#     [0,50,100],
#     [150,200,255]
# ])

img = np.random.randint(0,256,(100,100))

# bright = np.clip(img - 100,0,255)
# bright = 255- img

#128이상은 255변경, 128 미만은 0 변경
copy_img = img.copy() # 원본 복사
copy_img[ copy_img >= 128 ] = 255
copy_img[ copy_img < 128 ] = 0

plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.imshow(copy_img,cmap='gray')
plt.title("copy")
plt.axis('off') #축을 꺼라

plt.subplot(1,2,2)
plt.imshow(img, cmap='gray')
plt.title("original")
plt.axis("off")



plt.show()