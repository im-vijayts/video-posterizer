from PIL import Image, ImageOps  
from moviepy.editor import *
import glob
import os
import shutil
import time

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


def createPosterizedVideo(out_file_name):

	'''
		Creating the final video File
	'''

	n = len(os.listdir('./op'))
	img = [f'./op/{i}.jpg' for i in range(n)]
	clips = [ImageClip(m).set_duration(0.1) for m in img]

	vidclip = VideoFileClip('in-10.mp4')
	audio = vidclip.audio

	concat_clip = concatenate_videoclips(clips, method="compose").set_audio(audio)
	concat_clip.write_videofile(f'{out_file_name}', fps=24)

def deleteFiles():
	f = ['./frames', './op']
	for folder in f:
		for filename in os.listdir(folder):
			file_path = os.path.join(folder, filename)
			try:
				if os.path.isfile(file_path) or os.path.islink(file_path):
					os.unlink(file_path)
				elif os.path.isdir(file_path):
					shutil.rmtree(file_path)
			except Exception as e:
				print('Failed to delete %s. Reason: %s' % (file_path, e))