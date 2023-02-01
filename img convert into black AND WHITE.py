from PIL import Image
img =Image.open('C:\\users\\hp\\itachi 2.jpg');
bw=img.convert("L")
bw.show()