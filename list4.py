import cv2

cap = cv2.VideoCapture(0)
fps = 30

size = (640, 480)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('output.avi', fourcc, fps, size)

while (cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    video.write(frame)
            
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        cap.release()
        video.release()
        cv2.destroyAllWindows()
