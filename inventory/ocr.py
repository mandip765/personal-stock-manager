import pytesseract, cv2

def read_bill(path):
    img = cv2.imread(path)
    text = pytesseract.image_to_string(img)
    return text
