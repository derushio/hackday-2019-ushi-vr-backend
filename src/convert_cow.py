import cv2;
from video_loader import video_loader

def convert_cow(path: str):
    frames = video_loader(path);
    for frame in frames:
        pass
