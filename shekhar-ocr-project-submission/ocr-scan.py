import cv2
import numpy as np
import pytesseract
import os
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

'''
--------------------------------------------------------------------------
good-scan.png
--------------------------------------------------------------------------
'''

img = cv2.imread(r'.\scanned-images\good-scan.png',2)
text = pytesseract.image_to_string(img)
text = text.replace('-\n', '')
with open('./scanned-images/good-scan.txt', "w",  encoding="utf-8") as f:
    f.write(text)

'''
--------------------------------------------------------------------------
bad-scan-bad-contrast-and-background-375x487.png
--------------------------------------------------------------------------
'''

img = cv2.imread(r'.\scanned-images\bad-scan-bad-contrast-and-background-375x487.png')
img = cv2.resize(img, None, fx=1.75, fy=1.75)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
config = "--psm 4"
text = str(pytesseract.image_to_string(img, config= config))
text = text.replace('-\n','')
with open('./scanned-images/bad-scan-bad-contrast-and-background-375x487.txt', "w",  encoding="utf-8") as f:
    f.write(text)


'''
--------------------------------------------------------------------------
bad-scan-markings-and-underlines.png
--------------------------------------------------------------------------
'''

gray = cv2.imread(r'.\scanned-images\bad-scan-markings-and-underlines.png',
                cv2.IMREAD_GRAYSCALE)
config = "--psm 4"

# creating filter for dilation to be used to find underlines
kernel = np.ones((1,9), np.uint8)
dilate = cv2.dilate(gray, kernel, iterations=1)

# Removing underline part from the text
new_img = gray + abs(255 - dilate)

text = str(pytesseract.image_to_string(new_img, config= config))
text = text.replace('-\n','')
with open('./scanned-images/bad-scan-markings-and-underlines.txt', "w",  encoding="utf-8") as f:
    f.write(text)


'''
--------------------------------------------------------------------------
bad-scan-text-cut-off.png
--------------------------------------------------------------------------
'''

gray = cv2.imread(r'.\scanned-images\bad-scan-text-cut-off.png',
                cv2.IMREAD_GRAYSCALE)

# A function to read text column-wise since the image has two columns
def columns(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray) #Create a temp file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename) #Remove the temp file
    return text
text = columns(r'.\scanned-images\bad-scan-text-cut-off.png')
with open('./scanned-images/bad-scan-text-cut-off.txt', "w",  encoding="utf-8") as f:
    f.write(text)
