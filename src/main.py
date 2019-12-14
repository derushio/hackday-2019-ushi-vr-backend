import cv2;

cap = cv2.VideoCapture('./data/video.mp4')
ret, frame = cap.read()
print(frame)

# while(cap.isOpened()):
    # cv2.imshow('frame', frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        # break

cap.release()
