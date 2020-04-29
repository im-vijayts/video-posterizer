# To change the framerate of the video without changing the duration of the video
# ffmpeg -i in.mp4 -r 10 -y in-15.mp4

import cv2 

'''
    Getting each frame of the input video and saving it to a folder called 'frames'
'''

input_file_name = 'in-10.mp4'

def FrameCapture(path): 
    vidObj = cv2.VideoCapture(path) 
    count = 0
    success = 1
    while success: 
        success, image = vidObj.read() 
        cv2.imwrite("./frames/frame%d.jpg" % count, image)
        count += 1

FrameCapture(input_file_name)