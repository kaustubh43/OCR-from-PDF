#importing
import PIL
import sys
from pdf2image import convert_from_path
import os
print('Start with OCR project')

'Converting to image from PDF'
#path of pdf file
PDF_loc="OCR_1.pdf"

images=convert_from_path(PDF_loc,poppler_path = r"C:\Program Files\poppler-0.67.0\bin")

imagecounter=1

for image in images:
    filename="image"+str(imagecounter)+".jpg"
    image.save(filename,'JPEG')
    imagecounter+=1
    
    


