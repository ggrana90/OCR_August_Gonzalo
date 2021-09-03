import cv2
import pytesseract
import csv
import pandas as pd
from pytesseract import Output

img = cv2.imread('Tmp/girado.png',0)
text = pytesseract.image_to_string(img)

# data = pd.DataFrame(list(text), columns=['Review'])
# list(data)
# print(type(text))
#
#
d = pytesseract.image_to_data(img, output_type=Output.DICT)
# print(d.keys())

# n_boxes = len(d['text'])
# for i in range(n_boxes):
#     if int(d['conf'][i]) > 60:
#         (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#         img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# cv2.imshow('img', img)
# cv2.waitKey(0)
 print(d)
