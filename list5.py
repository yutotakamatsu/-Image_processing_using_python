import cv2
import numpy as np
from PIL import Image

img=np.zeros((3, 3, 3), np.float32)

img[0][0] = [255,0,0]
img[0][1] = [0,255,0]
img[0][2] = [0,0,255]
img[1][0] = [255,255,255]
img[1][1] = [192,192,192]
img[1][2] = [0,0,0]
img[2][0] = [255,255,0]
img[2][1] = [255,0,255]
img[2][2] = [0,255,255]

print(img)

cv2.imshow('color',img)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

cv2.imwrite('img.png', img)

color = cv2.imread('Color_small.jpg')
print(color)

