import cv2;
import numpy as np

def video_loader(path: str):
    cap = cv2.VideoCapture(path)

    frames = []

    ret, frame = cap.read()
    frames.append(frame);
    while frame is not None:
        ret, frame = cap.read()
        frames.append(frame)

    cap.release()

    return frames;

def get_1frame(path: str):
    cap = cv2.VideoCapture(path)

    ret, frame = cap.read()

    height = 3040//2
    width = 1520//2

    frame = cv2.resize(frame, dsize=(height, width))

    cap.release()

    # RGB分離
    img_colors = cv2.split(frame)

 
	# img_colors 0... blue, 1 ... green, 2 ... red
    subarr = np.array([[40]*height]*width)
    img_colors[1] = np.abs(img_colors[1] - subarr)
    img_colors[0] = np.abs(img_colors[0] - subarr)

    frame = cv2.merge((img_colors[0].astype(np.uint8), img_colors[1].astype(np.uint8), img_colors[2]))
    return frame
