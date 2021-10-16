import cv2
import glob
import numpy

imdir = 'Tmp/'
ext = ['png', 'jpg', 'gif']    # Add image formats here

files = []
[files.extend(glob.glob(imdir + '*.' + e)) for e in ext]

images = [cv2.imread(file) for file in files]

cv2.imread('images')
cv2.imshow('images', images)
cv2.waitKey(0)