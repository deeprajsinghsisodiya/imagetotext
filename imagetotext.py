
import pytesseract
from PIL import Image

# Set the path to the Tesseract executable if it's not in your PATH environment variable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the image file
# If you don't have tesseract executable in your PATH, include# the following:
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

image_path = 'C:\\Users\\deepr\\Pictures\\Screenshots\\1.png'
image = Image.open(image_path)

# Convert the image to grayscale for better OCR accuracy
image = image.convert('L')

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
