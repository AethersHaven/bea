#from pdf2image import convert_from_path
import pdf2image
import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "I:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Returns a cropped image of the first page of the pdf supplied
def GetImage(filePath):
    # Get image
    image = np.array(pdf2image.convert_from_path(filePath)[0])

    # Crop image
    image = image[0:250, 275:1385]

    # Convert the image to gray scale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return image

# Parses through text contained in an image to identify necessary information
# Returned in format: ['Last First', 'ID', 'Date', 'Document Type']
def ProcessPatientInfo(image):
    text = GetText(image)
    info = "Dovie Sullivan\n19860\n030422\na".splitlines()
    #for line in text.splitlines():
    return info

# Returns the text contained in a cropped portion of a pdf file
def GetText(image):
    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    
    # Applying dilation on the threshold image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
    
    # Finding contours
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Creating a copy of image
    image2 = image.copy()

    text = ""

    # Looping through the identified contours
    # Then rectangular part is cropped and passed on
    # to pytesseract for extracting text from it
    # Extracted text is then written into the text file
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        
        # Drawing a rectangle on copied image
        rect = cv2.rectangle(image2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Cropping the text block for giving input to OCR
        cropped = image2[y:y + h, x:x + w]
        
        # Apply OCR on the cropped image
        text += pytesseract.image_to_string(cropped)

    return text