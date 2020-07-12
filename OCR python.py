#importing
from PIL import Image
import sys
from pdf2image import convert_from_path
import os
import pytesseract

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

    
'Converting Image to text file'

files=imagecounter-1

output_file='output_file.txt'

f=open(output_file,'a')

#sepcifying tesseract installation location
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

for i in range(1,files+1):

    filename="image"+str(i)+".jpg"


    text=str(((pytesseract.image_to_string(Image.open(filename),lang='eng'))))
              
    #text=text.replace('-\n','')

    f.write(text)

f.close()
    


    


