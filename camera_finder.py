#!/usr/bin/python
#import exifread
import os, sys
import glob

sys.argv.append('Y:\\')
file_sigs = {'ext':('.jpg','.jpeg','.JPG','.JPEG')}

for i in glob.iglob(sys.argv[1] + '**', recursive=True):
	extension = os.path.splitext(i)[1]
	if os.path.isfile(i) and extension in file_sigs['ext']:
		with open(i, 'rb') as jpeg:
			image = jpeg.read()
			try:
				hex(image.index(b'DSC-W5'))
				print(i)
			except ValueError:
				pass
