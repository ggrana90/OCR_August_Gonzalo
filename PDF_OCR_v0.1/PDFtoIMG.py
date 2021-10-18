from pdf2image import convert_from_path
import pytesseract
import cv2
from PIL import Image
import os
import re
from pytesseract import Output
import shutil

def convertPDFToImage(filename):
    file = "PDF/" + filename
    converted_file = "PDF_Converted/" + filename
    error_file = "Errors" + filename
    convert_from_path(file,output_folder="Pending",fmt="png",output_file="")
    ### --> SIGUIENTE PASO <--- ###
    #Giramos la foto
    im_file = "Pending/0001-1.png"
    im = Image.open(im_file)
    # im.rotate(270).show()
    # im.save("TicketsRaw/girado2.png")
    angle = 270
    out = im.rotate(angle, expand=True)
    out.save('Pending/girado.png')
    ### --> SIGUIENTE PASO <--- ###
    #Sacamos el negativo de la nueva imagen para que Tesseract funcione mejor al leer el texto
    image1 = cv2.imread('Pending/girado.png')

    # cv2.cvtColor para convertir a escala de grises
    img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

    # se pueden aplicar diferentes tecnicas de threshold
    ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

    # quitar quote para previsualizar thresholds. El thresh4 fue la que mejor ha funcionado con los tickets de muestra
    # cv2.imshow('Binario', thresh1)
    # # cv2.imshow('Binario invertido', thresh2)
    # cv2.imshow('Truncado', thresh3)
    # cv2.imshow('Ajustar a cero', thresh4)
    # cv2.imshow('Ajustar a cero invertido', thresh5)
    #escribimos la imagen que nos interesa
    cv2.imwrite('Pending/girado.png',thresh4,None)

    # Eliminar lo que haya en memoria
    #if cv2.waitKey(0) & 0xff == 27:
    #    cv2.destroyAllWindows()

    ### --> SIGUIENTE PASO <--- ###
    #Extraemos el texto
    image = cv2.imread('Pending/girado.png',0)
    # return pytesseract.image_to_data(image, output_type=Output.DICT)['text']
    return pytesseract.image_to_data(image, output_type=Output.DICT)['text']


