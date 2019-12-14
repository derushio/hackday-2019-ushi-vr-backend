import cv2;

def convert_cow(path: str):
    cap = cv2.VideoCapture(path)

    frames = []

    ret, frame = cap.read()
    frames.append(frame);
    while frame:
        ret, frame = cap.read()
        frames.append(frame)

    cap.release()

    print(len(frames))
    print('hoge')
