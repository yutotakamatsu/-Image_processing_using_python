import cv2

img_path = 'img/Color.png'

img = cv2.imread(img_path, 1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray', gray)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()