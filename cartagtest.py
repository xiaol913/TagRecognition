from PIL import Image
import pytesseract

im = Image.open('tag2.jpg')

imgry = im.convert('L')

threshold = 140

table = []

for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

out = imgry.point(table, '1')

out.show()

print pytesseract.image_to_string(out)
