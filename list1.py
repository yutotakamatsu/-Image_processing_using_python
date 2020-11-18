import cv2

img_path = 'img/lena.jpg'

img = cv2.imread(img_path, 1)

cv2.imshow('img', img)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cap.release()
    cv2.destroyAllWindows()