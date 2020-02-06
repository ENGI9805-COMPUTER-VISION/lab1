import cv2.cv2 as cv2
import numpy as np

#################### Setting up the file ################
videoFile = "Movie1.MOV"
vidcap = cv2.VideoCapture(videoFile)
success, frame = vidcap.read()

#################### Setting up parameters ################

# OpenCV is notorious for not being able to good to
# predict how many frames are in a video. The point here is just to
# populate the "desired_frames" list for all the individual frames
# you'd like to capture.

fps = vidcap.get(cv2.CAP_PROP_FPS)
est_video_length_minutes = 3         # Round up if not sure.
# Sets an upper bound # of frames in video clip
est_tot_frames = est_video_length_minutes * 60 * fps

n = 5                             # Desired interval of frames to include
desired_frames = n * np.arange(est_tot_frames)

#################### Initiate Process ################

for i in desired_frames:
    vidcap.set(1, i - 1)
    # image is an array of array of [R,G,B] values
    success, frame = vidcap.read(1)
    if frame is None:
        break

    cv2.imshow('app', frame)
    # The 0th frame is often a throw-away
    frameId = vidcap.get(1)
    cv2.imwrite("FolderFrames/frame%d.jpg" % frameId, frame)

vidcap.release()
print("Complete")
