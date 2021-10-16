import cv2
import os



def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images


def readImage():
    img = cv2.imread('Tmp/girado.png')
    return pytesseract.image_to_data(img, output_type=Output.DICT)

data = readImage()

load_images_from_folder('Tmp')
cv2.imread('images')
cv2.imshow('images', images)
cv2.waitKey(0)