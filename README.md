# Video Posterizer

Applies posterization effect to videos with audio synchronised to the framerate reduced video.

# What this does?

Reduces frame rate of the video to 10 fps (using ffmpeg).
Seperates out the frames from the video and applies the posterisation effect to each frame (using  opencv-python and Pillow).
Rejoins the frames into a video with the audio synchronised (using moviepy).

# The parameters you need to provide

## Main file is GetFrames.py

You are required to provide the following arguements:
  * inp_file (defaults to 'in.mp4') - The name of file
  * out_file (defaults to 'out.mp4') - The name of output file
  
These files have to be in the same directory as the GetFrames.py file.
