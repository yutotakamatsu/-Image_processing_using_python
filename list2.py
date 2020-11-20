import cv2

img_path = 'img/img.png'

img = cv2.imread(img_path, 1)

print(f'img : {img}')