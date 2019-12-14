import cv2
import numpy as np
from video_loader import video_loader
from statics import video_size
import copy

def convert_cow(path: str):
    sample_div = 5

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter('video.avi', fourcc, 30.0, (video_size['width'], video_size['height']))

    frames = video_loader(path);
    for i_frame, frame in enumerate(frames):
        new_frame = []

        if frame is None:
            break;

        for x in frame:
            new_x = []
            for i, y in enumerate(x):
                if i % sample_div:
                    new_x.append(y)

            new_frame.append(new_x)

        main_frame = copy.deepcopy(new_frame)

        for xi, x in enumerate(main_frame):
            x_len = (len(x) - 1) // sample_div
            for y in x[:x_len]:
                new_frame[xi].append(y)

        for xi, x in enumerate(main_frame):
            x_len = (len(x) - 1) // sample_div
            for y in reversed(x[x_len:]):
                new_frame[xi].insert(0, y)

        print(np.array(new_frame).shape)
        video.write(np.array(new_frame))
        print('done: ' + str(i_frame))

    video.release()
