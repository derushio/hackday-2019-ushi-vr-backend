import cv2
import numpy as np
from video_loader import video_loader
from statics import video_size
import copy

def convert_cow(path: str):
    sample_div = 3

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
        changed_frame = change_color(new_frame)
        video.write(np.array(changed_frame))
        print('done: ' + str(i_frame))

    video.release()

def change_color(frame):
    img_colors = cv2.split(frame)

	# img_colors 0... blue, 1 ... green, 2 ... red
    subarr = np.array([[40]*height]*width)
    img_colors[1] = np.abs(img_colors[1] - subarr)
    img_colors[0] = np.abs(img_colors[0] - subarr)

    frame = cv2.merge((img_colors[0].astype(np.uint8), img_colors[1].astype(np.uint8), img_colors[2]))
    return frame