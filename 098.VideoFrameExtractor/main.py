"""
Extract Frame of a video at a particular second
"""

import argparse

import cv2 as cv

OUTPUT_PATH = "./output.png"

def extract_frame(video_path, second):
    cap = cv.VideoCapture(video_path)
    if cap.isOpened():
        fps = cap.get(cv.CAP_PROP_FPS)
        print(fps)
    else:
        print("Video cannot be opened!")
        return
    frame_number = int(fps * second)

    cap.set(cv.CAP_PROP_POS_FRAMES, frame_number)

    ret, frame = cap.read()

    if ret:
        cv.imwrite(OUTPUT_PATH, frame)
        print("Frame saved!")
    else:
        print("Failed to extract frame!")


def main():
    parser = argparse.ArgumentParser(description="Video Frame Extractor CLI")

    parser.add_argument("video_path", help="Path to a video file")
    parser.add_argument("second", type=float, help="Target second of the frame")

    args = parser.parse_args()
    extract_frame(args.video_path, args.second)


if __name__ == '__main__':
    main()
