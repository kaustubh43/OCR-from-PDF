#importing
from PIL import Image
import sys
from pdf2image import convert_from_path
import os
import pytesseract

print('Start with OCR project')

class Details:
    'Converting to image from PDF'
    #path of pdf file
    def __init__(self,name):
        self.PDF_loc=name
        self.text=' '
        self.convert()
        
    def convert(self):
        images=convert_from_path(self.PDF_loc,poppler_path = r"C:\Program Files\poppler-0.67.0\bin")

        imagecounter=1

        for image in images:
            filename="image"+str(imagecounter)+".jpg"
            image.save(filename,'JPEG')
            imagecounter+=1

            
        'Converting Image to text file'

        files=imagecounter-1

        output_file='output_file.txt'

        f=open(output_file,'w')

        #sepcifying tesseract installation location
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        for i in range(1,files+1):

            filename="image"+str(i)+".jpg"


            self.text=str(((pytesseract.image_to_string(Image.open(filename),lang='eng'))))
                      
            self.text=self.text.replace('-\n','')

            f.write(self.text)

        f.close()
        self.display()
        
    def display(self):
        if (self.PDF_loc=="OCR_1.pdf"):
            IEC=self.text[self.text.find('IEC')+3:self.text.find('Name')]
            print('IEC',IEC)
            POL=self.text[self.text.find('Port of Loading')+7:self.text.find('Total Pkgs')]
            print('Port of Loading',POL)
            POD=self.text[self.text.find('Discharge')+9:self.text.find('Loose p')]
            print('Port of Discharge',POD)
            GW=self.text[self.text.find('Gross wt')+13:self.text.find('Net Wt')]
            print('Gross Weight',GW)
            CD=self.text[self.text.find('Country of Dest')+16:self.text.find('No.of Ctrs')]
            print('Country of Destination',CD)
            TP=self.text[self.text.find('Total Pkgs')+11:self.text.find('Port of D')]
            TP.replace('\n\n','')
            print('Total Packages',TP,end='')
            LP=self.text[self.text.find('Loose pckts')+11:self.text.find('Gross wt')]
            LP.replace('\n','')
            print('Loose Packages',LP,end='')
            NW=self.text[self.text.find('Net Wt')+11:self.text.find('Country of Dest')-2]
            NW.replace('\n\n','')
            print('Net weight ',NW,end='')
            NC=self.text[self.text.find('No.of Ctrs')+11:self.text.find('Nature of Cargo')]
            NC.replace('\n\n','')
            
        elif self.PDF_loc=="OCR_2.pdf":
            f=open('output_file.txt','r')
            print(self.text[self.text.find('Con Det')+8:self.text.find('Date')+5])
            f.seek(self.text.find('Date')+5)
            f.readline()
            f.readline()
            print(f.readline())
            f.readline()
            print(f.readline())

                  
name="OCR_2.pdf"
test=Details(name)
    
    



