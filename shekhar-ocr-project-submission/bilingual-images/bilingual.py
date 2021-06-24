import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

'''
--------------------------------------------------------------------------
bilingual.png
--------------------------------------------------------------------------
'''

img = cv2.imread('./bilingual-images/bilingual.png')
config = "--psm 3 --oem 3"
text = str(pytesseract.image_to_string(img, config=config, lang="tam+eng"))
text = text.replace('-\n', '')
with open('./bilingual-images/bilingual.txt', "w",  encoding="utf-8") as f:
    f.write(text)

'''
--------------------------------------------------------------------------
bilingual-2.png
--------------------------------------------------------------------------
'''

img = cv2.imread('./bilingual-images/bilingual-2.png',2) # reading and converting image to grayscale

config = "--psm 3 --oem 3"
text = str(pytesseract.image_to_string(img, config=config, lang="tam+eng"))
text = text.replace('-\n', '')

with open('./bilingual-images/bilingual-2.txt', "w",  encoding="utf-8") as f:
    f.write(text)

'''
--------------------------------------------------------------------------
bilingual-3.png
--------------------------------------------------------------------------
'''
img = cv2.imread('./bilingual-images/bilingual-3.png',2)

config = "--psm 4 --oem 3"
text = str(pytesseract.image_to_string(img, config=config, lang="tam+eng"))
text = text.replace('-\n', '')

with open('./bilingual-images/bilingual-3.txt', "w",  encoding="utf-8") as f:
    f.write(text)