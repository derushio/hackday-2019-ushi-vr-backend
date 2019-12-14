import cv2
import numpy as np
from video_loader import video_loader
from statics import video_size

def convert_cow(path: str):
    sample_div = 2

    frames = video_loader(path);
    new_frames = []
    for frame in frames:
        new_frame = []
        for x in frame:
            new_x = []
            for i, y in enumerate(x):
                if i % sample_div:
                    new_x.append(y)

            new_frame.append(new_x)

        print(np.array(new_frame).shape)
        cv2.imshow('new_frame', np.array(new_frame))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        new_frames.append(new_frame)
        break;
