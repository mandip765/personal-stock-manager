import pytesseract
import cv2
import re

def read_bill(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)

    results = []

    for line in text.splitlines():
        line = line.lower().strip()
        match = re.search(r'([a-z\\s]+)[\\-–]\\s*(\\d+)\\s*(kg|ctn|pcs)', line)
        if match:
            results.append({
                'name': match.group(1).strip(),
                'qty': int(match.group(2)),
                'unit': match.group(3)
            })

    return results
