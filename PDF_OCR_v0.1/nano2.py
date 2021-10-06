#
# import cv2
# import numpy as np
#
# img = cv2.imread('Tmp/girado.png')
#
#
# # get grayscale image
# def get_grayscale(image):
#     return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
#
# # noise removal
# def remove_noise(image):
#     return cv2.medianBlur(image, 5)
#
#
# # thresholding
# def thresholding(image):
#     return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#
#
# # dilation
# def dilate(image):
#     kernel = np.ones((5, 5), np.uint8)
#     return cv2.dilate(image, kernel, iterations=1)
#
#
# # erosion
# def erode(image):
#     kernel = np.ones((5, 5), np.uint8)
#     return cv2.erode(image, kernel, iterations=1)
#
#
# # opening - erosion followed by dilation
# def opening(image):
#     kernel = np.ones((5, 5), np.uint8)
#     return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
#
#
# # canny edge detection
# def canny(image):
#     return cv2.Canny(image, 100, 200)
#
#
#
#
#
# # template matching
# def match_template(image, template):
#     return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
#

# def gonzalo(n_boxes):
#     return for i in range(n_boxes)

# import cv2
# import pytesseract
# from pytesseract import Output
#
# img = cv2.imread('Tmp/girado.png')
#
# d = pytesseract.image_to_data(img, output_type=Output.DICT)
# # print(d.keys())
#
# n_boxes = len(d['text'])
# for i in range(n_boxes):
#     if float(d['conf'][i]) > 10:
#         (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#         img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# cv2.imshow('img', img)
# cv2.waitKey(0)


# # # ##DETECTAR FECHA - OK
# import re
# import cv2
# import pytesseract
# from pytesseract import Output
# import datetime
#
# img = cv2.imread('Tmp/girado.png')
# d = pytesseract.image_to_data(img, output_type=Output.DICT)
# keys = list(d.keys())
#
# date_pattern = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'
#
# n_boxes = len(d['text'])
# for i in range(n_boxes):
#     if float(d['conf'][i]) > 1:
#         if re.match(date_pattern, d['text'][i]):
#             (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#             img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# cv2.imshow('img', img)
# cv2.waitKey(0)
#
# for i in range(n_boxes):
#     if float(d['conf'][i]) > 1:
#         if re.match(date_pattern, d['text'][i]):
#             print(re.match(date_pattern, d['text'][i]))
#

# #DETECTAR MATRICULA - NO FUNCIONA
# import re
# import cv2
# import pytesseract
# from pytesseract import Output
#
# img = cv2.imread('Tmp/girado.png')
# d = pytesseract.image_to_data(img, output_type=Output.DICT)
# keys = list(d.keys())
#
# matricula = '[0-9][0-9][0-9][0-9][\-]][A-Z][A-Z][A-Z]'
#
# n_boxes = len(d['text'])
# for i in range(n_boxes):
#     if float(d['conf'][i]) > 1:
#     	if re.match(matricula, d['text'][i]):
# 	        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
# 	        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# cv2.imshow('img', img)
# cv2.waitKey(0)

##DETECTAR TIPO GASOLINA - OK
import re
import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('Tmp/girado.png')
d = pytesseract.image_to_data(img, output_type=Output.DICT)
keys = list(d.keys())

gasolinatipo = '([A-Z][A-Z][A-Z][A-Z][A-Z][T][A][R])|([A-Z][A-Z][A-Z][A-Z][A-Z][U][E])'

n_boxes = len(d['text'])
for i in range(n_boxes):
    if float(d['conf'][i]) > 60:
    	if re.match(gasolinatipo, d['text'][i]):
	        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
	        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)



# ##DETECTAR LITROS GASOLINA
# import re
# import cv2
# import pytesseract
# from pytesseract import Output
#
# img = cv2.imread('Tmp/girado.png')
# d = pytesseract.image_to_data(img, output_type=Output.DICT)
# keys = list(d.keys())
#
# litros = '[0-9][0-9][A-Z]'
#
# n_boxes = len(d['text'])
# for i in range(n_boxes):
#     if float(d['conf'][i]) > 60:
#     	if re.match(litros, d['text'][i]):
# 	        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
# 	        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# cv2.imshow('img', img)
# cv2.waitKey(0)
