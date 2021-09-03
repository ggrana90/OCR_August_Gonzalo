from pdf2image import convert_from_path
import pytesseract
import cv2
from PIL import Image
import os

#Creamos la carpeta temporal
#wd = os.getcwd()
# print ("El working directory que estoy usando es %s" % wd)

proyecto = "C:/Users/34604/Documents/GitHub/PDF_OCR_v0.1"
carpetatemp = "Tmp"
path = os.path.join(proyecto, carpetatemp)


access_rights = 0o755

try:
    os.mkdir(path, access_rights)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)

### --> SIGUIENTE PASO <--- ###
#De PDF a Imagen
#Cargamos file y definimos ruta de salida(si va muy lento, mejor cambiar el formato a jpeg)
file = "PDF/9456GRG.pdf"
images = convert_from_path(file,poppler_path = r"C:\Program Files\poppler-0.68.0_x86\poppler-0.68.0\bin",output_folder="Tmp",fmt="png",output_file="")



### --> SIGUIENTE PASO <--- ###
#Giramos la foto
im_file = "Tmp/0001-1.png"
im = Image.open(im_file)
# im.rotate(270).show()
# im.save("TicketsRaw/girado2.png")
angle = 270
out = im.rotate(angle, expand=True)
out.save('Temp/girado.png')




### --> SIGUIENTE PASO <--- ###
#Sacamos el negativo de la nueva imagen para que Tesseract funcione mejor al leer el texto
image1 = cv2.imread('Temp/girado.png')

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
cv2.imwrite('Tmp/girado.png',thresh4,None)

# Eliminar lo que haya en memoria
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

### --> SIGUIENTE PASO <--- ###
#Extraemos el texto
image = cv2.imread('Tmp/girado.png',0)
text = pytesseract.image_to_string(image)
print(text)



# ### --> SIGUIENTE PASO <--- ###
# #Eliminamos la carpeta temporal
proyecto = "C:/Users/34604/Documents/GitHub/PDF_OCR_v0.1"
carpetatemp = "Tmp"
path = os.path.join(proyecto, carpetatemp)

try:
    os.rmdir(path)
except OSError:
    print ("Deletion of the directory %s failed" % path)
else:
    print ("Successfully deleted the directory %s" % path)