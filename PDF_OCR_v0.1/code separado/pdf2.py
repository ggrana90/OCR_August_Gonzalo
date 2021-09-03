from pdf2image import convert_from_path
import os
import sys
import time



file = "PDF/9456GRG.pdf"

images = convert_from_path(file,poppler_path = r"C:\Program Files\poppler-0.68.0_x86\poppler-0.68.0\bin",output_folder="Temp",fmt="png",output_file="")