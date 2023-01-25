import os
import sys

from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
from PIL import Image
import pytesseract


def save_file(filename, content):
    with open(filename + ".txt", "w+") as fh:
        fh.write(content)
        
def process_pdf(path, target_file):
    images = convert_from_path(path)
    print(images)
    for i, image in enumerate(images):
        s = pytesseract.image_to_string(image)
        print(s)
        save_file(target_file + " - " + "Page " + str(i) + ".txt", s)
            
def process_single_image(path, target_file):
    image = Image.open(path)
    s = pytesseract.image_to_string(image)
    print(s)
    save_file(target_file + ".txt", s)
        
def get_file_parts(path):
    parts = os.path.splitext(path)
    filename = parts[0]
    fileext = parts[1]
    return filename, fileext

def main():
    path = sys.argv[1]
    filename, fileext = get_file_parts(path)
    
    if fileext == ".pdf":
        process_pdf(path, filename)
    else:
        process_single_image(path, filename)
    input("\nPress any key to exit")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        input(e)