# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 01:32:57 2020

@author: ebrahim
"""

import cv2
import numpy as np
import os

from intersection import segment_by_angle_kmeans, segmented_intersections
from video_utils import VideoCam


SKIPFRAME = 30


def draw_lines(filename, input_path='', output_path='results'):
    img = cv2.imread(os.path.join(input_path, filename))  # Remember to add the path for the test1.jpg
    size = img.shape

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 100, 500
    edges = cv2.Canny(gray, 50, 800)  # The parameters are the thresholds for Canny

    _lines = cv2.HoughLines(edges, 1, np.pi / 180, 160)  # The parameters are accuracies and threshold
    num = len(_lines)
    for n in range(num):
        rho, theta = _lines[n][0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + size[1] * (-b))
        y1 = int(y0 + size[0] * (a))
        x2 = int(x0 - size[1] * (-b))
        y2 = int(y0 - size[0] * (a))

        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imwrite(os.path.join(output_path, filename), img)
    return filename, img, _lines


def process_images():
    for i in range(1, 5):
        input_name = 'test{}.jpg'.format(i)
        filename, img, _lines = draw_lines(input_name)
        intersections = draw_intersections(filename, img, _lines)


def draw_intersections(filename, img, lines, output_path="results"):
    segmented = segment_by_angle_kmeans(lines)
    intersections = segmented_intersections(segmented)
    for intersection in intersections:
        cv2.circle(img, (intersection[0][0], intersection[0][1]), 8, (0, 255, 255), 4)

    cv2.imwrite(os.path.join(output_path, filename), img)
    return intersections


def process_video():
    url = "Movie1.MOV"
    v1 = VideoCam(url)
    v1.check_camera(v1.cap)
    ct = 0
    while True:
        ct += 1
        try:
            ret = v1.cap.grab()
            if ct % SKIPFRAME == 0:  # skip some frames
                ret, frame = v1.get_frame()
                if not ret:
                    break
                # frame HERE
                saved_file = v1.save_frame(frame)
                _, res, __ = draw_lines(saved_file, "frames")
                v1.show_frame(res)
        except KeyboardInterrupt:
            v1.close_cam()
            exit(0)

    v1.close_cam()


if __name__ == "__main__":
    process_images()
    process_video()
