import cv2;

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
