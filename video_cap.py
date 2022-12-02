import threading
import numpy as np
import cv2
import pyautogui

class video_capture(object):
    def __init__(self) -> None:
        self.video = pyautogui.screenshot()
        self.started = False

    def __del__(self):
        self.video.release()

    def get(self):
        self.video = pyautogui.screenshot()
        self.video = np.array(self.video)
        self.video = cv2.cvtColor(self.video, cv2.COLOR_BGR2RGB)
        ret, jpeg = cv2.imencode('.jpg', self.video)
        return ret, jpeg.tobytes()