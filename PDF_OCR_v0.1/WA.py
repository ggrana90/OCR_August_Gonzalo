from pdf2image import convert_from_path
import pytesseract
import cv2
from PIL import Image
import os
import re
from pytesseract import Output
import shutil


def WAToImage(filename):
    file = "WA/" + filename
    converted_file = "Processed/" + filename
    im_file = "WA/"
    im = Image.open(im_file)
    out.save('Pending/wa1.jpeg')
    image1 = cv2.imread('Pending/wa1.jpeg')
    img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

    # se pueden aplicar diferentes tecnicas de threshold
    ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

    # cv2.imshow('Binario', thresh1)
    cv2.imwrite('Pending/wa1.jpeg',thresh4,None)
    image = cv2.imread('Pending/wa1.jpeg',0)
    return pytesseract.image_to_data(image, output_type=Output.DICT)['text']

