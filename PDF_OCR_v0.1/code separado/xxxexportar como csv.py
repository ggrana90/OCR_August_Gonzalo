import pytesseract
from PIL import Image # pip install Pillow

# set tesseract cmd to the be the path to your tesseract engine executable
# (where you installed tesseract from above urls)

# IMPORTANT: this should end with '...\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = <path_to_your_tesseract_cmd>

# and start doing it

# your saved images on desktop
list_with_many_images = [
  "path1",
  "path2"
  # ...
  "pathN"
]

# create a function that returns the text
def image_to_str(path):
    """ return a string from image """
    return pytesseract.image_to_string(Image.open(path))

# now pure action + csv part
with open("images_content.csv", "w+", encoding="utf-8") as file:
  file.write("ImagePath, ImageText")
  for image_path in list_with_many_images:
    text = image_to_str(image_path)
    line = f"{image_path}, {text}\n"
    file.write(line)