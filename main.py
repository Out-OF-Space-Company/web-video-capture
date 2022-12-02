import pyautogui
import numpy as np
import cv2
from flask import Flask, render_template, Response
from video_cap import video_capture
import time

SCREEN_SIZE = tuple(pyautogui.size())
RESOLUTION = (1920, 1080)
app = Flask(__name__)
video_stream = video_capture()

def gen(src):
    while True:
        success, frame = src.get()
        if not success:
            break
        else:
            yield ( b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen(video_stream),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port="5000")