# To change the framerate of the video without changing the duration of the video
# ffmpeg -i in.mp4 -r 10 -y in-10.mp4

import os
import cv2 
import p
import ffmpeg

'''
    Getting each frame of the input video and saving it to a folder called 'frames'
'''

os.popen('ffmpeg -i in.mp4 -r 10 -y in-10.mp4')

input_file_name = os.getcwd() + '\\in-10.mp4'

def FrameCapture(path): 
    vidObj = cv2.VideoCapture(path) 
    count = 0
    success = 1
    while success: 
        success, image = vidObj.read() 
        cv2.imwrite(os.getcwd() + '\\frames\\frame%d.jpg' % count, image)
        count += 1
try:
    FrameCapture(input_file_name)
except:
    print(' oh no something went wrong ')
finally:
    p.imageposterizer()
    p.createPosterizedVideo()