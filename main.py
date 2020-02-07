from camera import VideoCam
from lab1 import drawLines


SKIPFRAME = 30
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
            drawLines(saved_file, "frames")
    except KeyboardInterrupt:
        v1.close_cam()
        exit(0)

v1.close_cam()
