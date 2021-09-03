from PIL import Image
import cv2
import pytesseract
im_file = "PDF/imagenPIL0001-1.png"
im = Image.open(im_file)
# im.rotate(270).show()
# im.save("TicketsRaw/girado2.png")
angle = 270
out = im.rotate(angle, expand=True)
out.save('girado3.png')