# To change the framerate of the video without changing the duration of the video
# ffmpeg -i in.mp4 -r 10 -y in-10.mp4

import os
import cv2 
import p
import ffmpeg
import subprocess

'''
    Enter the name of the input file here
'''

inp_file = 'in.mp4'
out_file = 'out.mp4'






'''
    Getting each frame of the input video and saving it to a folder called 'frames'
'''

required_directories = ['./frames', './op']
for reqdir in required_directories:
    if not os.path.exists(reqdir):
        os.mkdir(reqdir)

subprocess.call(f'ffmpeg -i {inp_file} -r 10 -y in-10.mp4', shell=True)

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
    print(' ignore this idk why ')
finally:
    p.imageposterizer()
    p.createPosterizedVideo(out_file)
    p.deleteFiles()