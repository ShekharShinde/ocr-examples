import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def creat_txt_file(file_name, txt_file):
    file = open(file_name,"a")
    file.write(txt_file)
    file.close()


'''
--------------------------------------------------------------------------
multicolor-image.png
--------------------------------------------------------------------------
'''
gray = cv2.imread(r'.\multicolor\multicolor-image.jpg',
                cv2.IMREAD_GRAYSCALE)
hh, ww = gray.shape

# threshold the grayscale image
ret, thresh = cv2.threshold(gray,165,255,0)

# create black image to hold results
results = np.zeros((hh,ww))

# find contours
cntrs = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                         cv2.CHAIN_APPROX_SIMPLE)
cntrs = cntrs[0] if len(cntrs) == 2 else cntrs[1]

# Contour filtering and copy contour interior to new black image.
for c in cntrs:
    area = cv2.contourArea(c)
    if area > 5:
        x,y,w,h = cv2.boundingRect(c)
        results[y:y+h,x:x+w] = thresh[y:y+h,x:x+w]

# invert the results image so that have black letters on white background
results = (255 - results)

# write results to disk
cv2.imwrite("./multicolor/extracted_multicolor_image.png", results)

filename = './multicolor/extracted_multicolor_image.png'
out_txt = "./multicolor/multicolor-image.txt"

custom_config = r"--oem 3 --psm 6 "

f = open(out_txt, 'a')

text = str(((pytesseract.image_to_string(Image.open(filename), 
                                         lang='eng', config= custom_config))))
text = text.replace('-\n', '')
f.write(text)
f.close()


'''
--------------------------------------------------------------------------
mcimage.png
--------------------------------------------------------------------------
'''

gray = cv2.imread(r'.\multicolor\mcimage.png', 2) # reading gray scale image

(_, image_bw) = cv2.threshold(gray, 110, 255,
                               cv2.THRESH_BINARY) # converting to black and white

custom_config = r"--oem 3 --psm 6 "
out_txt = "./multicolor/mcimage.txt"

# writing txt file
f = open(out_txt, 'a')
text = str(pytesseract.image_to_string(image_bw, 
                                         config = custom_config))
text = text.replace('-\n', '')
f.write(text)
f.close()



