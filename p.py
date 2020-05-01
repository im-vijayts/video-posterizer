from PIL import Image, ImageOps  
from moviepy.editor import *
import glob
import os

def imageposterizer():

	'''
		Applying the posterizer effect
		In the line,
			im2 = ImageOps.posterize(im1, 2)  
		the 2 represents the intensity of posterization, highest being 1 and lowest being 8
		
		The output frames are saved to a folder called 'op'
	'''

	n = len(os.listdir('./frames'))

	for i in range(n):
		im1 = Image.open(f"./frames/frame{i}.jpg")  

		im2 = ImageOps.posterize(im1, 2)  
		
		im2.save(f'./op/{i}.jpg')


def createPosterizedVideo():

	'''
		Creating the final video File
	'''

	n = len(os.listdir('./op'))
	img = [f'{i}.jpg' for i in range(n)]
	clips = [ImageClip(m).set_duration(0.1) for m in img]

	vidclip = VideoFileClip('in-10.mp4')
	audio = vidclip.audio

	concat_clip = concatenate_videoclips(clips, method="compose").set_audio(audio)
	concat_clip.write_videofile("test.mp4", fps=24)